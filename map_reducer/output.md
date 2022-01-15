## Run Map Reducer
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -input /user/root/map_reducer/sample.txt -output /user/root/map_reducer/output -mapper mapper.py -reducer reducer.py -file /root/map_reducer/mapper.py -file /root/map_reducer/reducer.py


# Output
[root@sandbox-hdp map_reducer]# hdfs dfs -ls /user/root/map_reducer/output/

Found 2 items

-rw-r--r--   1 root hdfs          0 2022-01-15 11:44 /user/root/map_reducer/output/_SUCCESS

-rw-r--r--   1 root hdfs         58 2022-01-15 11:44 /user/root/map_reducer/output/part-00000

[root@sandbox-hdp map_reducer]# hdfs dfs -cat /user/root/map_reducer/output/part-00000

brown	1

dogs	2

fox	1

jumped	3

lazy	1

over	1

quick	2

the	1
