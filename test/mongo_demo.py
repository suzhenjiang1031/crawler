from pymongo import MongoClient
from pprint import pprint

# 连接 MongoDB 数据库
def connect_mongo():
    client = MongoClient("mongodb://localhost:27017/")  # 默认本地MongoDB
    db = client["gaokao_db"]  # 数据库名
    collection = db["schools"]  # 集合（类似MySQL表）
    return collection

# 插入高校信息
def insert_school(collection):
    school_data = {
        "school": "清华大学",
        "location": "北京",
        "type": "985",
        "double_first_class_subjects": ["计算机科学与技术", "电子信息工程", "建筑学"],
        "admission_scores": {
            "2023": 685,
            "2022": 680
        },
        "graduates": {
            "employment_rate": "98%",
            "popular_destinations": ["华为", "阿里巴巴", "字节跳动"]
        }
    }
    result = collection.insert_one(school_data)
    print(f"插入成功，id: {result.inserted_id}")

# 查询高校信息
def query_schools(collection):
    print("\n查询北京地区高校：")
    results = collection.find({"location": "北京"})
    for school in results:
        pprint(school)

    print("\n查询2023年录取分数高于680分的高校：")
    results = collection.find({"admission_scores.2023": {"$gt": 680}})
    for school in results:
        pprint(school)

# 更新高校信息
def update_admission_score(collection):
    print("\n更新清华大学2024年录取分数线...")
    result = collection.update_one(
        {"school": "清华大学"},
        {"$set": {"admission_scores.2024": 690}}
    )
    if result.modified_count:
        print("更新成功！")
    else:
        print("未找到匹配记录，未修改！")

# 删除高校信息
def delete_school(collection):
    print("\n删除浙江大学的信息...")
    result = collection.delete_one({"school": "浙江大学"})
    if result.deleted_count:
        print("删除成功！")
    else:
        print("未找到匹配记录！")

# 主流程
def main():
    collection = connect_mongo()

    # 插入高校信息
    insert_school(collection)

    # 查询高校信息
    query_schools(collection)

    # 更新高校录取分数线
    update_admission_score(collection)

    # 再次查询看更新结果
    query_schools(collection)

    # 删除高校信息
    delete_school(collection)

if __name__ == "__main__":
    main()
