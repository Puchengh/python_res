from pyspark import SparkContext

import os
import os

os.environ['PYSPARK_PYTHON'] = "E:/soft/anaconda3/envs/python38/python.exe"

if __name__ == '__main__':
    sc = SparkContext(master="local[*]", appName="pyspark")
    sc.setLogLevel("ERROR")

    lines = sc.textFile("E:/study/python_res/4Spark/data/words.txt")

    result = lines.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b).collect()

    print(result)
    # for (word,count) in result:
    #     print(f"${word}/t${count}")
