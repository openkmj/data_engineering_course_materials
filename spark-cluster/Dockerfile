FROM ubuntu:20.04

ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64
ENV PATH=$JAVA_HOME/bin:$PATH

ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk ssh rsync vim && \
    apt-get clean

COPY ./hadoop-$HADOOP_VERSION.tar.gz /hadoop-$HADOOP_VERSION.tar.gz
RUN tar -xzf hadoop-$HADOOP_VERSION.tar.gz && \
    mv hadoop-$HADOOP_VERSION $HADOOP_HOME && \
    rm hadoop-$HADOOP_VERSION.tar.gz

COPY ./config/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY ./config/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
COPY ./config/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
COPY ./config/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml

ENV SPARK_VERSION=3.5.4
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

COPY ./spark-3.5.4-bin-without-hadoop.tgz /opt/spark-3.5.4-bin-without-hadoop.tgz
RUN tar -xzf /opt/spark-3.5.4-bin-without-hadoop.tgz -C /opt/ && \
    mv /opt/spark-3.5.4-bin-without-hadoop /opt/spark


RUN ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

RUN echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
RUN echo "hadoop-worker1\nhadoop-worker2\nhadoop-worker3" > $HADOOP_HOME/etc/hadoop/workers
RUN echo "export SPARK_DIST_CLASSPATH=$(hadoop classpath)" >> $SPARK_HOME/conf/spark-env.sh
RUN echo "spark.master yarn" >> $SPARK_HOME/conf/spark-defaults.conf
RUN echo "spark.eventLog.enabled true" >> $SPARK_HOME/conf/spark-defaults.conf
RUN echo "spark.eventLog.dir /tmp/spark-events" >> $SPARK_HOME/conf/spark-defaults.conf
RUN echo "spark.history.fs.logDirectory /tmp/spark-events" >> $SPARK_HOME/conf/spark-defaults.conf
RUN echo "spark.history.ui.port 18080" >> $SPARK_HOME/conf/spark-defaults.conf

CMD service ssh start && tail -f /dev/null
