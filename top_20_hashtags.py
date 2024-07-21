import re
from pyspark.sql import SparkSession

def fetch_hashtags(tweet_text):
    return re.findall(r'#(\w+)', tweet_text.lower())

def process_tweets(tweet_rdd):
    return tweet_rdd.flatMap(fetch_hashtags) \
                    .map(lambda tag: (tag, 1)) \
                    .reduceByKey(lambda a, b: a + b)

def get_top_hashtags(hashtag_counts, n=20):
    return hashtag_counts.takeOrdered(n, key=lambda x: -x[1])

def print_top_hashtags(top_hashtags):
    print("Top 20 Hashtags:")
    for tag, count in top_hashtags:
        print(f"#{tag}: {count}")

def main():
    spark = SparkSession.builder \
        .appName("Top 20 Hashtags") \
        .getOrCreate()

    # Read tweets
    tweet_data = spark.read.json('s3://p2-inputdata/smallTwitter.json').rdd

    # Process tweets
    hashtag_counts = process_tweets(tweet_data.map(lambda row: row.text))

    # Get top hashtags
    top_hashtags = get_top_hashtags(hashtag_counts)

    # Print top hashtags
    print_top_hashtags(top_hashtags)

    # Write to file
    output_path = "s3://cloudcomputingvt/Sriharsha/top_20_hashtags.txt"
    spark.sparkContext.parallelize([top_hashtags]).saveAsTextFile(output_path)

    spark.stop()

if __name__ == "__main__":
    main()