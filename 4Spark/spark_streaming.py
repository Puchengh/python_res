from pyspark import SparkContext
from pyspark.streaming import StreamingContext

import os

os.environ['PYSPARK_PYTHON'] = "E:/soft/anaconda3/envs/python38/python.exe"

if __name__ == '__main__':
    sc = SparkContext(master="local[*]", appName="pyspark")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 5)

    lines = ssc.socketTextStream("study", 9999)

    result = lines.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)

    result.pprint()
    ssc.start()
    ssc.awaitTermination()
    # for (word,count) in result:
    #     print(f"${word}/t${count}")
