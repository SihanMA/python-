```python
while True:
    user_db = 'nick'
    pwd = '123'
    
    inp_user = input('username:')
    inp_pwd = input('password:')
    
    if inp_user == user_db and pwd_db == inp_pwd:
        print('login successful')
      	
        while True:
            cmd = input('输入命令')
            if cmd == 'q':
                break
            print(f'{cmd}功能执行')
        break
    else:
        print('username or password error')

print('退出循环')
```

```python
# tag控制循环退出
tag = True
while tag:
    user_db = 'nick'
    pwd_db = '123'

    inp_user = input('username: ')
    inp_pwd = input('password: ')

    if inp_user == user_db and pwd_db == inp_pwd:
        print('login successful')

        while tag:
            cmd = input('请输入你需要的命令：')
            if cmd == 'q':
                tag = False
            print(f'{cmd} 功能执行')
    else:
        print('username or password error')

print('退出了while循环')
```

