# Top 20 Hashtags Analyzer

## Project Description
This project analyzes a collection of tweets to identify and count the top 20 hashtags using Apache Spark on Amazon EMR (Elastic MapReduce). We chose Spark for its ability to handle large datasets efficiently and its compatibility with Python.

## Implementation Details
1. Data Source: JSON file from Amazon S3
2. Processing: Used regular expressions to extract hashtags
3. Analysis: Counted hashtag occurrences and identified the top 20
4. Output: Results printed and saved to an S3 bucket

## Code Structure
- `fetch_hashtags`: Extracts hashtags from a tweet
- `process_tweets`: Processes the tweet RDD to count hashtags
- `get_top_hashtags`: Retrieves the top 20 hashtags
- `print_top_hashtags`: Prints the top hashtags to console
- `main`: Orchestrates the entire process

## Setup and Execution
1. Ensure access to an Amazon EMR cluster with Spark installed
2. Upload the Python script to your EMR cluster
3. Run the script: `spark-submit top_20_hashtags.py`


## Top 20 Hashtags Results
1. #melbourne: 1759
2. #stkilda: 968
3. #australia: 510
4. #beach: 443
5. #ausgp: 410
6. #love: 313
7. #f1: 303
8. #sunset: 277
9. #votearianagrande: 239
10. #portmelbourne: 226
11. #stkildabeach: 214
12. #albertpark: 206
13. #buybreakfreeonitunesnow: 204
14. #summer: 196
15. #italianality: 110
16. #food: 96
17. #victoria: 94
18. #travel: 91
19. #coffee: 89
20. #nofilter: 86
