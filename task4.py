import pandas as pd
import re

# =========================
# TASK 4: pr_commit_details
# =========================

print("Loading pr_commit_details table...")

# The URL for the pr_commit_details table is:
url = "https://huggingface.co/datasets/hao-li/AIDev/resolve/main/pr_commit_details.parquet"

# Load Parquet file into a DataFrame
df_pr_commit_details = pd.read_parquet(url)

print("pr_commit_details table loaded. Columns available:")
print(list(df_pr_commit_details.columns))

# --- Data Cleaning Step (New for Task 4) ---
# Goal: Clean the 'patch' column (PRDIFF) to remove potential encoding issue characters
print("Cleaning 'patch' column to remove special characters...")

# The data in 'patch' is the diff (often a long string).
# We use a simple regular expression to keep only alphanumeric characters, spaces,
# and common punctuation used in code/diffs (like +, -, =, <, >, |, /, \, :, ;, ., ,, (, ), [, ], {, }, #, @, %, &, _, $).
# This is a robust way to handle complex string data before saving to CSV.
df_pr_commit_details['patch_cleaned'] = df_pr_commit_details['patch'].astype(str).apply(
    lambda x: re.sub(r'[^\w\s\+\-\=\<\>\|\/\\:\;\.\,\(\)\[\]\{\}\#\@\%\&\_\$]', '', x)
)
print("Cleaning complete.")

# --- Selection and Renaming ---
df_pr_commit_details_selected = df_pr_commit_details[[
    "pr_id", "sha", "message", "filename", "status", "additions", "deletions", "changes", "patch_cleaned"
]].rename(columns={
    "pr_id": "PRID",
    "sha": "PRSHA",
    "message": "PRCOMMITMESSAGE",
    "filename": "PRFILE",
    "status": "PRSTATUS",
    "additions": "PRADDS",
    "deletions": "PRDELSS",
    "changes": "PRCHANGECOUNT",
    "patch_cleaned": "PRDIFF" # Use the cleaned column
})

# Save to CSV
output_file = "pr_commit_details.csv"
df_pr_commit_details_selected.to_csv(output_file, index=False)

print(f"---")
print(f"Task-4 complete. CSV file '{output_file}' created successfully.")
print(f"Total rows: {len(df_pr_commit_details_selected)}")