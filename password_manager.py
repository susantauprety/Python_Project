master_pwd = input("What is your master password: ")

def view():
    with open ("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "password:", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open ("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("would you like to add new password or view exiting ones (view,add)? press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue