"""
python train_TransOnly_mask.py --input-path ../data/processed --val-path ..data/val_files/val_mask_noCiECGT512.pkl --output-path ../data/output
"""
import pickle
import warnings
from datetime import datetime
from itertools import repeat
from pathlib import Path

import mlflow
import numpy as np
import torch
import typer
from artifact import Saw
from data import CachedArtifactDataset, RealisticArtifactDataset
from mask_detector import WindowTransformerDetector
from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import (
    EarlyStopping,
    LearningRateMonitor,
    ModelCheckpoint,
)
from pytorch_lightning.loggers import MLFlowLogger
from torch.utils.data import DataLoader
from utilities import parameters_k

# stop warnings
torch.set_float32_matmul_precision("high")
warnings.filterwarnings("ignore", ".*does not have many workers.*")

# width of window
width = 512
convolution_features = [32]  # small input embedding to mostly determine performance of transformer blocks
convolution_width = [8]
convolution_dropout = 0.0
transformer_heads = 8  # embedding dimension must be divisible by number of heads
transformer_feedforward = 256
transformer_layers = 4
transformer_dropout = 0
loss = "mask"
loss_boost_fp = 0.2
artifact = Saw()
warmup = 30
batch_size = 32  # 'values': [32, 64, 128]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

# model
model = WindowTransformerDetector(
    window=width,
    convolution_features=convolution_features,
    convolution_width=convolution_width,
    convolution_dropout=convolution_dropout,
    transformer_heads=transformer_heads,
    transformer_feedforward=transformer_feedforward,
    transformer_layers=transformer_layers,
    transformer_dropout=transformer_dropout,
    loss=loss,
    loss_boost_fp=loss_boost_fp,
    warmup=warmup,
)

model_name = f"{model.__class__.__name__}_{parameters_k(model)}_{datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}"
run_name = model_name


train_datasets = [
    # # 'CinCECGTorso', # do not train on this dataset for validation purposes
    "ETTm",  # 1
    "ETTh",  # 2
    "electricity_load_diagrams",  # 3
    "australian_electricity_demand_dataset",  # 4
    "Phoneme",  # 5
    "electricity_hourly_dataset",  # 6
    "HouseholdPowerConsumption1",  # 7
    "london_smart_meters_dataset_without_missing_values",  # 8
    "SemgHandGenderCh2",  # 9
    "PigCVP",  # 10
    "HouseTwenty",  # 11
    "wind_farms_minutely_dataset_without_missing_values",  # 12
    "ptbdb",  # 13
    "mitbih",  # 14
    "PigArtPressure",  # 15
    "solar_10_minutes_dataset",  # 16
    "Mallat",  # 17
    "MixedShapesRegularTrain",  # 18
    "Rock",  # 19
    "ACSF1",  # 20
]
print(model_name)


def load_series(names: list[str], split: str, path: str):
    series: list[np.ndarray] = list()
    counts: list[float] = list()
    for name in names:
        try:
            with open(f"{path}/{name}_{split}.pickle", "rb") as f:
                raw = [a for a in pickle.load(f) if len(a) > width]
                series.extend(np.array(a).astype(np.float32) for a in raw)
                counts.extend(repeat(1 / len(raw), len(raw)))
        except:
            print(f"Dataset {name} not in input folder!")
    counts = np.array(counts)
    return series, np.divide(counts, np.sum(counts))


# Run it:
def main(
    input_path: Path = typer.Option(default=...),
    val_path: Path = typer.Option(default=...),
    output_path: Path = typer.Option(default=...),
):
    """
    Args:
        input_path (Path): directory containing datasets
        val_path (Path): directory containig validation file, in case it was already created
        output_path (Path): directory where to store the trained model
    """
    # Check GPU connection:
    print("GPU: %s", torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    # Check input arguments are right:
    assert (
        input_path.resolve().is_dir()
    ), f"Provided 'input_path' directory ({input_path}) doesn't exist!"

    # initialize logger
    logger = MLFlowLogger(
        log_model="all",
        run_name=model_name,
        experiment_name="artifactory_transformer_detector",
        tracking_uri=mlflow.get_tracking_uri(),
    )

    # validation
    val_file = Path(f"{val_path}")
    val = CachedArtifactDataset(file=val_file)
    val_loader = DataLoader(val, batch_size=batch_size)

    # train
    train_data, train_weights = load_series(train_datasets, "TRAIN", str(input_path))
    train_dataset = RealisticArtifactDataset(
        train_data,
        width=width,
        padding=64,
        artifact=artifact,
        weight=train_weights,
    )
    train_loader = DataLoader(train_dataset, batch_size=batch_size)

    # sanity check
    batch = next(iter(train_loader))
    batch["data"]

    # initialize callbacks
    checkpointcallback = ModelCheckpoint(
        monitor="val_fbeta",
        mode="max",
        save_top_k=1,
        dirpath=f"{output_path}/{model_name}",
    )
    lr_monitor = LearningRateMonitor(logging_interval="step")
    early_stop_callback = EarlyStopping(
        monitor="val_fbeta", min_delta=0.0, patience=20, verbose=True, mode="max"
    )

    print("mlflow_uri: ", mlflow.get_tracking_uri())

    # initialize trainer
    trainer = Trainer(
        logger=logger,
        max_steps=50000,
        val_check_interval=500,
        callbacks=[checkpointcallback, lr_monitor, early_stop_callback],
    )

    # Auto log all MLflow entities
    mlflow.pytorch.autolog(log_every_n_step=500)

    print("Starting training.")
    trainer.fit(model, train_dataloaders=train_loader, val_dataloaders=val_loader)

    print("Training completed.")

    print("Job completed successfully.")


if __name__ == "__main__":
    typer.run(main)
