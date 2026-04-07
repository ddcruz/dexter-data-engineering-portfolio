from pyspark.sql import SparkSession


def main() -> None:
    spark = SparkSession.builder.appName("spark-on-k8s").getOrCreate()

    data = [("hello", 1), ("spark", 2), ("k8s", 3)]
    df = spark.createDataFrame(data, ["word", "id"])
    df.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()
