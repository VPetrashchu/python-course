login_list=['First'] 

login = input("Please, enter login: ")

if login in login_list: 
    print('You entersd correct login', login)
else:
    print('You entersd incorrect login')