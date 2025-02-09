def add(a, b):  
    """加法运算"""  
    return a + b  

def subtract(a, b):  
    """减法运算"""  
    return a - b  

def multiply(a, b):  
    """乘法运算"""  
    return a * b  

def divide(a, b):  
    """除法运算（包含异常处理）"""  
    try:  
        return a / b  
    except ZeroDivisionError:  
        print("错误：除数不能为零！")  
        return None  #可以不写这句，但最好加上返回值确保调用者清楚地知道函数在不同情况下的行为。

# 主程序（结合之前的流程控制）  
while True:  
    print("简易计算器")  
    print("1. 加法  2. 减法  3. 乘法  4. 除法  0. 退出")  
    choice = input("请选择操作：")  

    if choice == '0':  
        break  

    num1 = float(input("输入第一个数字："))  
    num2 = float(input("输入第二个数字："))  

    # 通过字典映射替代复杂的if-elif链（优化流程控制）  
    operations = {  
        '1': add,  
        '2': subtract,  
        '3': multiply,  
        '4': divide  
    }  

    func = operations.get(choice, lambda: print("无效选择"))  
    result = func(num1, num2)  

    if result is not None:  
        print(f"结果：{result:.2f}")
