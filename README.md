# High-Performance XML Streaming & DGR Validation Pipeline

A memory-efficient Python ETL solution designed to extract, process, and validate Australian Business Register (ABR) registry archives and Deductible Gift Recipient (DGR) statuses.

## 🚀 Key Features

- **Memory-Efficient Parsing:** Utilizes `lxml.iterparse` for streaming multi-gigabyte XML datasets without memory overhead or Out-Of-Memory (OOM) failures.
- **Automated DGR Status Verification:** Scrapes and validates live tax-deductible gift recipient eligibility via ABN Lookup.
- **Resilient Execution & Checkpointing:** Built-in batching and auto-saving mechanisms to resume processing seamless after interruptions.
- **Data Standardization:** Parses raw unstructured HTML/XML nodes into structured, production-ready Excel and CSV reports.

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Data Processing:** `pandas`, `lxml`
- **Web Scraping & Parsing:** `requests`, `BeautifulSoup4`

## 📦 Usage

1. **Install Dependencies:**
   ```bash
   pip install pandas requests beautifulsoup4 openpyxl lxml
