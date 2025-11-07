from datasets import load_dataset
import pandas as pd

# Load the dataset from Hugging Face
print("Loading dataset...")
dataset = load_dataset("hao-li/AIDev")

# The dataset only has a 'train' split which contains all_pull_request data
print("Dataset loaded. Available splits:", dataset.keys())

# Convert to pandas DataFrame
df = pd.DataFrame(dataset["train"])

# Confirm columns available
print("Columns in dataset:", list(df.columns))

# Select only the required columns and rename them
df_selected = df[["title", "id", "agent", "body", "repo_id", "repo_url"]].rename(columns={
    "title": "TITLE",
    "id": "ID",
    "agent": "AGENTNAME",
    "body": "BODYSTRING",
    "repo_id": "REPOID",
    "repo_url": "REPOURL"
})

# Save to CSV file
output_file = "pull_requests.csv"
df_selected.to_csv(output_file, index=False)

print(f"Task-1 complete! CSV file '{output_file}' created successfully.")
print(f"Total rows: {len(df_selected)}")
