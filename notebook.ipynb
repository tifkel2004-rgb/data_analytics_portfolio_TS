# ==============================================================================
# 1. Pipeline Environment & Authentication Setup
# ==============================================================================
import os
from google.cloud import bigquery
import pandas as pd

# Initialize Google BigQuery Client
# Note: Ensure GOOGLE_APPLICATION_CREDENTIALS environment variable is mapped if local
client = bigquery.Client()

# Core Dataset & Table references pointing to the live public Hacker News pool
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
table_ref = dataset_ref.table("full")
table = client.get_table(table_ref)

# Configure safe execution budget limits (Max 10 GB billing threshold to save costs)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)

# ==============================================================================
# 2. Analytics Target 1: High-Volume Contributor Subsets
# ==============================================================================
# Objective: Isolate accounts responsible for writing > 10,000 distinct records.
# Note: Backticks escape the reserved word `by`, which maps back to the 'author' alias.
prolific_commenters_query = """
SELECT 
    `by` AS author, 
    COUNT(1) AS NumPosts
FROM `bigquery-public-data.hacker_news.full`
GROUP BY `by`
HAVING COUNT(1) > 10000
"""

# Execute pipeline data request and format output payload matrix
query_job_1 = client.query(prolific_commenters_query, job_config=safe_config)
prolific_commenters_df = query_job_1.to_dataframe()

print("--- Prolific Commenters DataFrame Summary ---")
print(prolific_commenters_df.head())

# ==============================================================================
# 3. Analytics Target 2: Quantitative Deletion Performance Deltas
# ==============================================================================
# Objective: Calculate the exact cumulative volume of records flagged with an active deletion status.
deleted_comments_query = """
SELECT 
    COUNT(1) AS num_deleted_comments
FROM `bigquery-public-data.hacker_news.full`
WHERE deleted = True
"""

# Run processing job and parse output stream into a summary framework
query_job_2 = client.query(deleted_comments_query, job_config=safe_config)
deleted_comments_df = query_job_2.to_dataframe()

print("\n--- Structural Audit Deletion Summary ---")
print(deleted_comments_df)
