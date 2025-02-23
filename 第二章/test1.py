import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('signup_count.csv')

# 筛选报名数小于等于 5 的行
filtered_df = df[df['报名数'] <= 5]

print(filtered_df)

# 将筛选后的数据保存到新的 CSV 文件：
filtered_df.to_csv('filtered_signup_count.csv', index=False, encoding='utf-8')

print(filtered_df.describe())  # 打印数据的基本统计信息