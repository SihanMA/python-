username_list = []
prize_dict = {
    '0': "芭比娃娃",
    '1': "变形金刚",
    '2': "psp游戏机",
    '3': "奥特曼",
    '4': "遥控飞机",
    '5': "chongqiwawa",
}

shopping_car_dict = {}

def inp_username_pwd():
    username_inp = input('请输入你的用户名：')
    pwd_inp = input('请输入你的密码：')

    return username_inp, pwd_inp

def login():
    print('欢迎来到登录功能')
    if username_list:
        print('已经登录，请勿重复登录')
        return

    count = 0
    while count < 3:
        username_inp, pwd_inp = inp_username_pwd()
        with open('user_info.txt', 'r', encoding='utf8') as fr:
            for user_info in fr:
                user_info = user_info.strip()
                username, pwd = user_info.split(':')

                if username == username_inp and pwd == pwd_inp:
                    print('登录成功')
                    username_list.append(username_inp)
                    return

            else:
                print('账号密码错误')

            count += 1

def register():
    print('欢迎来到注册功能')

    username_inp, pwd_inp = inp_username_pwd()

    with open('user_info.txt', 'a', encoding='utf8') as fa:
        fa.write(f'{username_inp}:{pwd_inp}\n')

def logout():
    print('欢迎来到注销功能')

    if not username_list:
        print('请登录后使用该功能')
        return

    username_list.clear()

def shopping():
    print('欢迎来到Nick集团消费功能')

    if not username_list:
        print('请登录后使用该功能')
        return

    print('''
            0 芭比娃娃
            1 变形金刚
            2 psp游戏机
            3 奥特曼
            4 遥控飞机
            5 chongqiwawa
            ''')
    prize_choice = input('输入要购买的商品编号：')
    prize_name = prize_dict[prize_choice]

    if prize_name in shopping_car_dict:
        shopping_car_dict[prize_name] += 1
    else:
        shopping_car_dict[prize_name] = 1

    print(f'消费成功{prize_name}，当前购物车情况为{shopping_car_dict}')

def shopping_car():
    print('恭喜剁手成功功能')

    if not username_list:
        print('请登录后使用该功能')
        return

    print(f'恭喜你购物成功：{shopping_car_dict}')

    shopping_car_dict.clear()

func_dict = {
    '1':login,
    '2':register,
    '3':logout,
    '4':shopping,
    '5':shopping_car,
}

while True:
    print('''
        1 登录
        2 注册
        3 注销
        4 购物
        5 购物车
        q 退出
        ''')
    func_choice = input('请选择你要选择的功能(输入q退出):')
    if func_choice == 'q':
        break
    if func_choice not in func_dict:
        print('傻逼，英文看不懂正常，还看不懂阿拉伯数字')
        continue

    func_dict[func_choice]()
