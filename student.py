#学生管理系统
students = {}
# 添加学生
def add_student(sid, name):
    students[sid] = {"name": name, "scores": {}}
# 添加成绩
def add_score(sid, subject, score):
    if sid in students:
        students[sid]["scores"][subject] = score
    else:
        print("学生不存在")
# 获取平均分
def get_average(sid):
    scores = students.get(sid, {}).get("scores", {})
    if not scores:
        return 0
    return round(sum(scores.values()) / len(scores), 2)
# 获取数学尖子生
def top_math_students():
    return [sid # 👈 最终收集的是学号（键）
            for sid, info in students.items() # 👈 解包键值对
            if info["scores"].get("数学", 0) > 90]# 👈 通过值判断条件

# 测试用例
add_student("S001", "张三")
add_score("S001", "数学", 95)
add_score("S001", "语文", 88)

add_student("S002", "李四")
add_score("S002", "数学", 87)
add_score("S002", "英语", 92)

print("张三平均分:", get_average("S001"))  # 输出 91.5
print("数学尖子生:", top_math_students())  # 输出 ['S001']