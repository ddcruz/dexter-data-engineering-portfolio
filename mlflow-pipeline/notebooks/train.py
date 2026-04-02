import os
from pathlib import Path

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def configure_mlflow() -> tuple[str, str]:
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{PROJECT_ROOT / 'mlflow.db'}")
    experiment_name = os.getenv("MLFLOW_EXPERIMENT", "mlflow-training-inference-demo")

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    return tracking_uri, experiment_name


def main() -> None:
    tracking_uri, experiment_name = configure_mlflow()
    registered_model_name = os.getenv("REGISTERED_MODEL_NAME", "wine-quality-model")

    X, y = load_wine(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    with mlflow.start_run(run_name="rf-train") as run:
        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            random_state=42,
        )
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_params({"n_estimators": 200, "max_depth": 8, "random_state": 42})
        mlflow.log_metric("accuracy", acc)

        signature = infer_signature(X_train, model.predict(X_train))
        model_info = mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name=registered_model_name,
            signature=signature,
            input_example=X_train[:2],
        )

        print(f"Run ID: {run.info.run_id}")
        print(f"Accuracy: {acc:.4f}")
        print(f"Tracking URI: {tracking_uri}")
        print(f"Experiment: {experiment_name}")
        print(f"Registered model: {registered_model_name}")
        print(f"Model URI: {model_info.model_uri}")


if __name__ == "__main__":
    main()
