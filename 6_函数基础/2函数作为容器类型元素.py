def pay():
    print('支付')

def withdraw():
    print('提现')

dic = {
    '1':pay,
    '2':withdraw
}

while True:
    msg = """
    '1':支付,
    '2':提现，
    '3':退出,
    """
    print(msg)
    choice = input('>>:').strip()
    if choice == '3':
        break
    elif choice in dic:
        dic[choice]()