FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    curl

RUN apt-get install -y python3 python3-pip

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV SPARK_VERSION=3.5.4
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

COPY spark-3.5.4-bin-hadoop3.tgz /opt/
RUN tar -xzvf /opt/spark-3.5.4-bin-hadoop3.tgz -C /opt/ && \
    mv /opt/spark-3.5.4-bin-hadoop3 /opt/spark

RUN pip3 install pyspark
RUN pip3 install jupyter

WORKDIR /opt/spark/work-dir

# CMD ["/bin/bash"]
CMD ["tail", "-f", "/dev/null"]

# spark.yarn.populateHadoopClasspath=true