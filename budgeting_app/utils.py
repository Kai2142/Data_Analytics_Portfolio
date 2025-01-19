import pdfplumber
import re
from tabulate import tabulate
import pandas as pd


# Extract Test from PDF E-Statement File
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text


def statement_pdf_processing(statement_path: str):
    global numeric_date
    text_data = extract_text_from_pdf(statement_path)
    # Initialize a list to store transaction details
    transactions = []

    # Define a regular expression pattern to extract transaction details
    pattern = r"(\d{2}[A-Z]{3}) (\d{2}[A-Z]{3}) (.*?)(\d{1,3}(?:,\d{3})*\.\d{2})"

    # Find all matches in the text data using the pattern
    matches = re.findall(pattern, text_data)

    # Extract transaction details and store them in a list of dictionaries
    for match in matches:
        transaction_date = match[0]
        post_date = match[1]
        description = match[2].strip()
        amount = float(match[3].replace(',', ''))  # Remove commas from the amount string

        transaction = {
            "Transaction Date": transaction_date,
            "Post Date": post_date,
            "Description": description,
            "Amount": amount
        }

        transactions.append(transaction)

    # Create a DataFrame from the transaction details
    df = pd.DataFrame(transactions)

    # Define a regular expression pattern to match the date in the format DD MMM YYYY
    pattern_date = r"\b\d{2} [A-Z]{3} \d{4}\b"

    # Find the first match in the text using the pattern
    match = re.search(pattern_date, text_data)
    date = match.group() if match else None
    #
    month_map = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
                 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

    if date:
        day, month, year = date.split(' ')
        month_numeric = month_map.get(month)
        numeric_date = f'{day}-{month_numeric}-{year}'

    # File name
    file_name = numeric_date

    # Save the DataFrame to a CSV file
    csv_filename = f'{file_name}.csv'
    df.to_csv(
        f'/Users/kaiisfly/PycharmProjects/Data_Analytics_Portfolio/budgeting_app/e_statement_tables/{csv_filename}',
        index=False)

    # Display transaction details in a table using tabulate
    table_headers = ["Transaction Date", "Post Date", "Description", "Amount"]
    table_data = [[t["Transaction Date"], t["Post Date"], t["Description"], t["Amount"]] for t in transactions]
    return csv_filename
