#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact.
"""

import argparse
import logging
import os

import pandas as pd
import wandb

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    run = wandb.init(project="nyc_airbnb", job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    logger.info("Downloading artifact")
    local_path = run.use_artifact(args.input_artifact).file()

    df = pd.read_csv(local_path)

    logger.info("Dropping price outliers")
    idx = df["price"].between(args.min_price, args.max_price)
    df = df[idx].copy()

    logger.info("Converting last_review to datetime")
    logger.info("Saving clean data to csv")
    df.to_csv(args.output_artifact, index=False)

    logger.info(f"Uploading {args.output_artifact} to Weights & Biases")
    artifact = wandb.Artifact(
        args.output_artifact, type=args.output_type, description=args.output_description
    )
    artifact.add_file(args.output_artifact)
    run.log_artifact(artifact)

    os.remove(args.output_artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="name of W&B artifact to be used as input",
        required=True,
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="name of W&B artifact to be stored as output",
        required=True,
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="W&B artifact type for the output artifact",
        required=True,
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="W&B artifact description for the output artifact",
        required=True,
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="lower price limit for the dataset",
        required=True,
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="upper price limit for the dataset",
        required=True,
    )

    args = parser.parse_args()

    go(args)
