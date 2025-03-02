import csv
from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome()

for year in range(2024, 2015, -1):
    url = f"https://www.gotopku.cn/programa/admitline/7/{year}.html"
    print(f"正在爬取 {year} 年的数据...")
    driver.get(url)

    html = driver.page_source
    tree = etree.HTML(html)
    rows = tree.xpath('/html/body/div[5]/div[2]/table/tbody/tr')

    with open('pku.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        

        if year < 2024: 
            writer.writerow([])
        writer.writerow([f"{year}年的录取情况"])
        
        for row in rows:
            cols = row.xpath('./td/text()')
            if cols:
                writer.writerow(cols)

driver.quit()
print("所有数据已成功保存到 'pku.csv'")