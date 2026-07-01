# Amazon Bestselling Books Analysis (2009–2019)

A lightweight, robust command-line analytical pipeline written in Python using Pandas. This tool sanitizes, processes, and extracts clean commercial market insights from an absolute dataset tracking Amazon's top-performing books over a 10-year span.

---
## Project Overview at a Glance

| Section | What It Does / What It Solves | Key Metric / Output |
| :--- | :--- | :--- |
| **Data Cleaning** | Strips whitespaces, drops nulls, deletes $0 free books, sets 0-5 rating limits. | Calculation-safe DataFrames. |
| **Duplicate Strategy** | Splits data into a `unique` list for totals and a `duplicate` list for multi-year trends. | Prevents popular books from warping math. |
| **Part 1: Market Survey** | Counts totals, price extremes (min/max), and overall review/rating averages. | Baseline market health benchmarks. |
| **Part 2: Genre Comparison** | Groups data by Fiction vs. Non-Fiction to compare market share, price, and reviews. | Direct performance comparison. |
| **Part 3: Leaderboards** | Identifies the top 5 authors by book count and top 3 longest-retaining titles  | Visual ranking of elite performers. |
| **Part 4: Market Evolution** | Tabulates the most-rated and most-reviewed book for every individual year. | Year-by-year historical timeline. |
| **Part 5: Correlations** | Calculates a correlation matrix between Price, Reviews, and Ratings. | Mathematical relationship scores. |

---

## Project Architecture
```text
├── data/
│   └── bestsellingbooks.csv   
├── src/
│   └── analysis.py           
|  
└── README.md   
```            
---    
## Technical Stack
- **Language:** Python 3.x
- **Libraries:** Pandas (`pd`), Pathlib (`Path`)
- **Data Source:** Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019)

---

## How To Setup and Run

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/ayus28ayushi-ai/python-projects-abode.git](https://github.com/ayus28ayushi-ai/python-projects-abode.git)
   cd python-projects-abode
   ```

2. **Install Core Dependencies:**
```bash
pip install pandas
```
3. **Execute the Script:**
```bash
   python src/analysis.py
``` 
---
***Author*** - Ayushi Singh

***GitHub Profile*** - https://github.com/ayus28ayushi-ai
