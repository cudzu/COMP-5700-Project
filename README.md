## Overview

This project focuses on analyzing AI-generated pull requests and repositories from the [AIDev dataset](https://huggingface.co/datasets/hao-li/AIDev) to understand the types of security-related tasks performed by agentic AI tools. The project extracts relevant information into CSV files for further exploration and analysis.

The analysis is part of a course project and demonstrates practical skills in dataset extraction, cleaning, and organization using Python.

## Dataset

- **Source:** [Hugging Face AIDev Dataset](https://huggingface.co/datasets/hao-li/AIDev)
- **Data Included:**
  - `all_pull_request.parquet` – contains AI-generated pull requests.
  - `all_repository.parquet` – contains repository metadata.

- **Size:**
  - Pull Requests: ~933,000 rows
  - Repositories: ~183,000 rows

## Project Structure

```
.
├── project.py                 # Combined script for Task-1 and Task-2
├── pull_requests.csv          # Generated CSV from Task-1
├── repositories.csv           # Generated CSV from Task-2
└── README.md
```

## Tasks

### Task-1: Extract Pull Request Data

- Extracted columns:
  | CSV Header | Source Column |
  |------------|---------------|
  | TITLE      | `title`       |
  | ID         | `id`          |
  | AGENTNAME  | `agent`       |
  | BODYSTRING | `body`        |
  | REPOID     | `repo_id`     |
  | REPOURL    | `repo_url`    |

- Output CSV: `pull_requests.csv`
- Method: Loaded the Parquet file directly using **pandas** to avoid schema mismatch issues.

### Task-2: Extract Repository Data

- Extracted columns:
  | CSV Header | Source Column |
  |------------|---------------|
  | REPOID     | `id`          |
  | LANG       | `language`    |
  | STARS      | `stars`       |
  | REPOURL    | `url`         |

- Output CSV: `repositories.csv`
- Method: Loaded the Parquet file directly using **pandas**, consistent with Task-1.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/AIDev-Security-Analysis.git
cd AIDev-Security-Analysis
```

2. Install required packages:

```bash
pip install pandas pyarrow
```

3. Run the combined script:

```bash
python project.py
```

This will generate:
- `pull_requests.csv`
- `repositories.csv`

## Notes

- Both scripts read Parquet files directly from Hugging Face to avoid schema conflicts.
- The CSV files can be used for further analysis, including identifying security-related tasks performed by AI agents.

## Project Summary

This project investigates AI-generated software development contributions, specifically pull requests and repository data, to explore security-related patterns. By extracting structured datasets from the AIDev repository, we aim to analyze the types of tasks that autonomous AI agents perform in coding environments.

The workflow includes downloading the dataset, processing it using Python, and creating CSV files that isolate relevant fields for analysis. This approach allows for easy exploration of AI behavior in software engineering tasks and provides a foundation for future studies on AI-assisted security improvements.

Through this project, we develop skills in dataset extraction, transformation, and practical data management, while gaining insight into the current capabilities of agentic AI in development workflows.

## References

- [Hugging Face AIDev Dataset](https://huggingface.co/datasets/hao-li/AIDev)

