from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("Engagement by Age Group").getOrCreate()

# ✅ Correct paths to input files
posts = spark.read.csv("input/posts.csv", header=True, inferSchema=True)
users = spark.read.csv("input/users.csv", header=True, inferSchema=True)

# Join posts with users
data = posts.join(users, "UserID")

# Group by AgeGroup and compute average likes and retweets
engagement = data.groupBy("AgeGroup").agg(
    avg("Likes").alias("AvgLikes"),
    avg("Retweets").alias("AvgRetweets")
)

# ✅ Save output to outputs folder
engagement.coalesce(1).write.mode("overwrite").csv("outputs/engagement_by_age.csv", header=True)

print("✅ Task 2 Completed: Engagement by Age Group saved in outputs/engagement_by_age.csv")

spark.stop()
