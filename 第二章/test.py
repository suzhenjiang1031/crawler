import csv
from selenium import webdriver
from lxml import etree

# 启动浏览器并加载页面
driver = webdriver.Chrome()

# 目标URL
url = "https://gwykl.fujian.gov.cn/kl2024/signupcount"
driver.get(url)

# 获取页面的完整源代码
html = driver.page_source

# 解析HTML
tree = etree.HTML(html)         

# 使用XPath提取表格数据
rows = tree.xpath('//*[@id="datalist"]/table/tbody/tr')  # 获取每一行

# 打开CSV文件并写入数据
with open('signup_count.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 写入CSV文件的头部
    writer.writerow(['单位', '职位', '考试类型', '招考数', '报名数', '审核通过', '未审核'])
    
    # 遍历每一行并提取每一列的数据
    for row in rows:
        cols = row.xpath('.//td/text()')  # 获取每列的文本内容
        if cols:  # 确保列不为空
            writer.writerow(cols)  # 将数据写入CSV文件

# 关闭浏览器
driver.quit()

print("数据已成功保存到 'signup_count.csv'")