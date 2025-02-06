# 原始数据：包含学生的成绩列表
scores = [85, 92, 45, 67, 73, 58, 89, 95, 60, 81]

# 初始化统计变量：用于记录不同等级的成绩数量
grade_count = {
    "优秀": 0,   # 90-100 分
    "良好": 0,   # 80-89 分
    "中等": 0,   # 70-79 分
    "及格": 0,   # 60-69 分
    "不及格": 0  # <60 分
}
total = 0  # 用于累加所有成绩的总分

# 遍历处理每个成绩
for score in scores:
    # 累加总分
    total += score
    
    # 成绩分类：根据分数确定对应的等级
    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 70:
        grade = "中等"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    
    # 更新统计：增加对应等级的数量
    grade_count[grade] += 1

# 计算平均分：总分除以成绩数量
average = total / len(scores)

# 输出报告：打印成绩分析结果
print("\n=== 成绩分析报告 ===")
print(f"平均分：{average:.1f}")  # 格式化输出平均分，保留一位小数
print("等级分布：")
for grade, count in grade_count.items():
    print(f"{grade}: {count}人")  # 打印每个等级的人数



