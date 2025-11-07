import pandas as pd

# =========================
# TASK 1: all_pull_request
# =========================

print("Loading all_pull_request table...")

# Directly load from the source Parquet file on Hugging Face
url = "https://huggingface.co/datasets/hao-li/AIDev/resolve/main/all_pull_request.parquet"
df_pr = pd.read_parquet(url)

print("all_pull_request table loaded. Columns available:")
print(list(df_pr.columns))

# Select and rename required columns
df_pr_selected = df_pr[["title", "id", "agent", "body", "repo_id", "repo_url"]].rename(columns={
    "title": "TITLE",
    "id": "ID",
    "agent": "AGENTNAME",
    "body": "BODYSTRING",
    "repo_id": "REPOID",
    "repo_url": "REPOURL"
})

# Save to CSV
output_file = "pull_requests.csv"
df_pr_selected.to_csv(output_file, index=False)

print(f"Task-1 complete. CSV file '{output_file}' created successfully.")
print(f"Total rows: {len(df_pr_selected)}")
