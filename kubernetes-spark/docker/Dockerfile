FROM apache/spark:3.5.1

USER root
WORKDIR /opt/spark

# Copy your Spark jobs into the image path referenced by spark-submit.
COPY jobs/ /opt/spark/jobs/

USER 185
