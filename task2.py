import pandas as pd

# =========================
# TASK 2: all_repository
# =========================

print("Loading all_repository table...")

# Directly read the Parquet file from the Hugging Face repo
# (Hugging Face hosts it at: https://huggingface.co/datasets/hao-li/AIDev/resolve/main/all_repository.parquet)
url = "https://huggingface.co/datasets/hao-li/AIDev/resolve/main/all_repository.parquet"

# Load Parquet file into a DataFrame
df_repo = pd.read_parquet(url)

print("all_repository table loaded. Columns available:")
print(list(df_repo.columns))

# Select and rename required columns
df_repo_selected = df_repo[["id", "language", "stars", "url"]].rename(columns={
    "id": "REPOID",
    "language": "LANG",
    "stars": "STARS",
    "url": "REPOURL"
})

# Save to CSV
output_file = "repositories.csv"
df_repo_selected.to_csv(output_file, index=False)

print(f"Task-2 complete. CSV file '{output_file}' created successfully.")
print(f"Total rows: {len(df_repo_selected)}")
