import pandas as pd

# =========================
# TASK 5: Security CSV
# =========================

# Security-related keywords (exact list from user)
SECURITY_KEYWORDS = [
    "race",
    "racy",
    "buffer",
    "overflow",
    "stack",
    "integer",
    "signedness",
    "underflow",
    "improper",
    "unauthenticated",
    "gain access",
    "permission",
    "cross site",
    "css",
    "xss",
    "denial service",
    "dos",
    "crash",
    "deadlock",
    "injection",
    "request forgery",
    "csrf",
    "xsrf",
    "forged",
    "security",
    "vulnerability",
    "vulnerable",
    "exploit",
    "attack",
    "bypass",
    "backdoor",
    "threat",
    "expose",
    "breach",
    "violate",
    "fatal",
    "blacklist",
    "overrun",
    "insecure"
]

def contains_security_keyword(text: str) -> bool:
    """Return True if any security keyword appears in the given text."""
    if not isinstance(text, str):
        return False
    lower = text.lower()
    return any(kw in lower for kw in SECURITY_KEYWORDS)


def main():
    # 1. Load your Task 1 and Task 3 outputs
    print("Loading Task-1 output: pull_requests.csv ...")
    df_pr = pd.read_csv("pull_requests.csv")

    print("Loading Task-3 output: pr_task_types.csv ...")
    df_task_type = pd.read_csv("pr_task_types.csv")

    # 2. Merge on PR ID
    print("Merging on ID <-> PRID ...")
    df_merged = pd.merge(
        df_pr,
        df_task_type,
        left_on="ID",
        right_on="PRID",
        how="inner"
    )

    print(f"Merged rows: {len(df_merged)}")

    # 3. Compute SECURITY flag
    print("Computing SECURITY flag...")

    def security_flag(row):
        title = row.get("TITLE", "")
        body = row.get("BODYSTRING", "")
        is_sec = contains_security_keyword(title) or contains_security_keyword(body)
        return 1 if is_sec else 0

    df_merged["SECURITY"] = df_merged.apply(security_flag, axis=1)

    # 4. Select & rename columns per Task-5 spec
    df_task5 = df_merged[["ID", "AGENTNAME", "PRTYPE", "CONFIDENCE", "SECURITY"]].rename(
        columns={
            "AGENTNAME": "AGENT",
            "PRTYPE": "TYPE",
        }
    )

    # 5. Save CSV
    output_file = "task5_security_summary.csv"
    df_task5.to_csv(output_file, index=False)

    print("------")
    print(f"Task-5 complete. CSV saved as: {output_file}")
    print(f"Total rows: {len(df_task5)}")
    print(df_task5.head())


if __name__ == "__main__":
    main()
