from pyspark.sql import SparkSession, functions as F
from pyspark.sql.functions import split, explode

if __name__ == '__main__':
    spark = SparkSession.builder.appName("pyspark").master("local[*]").getOrCreate()
    df = spark.readStream.format("socket").option("host", "study").option("port", "9999").load()

    words_df = df.select(explode(split(df.value, " ")).alias("word"))

    words_df.createOrReplaceTempView("t_words")

    # sql
    result1 = spark.sql("select word,count(*) as counts from t_words group by word order by counts desc ")

    # dsl
    result2 = words_df.groupBy("word").count().orderBy("count", ascending=False)

    result1.writeStream.format("console") \
        .outputMode("complete") \
        .option("checkpointLocation", "E:/study/python_res/4Spark/data/reslut1") \
        .start()

    result2.writeStream.format("console") \
        .outputMode("complete") \
        .option("checkpointLocation", "E:/study/python_res/4Spark/data/reslut2") \
        .start() \
        .awaitTermination()

    spark.stop()
