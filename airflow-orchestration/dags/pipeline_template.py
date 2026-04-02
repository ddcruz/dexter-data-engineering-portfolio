from datetime import timedelta
import os

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule

USE_DATABRICKS = os.getenv("USE_DATABRICKS", "false").lower() == "true"

if USE_DATABRICKS:
        from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator


default_args = {
        "owner": "data-platform",
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
}


def ingest(**context):
        run_date = context["ds"]
        print(f"Ingestion step for {run_date}")


def transform_local(**context):
        run_date = context["ds"]
        print(f"Local transform step for {run_date}")


def validate(**context):
        run_date = context["ds"]
        print(f"Validation step for {run_date}")
        # Replace this with real quality checks and raise exceptions on failure.


def publish(**context):
        run_date = context["ds"]
        print(f"Publishing curated output for {run_date}")


with DAG(
        dag_id="orchestration_pipeline_template",
        description="Ingest -> Transform -> Validate -> Publish",
        schedule_interval="0 6 * * *",
        start_date=days_ago(1),
        catchup=False,
        max_active_runs=1,
        default_args=default_args,
        tags=["orchestration", "template"],
) as dag:
        start = EmptyOperator(task_id="start")

        ingest_task = PythonOperator(
                task_id="ingest",
                python_callable=ingest,
                execution_timeout=timedelta(minutes=15),
        )

        if USE_DATABRICKS:
                transform_task = DatabricksRunNowOperator(
                        task_id="transform_databricks",
                        databricks_conn_id="databricks_default",
                        job_id=int(os.getenv("DATABRICKS_JOB_ID", "0")),
                )
        else:
                transform_task = PythonOperator(
                        task_id="transform_local",
                        python_callable=transform_local,
                        execution_timeout=timedelta(minutes=20),
                )

        validate_task = PythonOperator(
                task_id="validate",
                python_callable=validate,
                execution_timeout=timedelta(minutes=10),
        )

        publish_task = PythonOperator(
                task_id="publish",
                python_callable=publish,
                execution_timeout=timedelta(minutes=10),
        )

        notify_failure = EmptyOperator(
                task_id="notify_failure",
                trigger_rule=TriggerRule.ONE_FAILED,
        )

        end = EmptyOperator(task_id="end")

        start >> ingest_task >> transform_task >> validate_task >> publish_task >> end
        [ingest_task, transform_task, validate_task, publish_task] >> notify_failure

