from time import sleep

def get_username_from_email():
    attempt = 1

    while True:
        if attempt > 3:
            print("Подождите 10 секунд")
            sleep(10)

        email = input(f"[Попытка {attempt}] Введите свою электронную почту :\t").lower()

        if email.count("@") == 1:
            if email.split("@")[1].count(".") == 1:
                break

        print("Это не является электронной почтой. Попробуйте еще раз.")
        attempt += 1

    print(f"Вы ввошли как {email.split('@')[0]}")

    with open("email-data.txt", "r", encoding="UTF-8") as file:
        info = []
        for i in file:
            info.append(i.strip())

    if email not in info:
        info.append(email)

    with open("email-data.txt", "w", encoding="UTF-8") as file:
        for i in info:
            file.write(i+"\n")

    return email.split("@")[0]

a = get_username_from_email()
print(f"--- {a} ---")