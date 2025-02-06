# 设置最大尝试次数为 3 次
max_attempts = 3

# 定义正确的用户名和密码
correct_user = "admin"
correct_password = "123456"

# 初始化尝试次数为 0
attempts = 0

# 初始化登录状态为 False
logged_in = False

# 使用 while 循环进行登录验证，直到达到最大尝试次数或成功登录
while attempts < max_attempts and not logged_in:
    # 获取用户输入的用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    
    # 验证用户名和密码是否正确
    if username == correct_user and password == correct_password:
        # 如果验证成功，设置登录状态为 True
        logged_in = True
        print("登录成功！欢迎进入系统")
    else:
        # 如果验证失败，增加尝试次数
        attempts += 1
        # 计算剩余尝试次数
        remaining = max_attempts - attempts
        print(f"验证失败，剩余尝试次数：{remaining}")
        
    # 打印分隔线以美化输出ad
    print("-" * 30)

# 最终结果判断
if not logged_in:
    print("账户已锁定，请联系管理员")
