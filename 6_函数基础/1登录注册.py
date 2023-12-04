def register():
    username = input('username:').strip()
    pwd = input('password:').strip()

    with open('38a.txt','a',encoding='utf-8') as fa:
        fa.write(f'{username}:{pwd}\n')
        fa.flush()

def login():
    inp_username = input('username:').strip()
    inp_pwd = input('password:').strip()

    with open('38a.txt','rt',encoding='utf-8') as fr:
        for user_info in fr:
            user_info = user_info.strip('\n')
            user_info_list = user_info.split(':')
            if inp_username == user_info_list[0] and inp_pwd == user_info_list[1]:
                print('login successful')
                break
        else:
            print('failed')
login()