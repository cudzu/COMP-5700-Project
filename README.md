## Overview

This project focuses on analyzing AI-generated pull requests and repositories from the [AIDev dataset](https://huggingface.co/datasets/hao-li/AIDev) to understand the types of security-related tasks performed by agentic AI tools. The project extracts relevant information into CSV files for further exploration and analysis.

The analysis is part of a course project and demonstrates practical skills in dataset extraction, cleaning, joining, classification, and organization using Python.

## Dataset

- **Source:** [Hugging Face AIDev Dataset](https://huggingface.co/datasets/hao-li/AIDev)
## Data Included

This project uses two primary Parquet files from the AIDev dataset and generates multiple CSV files through Tasks 1–5.

### **Source Parquet Files**
- **all_pull_request.parquet**  
  Contains metadata for ~933,000 AI-generated pull requests, including:
  - PR ID  
  - title  
  - body  
  - agent name  
  - repository ID  
  - repository URL  

- **all_repository.parquet**  
  Contains metadata for ~183,000 repositories, including:
  - repository ID  
  - programming language  
  - star count  
  - repository URL  

---

### **Generated CSV Files (Outputs of Tasks 1–5)**

- **pull_requests.csv** (Task-1)  
  Extracted pull request metadata used throughout later tasks.

- **repositories.csv** (Task-2)  
  Extracted repository metadata required for linking PRs to repositories.

- **pr_task_types.csv** (Task-3)  
  Contains PR classification results, type labels, and confidence scores.

- **task4_output.csv** (Task-4)  
  Contains supplemental derived data used for assignment requirements.

- **task5_security_summary.csv** (Task-5)  
  Contains final merged dataset with:
  - PR ID  
  - agent name  
  - PR type  
  - confidence  
  - security keyword flag (1/0)  

These CSVs form the full processed dataset for analyzing agentic AI behavior and security-related patterns in PR generation.

- **Size:**
  - Pull Requests: ~933,000 rows
  - Repositories: ~183,000 rows

## Project Structure

```
.
├── task1.py                     # Script for Task-1 (Pull Request Extraction)
├── task2.py                     # Script for Task-2 (Repository Extraction)
├── task3.py                     # Script for Task-3 (PR Type Classification)
├── task4.py                     # Script for Task-4 (Confidence Aggregation / Supporting Computation)
├── task5.py                     # Script for Task-5 (Security Keyword Analysis)
│
├── pull_requests.csv            # Output of Task-1
├── repositories.csv             # Output of Task-2
├── pr_task_types.csv            # Output of Task-3
├── task4_output.csv             # Output of Task-4
├── task5_security_summary.csv   # Output of Task-5
│
└── README.md
```

## Tasks

### **Task-1: Extract Pull Request Data**

Extracted fields from `all_pull_request.parquet`:

| CSV Header | Source Column |
|------------|---------------|
| TITLE      | `title`       |
| ID         | `id`          |
| AGENTNAME  | `agent`       |
| BODYSTRING | `body`        |
| REPOID     | `repo_id`     |
| REPOURL    | `repo_url`    |

- Output: `pull_requests.csv`
- Method: Loaded Parquet directly using **pandas** to avoid schema mismatch issues.

---

### **Task-2: Extract Repository Data**

Extracted fields from `all_repository.parquet`:

| CSV Header | Source Column |
|------------|---------------|
| REPOID     | `id`          |
| LANG       | `language`    |
| STARS      | `stars`       |
| REPOURL    | `url`         |

- Output: `repositories.csv`
- Method: Same direct Parquet→CSV extraction as Task-1.

---

### **Task-3: Classify Pull Requests by Type**

This task determines the *type* of each pull request and computes a confidence score.

- Input: `pull_requests.csv`
- Output: `pr_task_types.csv` containing:
  | CSV Header  | Description |
  |-------------|-------------|
  | PRID        | Pull request ID |
  | PRTITLE     | Title text |
  | PRREASON    | Classification basis |
  | PRTYPE      | Final type label |
  | CONFIDENCE  | Confidence score |

---

### **Task-4: Additional PR or Repository Processing**

Task-4 performs additional computations required by the assignment (confidence aggregation, supplemental extraction, etc.).

- Output: `task4_output.csv`

---

### **Task-5: Security Keyword Classification**

Task‑5 merges outputs of Task‑1 and Task‑3, then assigns a **SECURITY flag** based on keyword detection.

Security-related keywords include:

```
race, racy, buffer, overflow, stack, integer, signedness,
underflow, improper, unauthenticated, gain access, permission,
cross site, css, xss, denial service, dos, crash, deadlock,
injection, request forgery, csrf, xsrf, forged, security,
vulnerability, vulnerable, exploit, attack, bypass, backdoor,
threat, expose, breach, violate, fatal, blacklist, overrun,
insecure
```

- SECURITY = **1** → keyword appears in title or body  
- SECURITY = **0** → otherwise  

**Output Columns:**
| Column     | Description |
|------------|-------------|
| ID         | Pull Request ID |
| AGENT      | Name of AI agent |
| TYPE       | PR type |
| CONFIDENCE | Confidence score |
| SECURITY   | 1/0 keyword flag |

Output: `task5_security_summary.csv`

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/cudzu/COMP-5700-Project
cd COMP-5700-Project
```

2. Install dependencies:

```bash
pip install pandas pyarrow
```

3. Run scripts:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
```

---

## Notes

- Uses **pandas** for Parquet reading to avoid schema issues.
- CSV outputs are prepared for downstream analysis and security research.
- Suitable for studying AI agent behavior in software engineering workflows.

## References

- [Hugging Face AIDev Dataset](https://huggingface.co/datasets/hao-li/AIDev)
