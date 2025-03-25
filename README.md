**handson-08-sparkSQL-dataframes-social-media-sentiment-analysis**
**Prerequisites**
**Before starting the assignment, ensure you have the following software installed and properly configured on your machine:**

Python 3.x:

**Download and Install Python**

Verify installation:


python3 --version
**PySpark:**

Install using pip:


pip install pyspark
Apache Spark:

Ensure Spark is installed. You can download it from the Apache Spark Downloads page.

**Verify installation by running:**


spark-submit --version
**Docker & Docker Compose (Optional):**

If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.

Docker Installation Guide

Docker Compose Installation Guide

Setup Instructions
1. Project Structure
Ensure your project directory follows the structure below:

css
Copy
Edit
SocialMediaSentimentAnalysis/
├── input/
│   ├── posts.csv
│   └── users.csv
├── outputs/
│   ├── hashtag_trends.csv
│   ├── engagement_by_age.csv
│   ├── sentiment_engagement.csv
│   └── top_verified_users.csv
├── src/
│   ├── task1_hashtag_trends.py
│   ├── task2_engagement_by_age.py
│   ├── task3_sentiment_vs_engagement.py
│   └── task4_top_verified_users.py
├── docker-compose.yml
└── README.md

input/: Contains the input datasets (posts.csv and users.csv)

outputs/: Directory where the results of each task will be saved.

src/: Contains the individual Python scripts for each task.

docker-compose.yml: Docker Compose configuration file to set up Spark.

README.md: Assignment instructions and guidelines.

**2. Running the Analysis Tasks**
You can run the analysis tasks either locally or using Docker.

a. Running Locally
Navigate to the Project Directory:


cd SocialMediaSentimentAnalysis/
**Execute Each Task Using spark-submit:**


spark-submit src/task1_hashtag_trends.py
spark-submit src/task2_engagement_by_age.py
spark-submit src/task3_sentiment_vs_engagement.py
spark-submit src/task4_top_verified_users.py
**Verify the Outputs: Check the outputs/ directory for the resulting files:**


ls outputs/
**b. Running with Docker (Optional)**
Start the Spark Cluster:
docker-compose up -d
**Access the Spark Master Container:**

docker exec -it spark-master bash
**Navigate to the Spark Directory:**

cd /opt/bitnami/spark/
**Run Your PySpark Scripts Using spark-submit:**

spark-submit src/task1_hashtag_trends.py
spark-submit src/task2_engagement_by_age.py
spark-submit src/task3_sentiment_vs_engagement.py
spark-submit src/task4_top_verified_users.py
**Exit the Container:**
exit
**Verify the Outputs: On your host machine, check the outputs/ directory for the resulting files.**

Stop the Spark Cluster:

docker-compose down
**Overview**
In this assignment, you will leverage Spark Structured APIs to analyze social media datasets. Your goal is to extract meaningful insights related to hashtag trends, engagement by age group, sentiment influence, and top verified users. This exercise is designed to enhance your data manipulation and analytical skills using Spark's powerful APIs.

**Objectives**
By the end of this assignment, you should be able to:

Data Loading and Preparation: Import and preprocess data using Spark Structured APIs.

Data Analysis: Perform complex queries and transformations to address specific business questions.

Insight Generation: Derive actionable insights from the analyzed data.

**Dataset**
Dataset: posts.csv
Column Name	Type	Description
PostID	Integer	Unique ID for the post
UserID	Integer	ID of the user who posted
Content	String	Text content of the post
Timestamp	String	Date and time the post was made
Likes	Integer	Number of likes on the post
Retweets	Integer	Number of shares/retweets
Hashtags	String	Comma-separated hashtags used in the post
SentimentScore	Float	Sentiment score (-1 to 1, where -1 is most negative)
Dataset: users.csv
Column Name	Type	Description
UserID	Integer	Unique user ID
Username	String	User's handle
AgeGroup	String	Age category (Teen, Adult, Senior)
Country	String	Country of residence
Verified	Boolean	Whether the account is verified
**Sample Data**
posts.csv

