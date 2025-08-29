from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import string

columns = [
    'Name','Performance Year','Basic EPS Based On Continuous operations',
    'Basic EPS Based On Including Extra-Ordinary Income',
    'Basic EPS (restated) Based On Continuous operations',
    'Basic EPS (restated) Based On Including Extra-Ordinary Income',
    'Net Asset Value Per Share','Restated Net Asset Value Per Share',
    'Net Profit After Tax Continuous operations (mn)',
    'Net Profit After Tax Including Extra-Ordinary Income (mn)',
    '% Dividend','% Dividend Yield'
]

def get_finance_table(name, cols_text):
    contents = {}
    contents['Name'] = name
    for i, col_name in enumerate(columns[1:], start=0):
        try:
            contents[col_name] = cols_text[i]
        except IndexError:
            contents[col_name] = ""  
    return contents


def main():
    #all listed companies name and url
    driver = webdriver.Chrome()
    url = "https://www.cse.com.bd/company/listedcompanies"
    driver.get(url)

    listed_companies = []
    Listed_companies = driver.find_element(By.CLASS_NAME, 'com_inner_body')

    for alphabet in string.ascii_uppercase:
        rows = Listed_companies.find_elements(By.ID, f'{alphabet}')
        if not rows:
            continue
        li_tags = rows[0].find_elements(By.TAG_NAME, "li")
        for li in li_tags:
            a_tag = li.find_element(By.TAG_NAME, "a")
            name = a_tag.text.strip()
            link = a_tag.get_attribute('href')
            print(f"Name: {name}, URL: {link}")
            listed_companies.append([name, link])

    # Finance table extraction
    fin_table_data = []
    for name, link in listed_companies:
        driver.get(link)
        print(f"Processing {name} | {link}")
        

        try:
            finance_table = driver.find_element(By.ID, 'print-block')
            tables = finance_table.find_elements(By.TAG_NAME, "table")

            target_table = None
            for table in tables:
                trs = table.find_elements(By.TAG_NAME, "tr")
                if trs:
                    first_tr_text = trs[0].text.strip()
                    if "Financial Performance" in first_tr_text:
                        target_table = table
                        break

            if target_table:
                trs = target_table.find_elements(By.TAG_NAME, "tr")
                data_rows = trs[3:]
                for row in data_rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    cols_text = [col.text.strip() for col in cols]
                    if cols_text:  
                        fin_table_data.append(get_finance_table(name, cols_text))

        except Exception as e:
            print(f"Error processing {name}: {e}")

    driver.close()
    df = pd.DataFrame(fin_table_data, columns=columns)
    df.to_csv("NAV_EPS.csv", index=False)
    print("Data saved to NAV_EPS.csv")


if __name__ == "__main__":
    main()
