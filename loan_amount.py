import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Firefox()

df = pd.read_csv("C:\\Users\\PC\\Desktop\\PixelEdge\\Borrower name\\loan_amount.csv")

result_data = pd.DataFrame(columns=["SEC.gov URL", "Keyword and Amount"])

for index, row in df.iterrows():
    url = row["SEC.gov URL"]
    try:
        driver.get(url)
        sleep(5)
        
        page_text = driver.find_element(By.TAG_NAME, 'body').text
        first_400_words=' '.join(page_text.split()[:400])
        if "$" in first_400_words:
            pattern = r'(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'
            match=re.search(pattern,first_400_words)
            print(match)
        
        keyword = '“Aggregate Commitments”' 
        keyword_index = page_text.find(keyword)
        
       # if keyword_index != -1:
            # Find the line containing the keyword
        lines = page_text.split('\n')
        keyword_line = None
        for line in lines: 
            
            if '“Aggregate Commitments”' in line or 'Commitments of all the Lenders' in line or '“Commitments”' in line or '"Revolving Commitments"' in line:
                pattern = r'(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'
                match = re.search(pattern, line)
                if match:
                    print(match.group(0))
                    print(line)
                    print('.................')
                    break
            else:
                continue
        #else:
            #continue
    except Exception as e:
        print(f"Error processing URL {url}: {e}")

driver.quit()

# Save the results to a CSV file
result_data.to_csv("C:\\Users\\PC\\Desktop\\PixelEdge\\found_text_with_amount.csv", index=False)