PostID,UserID,Content,Timestamp,Likes,Retweets,Hashtags,SentimentScore
101,1,"Loving the new update! #tech #innovation","2023-10-05 14:20:00",120,45,"#tech,#innovation",0.8
102,2,"This app keeps crashing. Frustrating! #fail","2023-10-05 15:00:00",5,1,"#fail",-0.7
103,3,"Just another day... #mood","2023-10-05 16:30:00",15,3,"#mood",0.0
104,4,"Absolutely love the UX! #design #cleanUI","2023-10-06 09:10:00",75,20,"#design,#cleanUI",0.6
105,5,"Worst experience ever. Fix it. #bug","2023-10-06 10:45:00",2,0,"#bug",-0.9

users.csv

UserID,Username,AgeGroup,Country,Verified
1,@techie42,Adult,US,True
2,@critic99,Senior,UK,False
3,@daily_vibes,Teen,India,False
4,@designer_dan,Adult,Canada,True
5,@rage_user,Adult,US,False
```

---



## **Assignment Tasks**

You are required to complete the following three analysis tasks using Spark Structured APIs. Ensure that your analysis is well-documented, with clear explanations and any relevant visualizations or summaries.

### **1. Hashtag Trends **

**Objective:**

Identify trending hashtags by analyzing their frequency of use across all posts.

**Tasks:**

- **Extract Hashtags**: Split the `Hashtags` column and flatten it into individual hashtag entries.
- **Count Frequency**: Count how often each hashtag appears.
- **Find Top Hashtags**: Identify the top 10 most frequently used hashtags.


**Expected Outcome:**  
A ranked list of the most-used hashtags and their frequencies.

**Example Output:**

| Hashtag     | Count |
|-------------|-------|
| #tech       | 120   |
| #mood       | 98    |
| #design     | 85    |

---

### **2. Engagement by Age Group**

**Objective:**  
Understand how users from different age groups engage with content based on likes and retweets.

**Tasks:**

- **Join Datasets**: Combine `posts.csv` and `users.csv` using `UserID`.
- **Group by AgeGroup**: Calculate average likes and retweets for each age group.
- **Rank Groups**: Sort the results to highlight the most engaged age group.

**Expected Outcome:**  
A summary of user engagement behavior categorized by age group.

**Example Output:**

| Age Group | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Adult     | 67.3      | 25.2         |
| Teen      | 22.0      | 5.6          |
| Senior    | 9.2       | 1.3          |

---

### **3. Sentiment vs Engagement**

**Objective:**  
Evaluate how sentiment (positive, neutral, or negative) influences post engagement.

**Tasks:**

- **Categorize Posts**: Group posts into Positive (`>0.3`), Neutral (`-0.3 to 0.3`), and Negative (`< -0.3`) sentiment groups.
- **Analyze Engagement**: Calculate average likes and retweets per sentiment category.

**Expected Outcome:**  
Insights into whether happier or angrier posts get more attention.

**Example Output:**

| Sentiment | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Positive  | 85.6      | 32.3         |
| Neutral   | 27.1      | 10.4         |
| Negative  | 13.6      | 4.7          |

---

### **4. Top Verified Users by Reach**

**Objective:**  
Find the most influential verified users based on their post reach (likes + retweets).

**Tasks:**

- **Filter Verified Users**: Use `Verified = True` from `users.csv`.
- **Calculate Reach**: Sum likes and retweets for each user.
- **Rank Users**: Return top 5 verified users with highest total reach.

**Expected Outcome:**  
A leaderboard of verified users based on audience engagement.

**Example Output:**

| Username       | Total Reach |
|----------------|-------------|
| @techie42      | 1650        |
| @designer_dan  | 1320        |

---

## **Grading Criteria**

| Task                        | Marks |
|-----------------------------|-------|
| Hashtag Trend Analysis      | 1     |
| Engagement by Age Group     | 1     |
| Sentiment vs Engagement     | 1     |
| Top Verified Users by Reach | 1     |
| **Total**                   | **1** |

---

## 📬 Submission Checklist

- [ ] PySpark scripts in the `src/` directory  
- [ ] Output files in the `outputs/` directory  
- [ ] Datasets in the `input/` directory  
- [ ] Completed `README.md`  
- [ ] Commit everything to GitHub Classroom  
- [ ] Submit your GitHub repo link on canvas

---

Now go uncover the trends behind the tweets 📊🐤✨
