# 将每个操作封装为独立函数
def login():
    # 登录逻辑...
    print("登录成功")

def register():
    # 注册逻辑...
    print("注册成功")

# 建立操作映射表
action_handlers = {
    "login": login,#login指向了login函数
    "register": register,
}

def handle_user_action(action):
    handler = action_handlers.get(action, default_handler)
    handler()

def default_handler():
    print("未知操作")

handle_user_action("register")
