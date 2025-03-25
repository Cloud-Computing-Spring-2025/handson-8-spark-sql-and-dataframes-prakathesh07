from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_

# Initialize Spark Session
spark = SparkSession.builder.appName("Top Verified Users").getOrCreate()

# ✅ Corrected Paths (no ../)
posts = spark.read.csv("input/posts.csv", header=True, inferSchema=True)
users = spark.read.csv("input/users.csv", header=True, inferSchema=True)

# ✅ Join posts and users on UserID
joined_df = posts.join(users, on="UserID")

# ✅ Filter only Verified Users
verified_df = joined_df.filter(col("Verified") == True)

# ✅ Calculate Reach (Likes + Retweets)
verified_df = verified_df.withColumn("Reach", col("Likes") + col("Retweets"))

# ✅ Aggregate total reach per verified user
top_verified_users = (
    verified_df.groupBy("Username")
    .agg(sum_("Reach").alias("TotalReach"))
    .orderBy(col("TotalReach").desc())
    .limit(5)
)

# ✅ Save the output
top_verified_users.coalesce(1).write.mode("overwrite").csv("outputs/top_verified_users.csv", header=True)

print("✅ Task 4 Completed: Top Verified Users by Reach saved in outputs/top_verified_users.csv")

spark.stop()
