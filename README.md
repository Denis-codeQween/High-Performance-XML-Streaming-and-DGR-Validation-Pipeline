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

### 1. Clone the Repository
```bash
git clone https://github.com/Denis-codeQween/High-Performance-XML-Streaming-and-DGR-Validation-Pipeline
cd High-Performance-XML-Streaming-and-DGR-Validation-Pipeline
```

### 2. Install Dependencies
Install via `requirements.txt` (recommended):
```bash
pip install -r requirements.txt
```
Or install the required packages directly:
```bash
pip install pandas requests beautifulsoup4 openpyxl lxml
```

### 3. Run the Pipeline
Place your ABR XML archive into the data directory and execute the main script:
```bash
python main.py
```
