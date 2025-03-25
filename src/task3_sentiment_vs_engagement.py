from pyspark.sql import SparkSession
from pyspark.sql.functions import when, avg, col

# Initialize Spark Session
spark = SparkSession.builder.appName("SentimentVsEngagement").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).option("inferSchema", True).csv("input/posts.csv")

# Categorize Sentiment
posts_df = posts_df.withColumn(
    "SentimentCategory",
    when(col("SentimentScore") > 0.3, "Positive")
    .when(col("SentimentScore") < -0.3, "Negative")
    .otherwise("Neutral")
)

# Calculate average Likes and Retweets per sentiment category
sentiment_stats = posts_df.groupBy("SentimentCategory").agg(
    avg("Likes").alias("AvgLikes"),
    avg("Retweets").alias("AvgRetweets")
)

# Save result as CSV
sentiment_stats.coalesce(1).write.mode("overwrite").csv("outputs/sentiment_engagement.csv", header=True)

print("✅ Task 3 Sentiment vs Engagement analysis complete. Output saved to outputs/sentiment_engagement.csv")

spark.stop()
