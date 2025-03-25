from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, lower

spark = SparkSession.builder.appName("Hashtag Trends").getOrCreate()

# ✅ Correct path
posts = spark.read.csv("input/posts.csv", header=True, inferSchema=True)

# Explode the hashtags
hashtags_df = posts.select(explode(split(col("Hashtags"), ",")).alias("Hashtag"))
hashtag_counts = hashtags_df.groupBy(lower(col("Hashtag")).alias("Hashtag")).count().orderBy(col("count").desc())

# Save result
hashtag_counts.coalesce(1).write.mode("overwrite").csv("outputs/hashtag_trends.csv", header=True)

print("✅ Hashtag trends analysis completed. Output saved in outputs/hashtag_trends.csv")

spark.stop()
