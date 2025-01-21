# Hadoop Multi Node Cluster on Docker

### Build Images
```
docker compose build
```

### Run Containers
```
docker compose up
```

### Format HDFS
If you want to format HDFS, run the following command:
```
hdfs namenode -format
```

### HDFS Test Commands
```
echo "hello world" > test.txt
hdfs dfs -put test.txt /test.txt
hdfs dfs -cat /test.txt
```

### MapReduce Test Commands
```
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 16 1000
```