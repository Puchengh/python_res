from pyspark.sql import SparkSession, functions as F
from pyspark.sql.functions import split, explode

if __name__ == '__main__':
    spark = SparkSession.builder.appName("pyspark").master("local[*]").getOrCreate()

    df = spark.read.text("E:/study/python_res/4Spark/data/words.txt")
    words_df = df.select(explode(split(df.value, " ")).alias("word"))

    words_df.createOrReplaceTempView("t_words")

    # sql
    spark.sql("select word,count(*) as counts from t_words group by word order by counts desc ").show()

    # dsl
    words_df.groupBy("word").count().orderBy("count", ascending=False).show()

    spark.stop()
