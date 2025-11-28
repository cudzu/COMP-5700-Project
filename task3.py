import pandas as pd

# =========================
# TASK 3: pr_task_type
# =========================

print("Loading pr_task_type table...")

# Directly read the Parquet file from the Hugging Face repo
# The URL for the pr_task_type table is:
url = "https://huggingface.co/datasets/hao-li/AIDev/resolve/main/pr_task_type.parquet"

# Load Parquet file into a DataFrame
df_pr_task_type = pd.read_parquet(url)

print("pr_task_type table loaded. Columns available:")
print(list(df_pr_task_type.columns))

# Select and rename required columns as per Task 3 instructions
df_pr_task_type_selected = df_pr_task_type[
    ["id", "title", "reason", "type", "confidence"]
].rename(columns={
    "id": "PRID",
    "title": "PRTITLE",
    "reason": "PRREASON",
    "type": "PRTYPE",
    "confidence": "CONFIDENCE"
})

# Save to CSV
output_file = "pr_task_types.csv"
df_pr_task_type_selected.to_csv(output_file, index=False)

print(f"---")
print(f"Task-3 complete. CSV file '{output_file}' created successfully.")
print(f"Total rows: {len(df_pr_task_type_selected)}")