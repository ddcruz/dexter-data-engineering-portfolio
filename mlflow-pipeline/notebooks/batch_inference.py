import os
from pathlib import Path

import mlflow
import pandas as pd
from mlflow.tracking import MlflowClient
from sklearn.datasets import load_wine


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def configure_mlflow() -> str:
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{PROJECT_ROOT / 'mlflow.db'}")
    mlflow.set_tracking_uri(tracking_uri)
    return tracking_uri


def resolve_model_uri(client: MlflowClient, model_name: str) -> str:
    explicit_version = os.getenv("MODEL_VERSION")
    if explicit_version:
        return f"models:/{model_name}/{explicit_version}"

    explicit_stage = os.getenv("MODEL_STAGE")
    if explicit_stage:
        return f"models:/{model_name}/{explicit_stage}"

    latest_versions = client.search_model_versions(f"name='{model_name}'")
    if not latest_versions:
        raise RuntimeError(
            f"No registered versions found for model '{model_name}'. Run notebooks/train.py first."
        )

    newest = max(latest_versions, key=lambda mv: int(mv.version))
    return f"models:/{model_name}/{newest.version}"


def main() -> None:
    tracking_uri = configure_mlflow()
    model_name = os.getenv("REGISTERED_MODEL_NAME", "wine-quality-model")

    client = MlflowClient()
    model_uri = resolve_model_uri(client, model_name)
    model = mlflow.pyfunc.load_model(model_uri)

    X, _ = load_wine(return_X_y=True)
    batch_df = pd.DataFrame(X)
    predictions = model.predict(batch_df)

    output_df = batch_df.copy()
    output_df["prediction"] = predictions

    output_dir = PROJECT_ROOT / "inference"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "predictions.csv"
    output_df.to_csv(output_path, index=False)

    print(f"Tracking URI: {tracking_uri}")
    print(f"Model URI used: {model_uri}")
    print(f"Rows scored: {len(output_df)}")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    main()
