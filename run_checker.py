import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

def check_abn_dgr(abn):
    """
    Checks the DGR (Deductible Gift Recipient) status 
    by parsing the official ABN Lookup page structure.
    """
    abn_clean = str(abn).replace(" ", "").strip()
    url = f"https://abr.business.gov.au/ABN/View?id={abn_clean}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Locate tables on the page and find the DGR section
            tables = soup.find_all('table')
            for table in tables:
                table_text = table.get_text()
                if "Deductible gift recipient status" in table_text:
                    # Check if the section contains active records (e.g., 'From' date)
                    if "From" in table_text or "from" in table_text:
                        if "Not entitled" not in table_text:
                            return "Yes"
            
            return "No"
        else:
            return f"HTTP Error {response.status_code}"
            
    except Exception as e:
        print(f"Error checking ABN {abn}: {e}")
        return "Error"

def process_charity_file(input_file, output_file, batch_size=10):
    print(f"Loading file: {input_file}...")
    df = pd.read_excel(input_file)
    
    # Ensure correct data types
    df['ABN'] = df['ABN'].astype(str)
    df['DGR'] = df['DGR'].astype(object)
        
    total_rows = len(df)
    print(f"Total rows to process: {total_rows}\n" + "-"*50)
    
    for idx, row in df.iterrows():
        # Skip already checked rows for resume capability after failures
        if pd.notna(row['DGR']) and row['DGR'] not in ["Error", "Not Checked", "", "HTTP Error", "No"]:
            continue
            
        abn = row['ABN']
        dgr_status = check_abn_dgr(abn)
        df.at[idx, 'DGR'] = dgr_status
        
        print(f"Row {idx + 1}/{total_rows} | ABN: {abn} | DGR: {dgr_status}")
        
        # Polite delay to prevent server blocking
        time.sleep(0.4) 
        
        # Checkpoint: save progress every batch_size rows
        if (idx + 1) % batch_size == 0 or (idx + 1) == total_rows:
            df.to_excel(output_file, index=False)
            print(f">>> Intermediate progress saved ({idx + 1}/{total_rows}) <<<\n")

if __name__ == "__main__":
    input_path = "ACNC LIST .xlsx"
    output_path = "ACNC_LIST_Processed.xlsx"
    process_charity_file(input_path, output_path, batch_size=10)