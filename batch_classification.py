import os
import shutil
import logging
from datetime import datetime
from functools import wraps

#定义文件分类字典常量
FILE_CATEGORIES = {
    "图片": ["jpg", "jpeg", "png", "gif", "bmp"],
    "文档": ["txt", "doc", "docx", "pdf", "xlsx"],
    "其他": []
}

# 初始化日志配置（只需在程序启动时调用一次）
def init_logger():
    logging.basicConfig(
        filename='C:\\Users\\75219\\Desktop\\学习\\file_classify.log',  # 📁 指定日志文件名或者对应路径
        format='[%(asctime)s] %(message)s',  # ⏰ 含时间戳的格式
        level=logging.INFO  # 📊 设置信息记录最低级别，记录INFO及以上级别的日志
    )
# 记录分类操作的装饰器
def log_operation(operation_name="操作"):
    def decorator(func):
        @wraps(func)#保留原函数返回值
        def wrapper(*args, **kwargs):
            try:
                result=func(*args, **kwargs)  # 🚀 执行原始操作（如移动文件）
                # ✅ 成功日志
                logging.info(f"SUCCESS |  {operation_name} 操作成功")
                return result
            except Exception as e:
                # ❌ 失败日志（含错误信息）
                logging.error(f"FAILURE | {operation_name} 操作失败 | 错误类型：{type(e).__name__} | 详情：{str(e)}")
                return False
        return wrapper
    return decorator


#创建文件夹
@log_operation(operation_name="创建文件夹")
def create_directories(path: str)-> None:
    try:
        for category, extensions in FILE_CATEGORIES.items():
            category_path = os.path.join(path, category)
            os.makedirs(category_path,exist_ok=True)#exist_ok=True避免文件夹存在时报错
            print(f"创建文件夹：{category_path}")
    except Exception as e:
        print(f"创建文件夹失败：{e}")
        raise#不在这里丢出报错的话日志记录不到
    
#文件分类判断模块
@log_operation(operation_name="文件分类判断")
def file_category(file_name:str)->str:
    file_extension = os.path.splitext(file_name)[1].lstrip(".").lower()#获取文件扩展名(.jpg)，去掉前缀，并转化为小写
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "其他"


#移动文件
@log_operation(operation_name="移动文件")
def move_file(start_path:str,end_path:str)->None:
    try:
        with os.scandir(start_path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"文件: {entry.name}")
                    shutil.move(entry.path, os.path.join(end_path,file_category(entry.name)))
                elif entry.is_dir():
                    print(f"目录: {entry.path}")
                    move_file(entry.path,end_path)  # 递归调用
    except Exception as e:
        print(f"移动文件失败：{e}")
        raise#不在这里丢出报错的话日志记录不到               


start_path=input("请输入要分类的文件夹路径：")
end_path=input("请输入目标文件夹路径：")
if os.path.exists(start_path) and os.path.exists(end_path):
    init_logger()
    create_directories(end_path)
    move_file(start_path,end_path)
else:
    print("路径不存在！")

