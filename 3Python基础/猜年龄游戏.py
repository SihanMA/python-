age = 18
count = 0
prize_dict = {0:'布娃娃',1:'变形金刚',2:'奥特曼',3:'<python从入门到放弃>'}

while count < 3:
    inp_age = input('输入年龄：')

    if not inp_age.isdigit():
        print('输入错误')
        continue
    
    inp_age = int(inp_age)

    if inp_age == age:
        print('猜对了')
        
        print(prize_dict)

        for i in range(2):
            prize_choice = input('输入你要的奖品，不要则输入”n“退出！')

            if prize_choice != 'n':
                print(f'恭喜你获得{prize_dict[int(prize_choice)]}')
            else:
                break
        break
    elif inp_age < age:
        print('小了')
    else:
        print('大了')
    
    count += 1

    if count != 3:
        continue

    again_choice = input('是否继续游戏，继续输入”Y“，否则任意角退出')

    if(again_choice == 'Y'):
        count = 0
        