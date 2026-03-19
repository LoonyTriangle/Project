import pyperclip
import random

digits = "0123456789"
min_b = "abcdefghijklmnopqrstuvwxyz"
big_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()"

while True:
    try:
        length = int(input("Введите длину пароля (6-50): "))
        if 5 <= length <= 85:
            break
        else:
            print("Длина должна быть от 6 до 50")
    except ValueError:
        print("Тут только цифры пожалуйста!")

while True:
    use_digits = input("Добавить цифры? (да/нет): ").strip().lower()
    if use_digits in ("да", "нет"):
        use_digits = use_digits == "да"
        break
    print("Ошибка: введите «да» или «нет»")

while True:
    use_low = input("Добавить строчные буквы? (да/нет): ").strip().lower()
    if use_low in ("да", "нет"):
        use_low = use_low == "да"
        break
    print("Ошибка: введите «да» или «нет»")

while True:
    use_up = input("Добавить прописные буквы? (да/нет): ").strip().lower()
    if use_up in ("да", "нет"):
        use_up = use_up == "да"
        break
    print("Ошибка: введите «да» или «нет»")

while True:
    use_special = input("Добавить спецсимволы? (да/нет): ").strip().lower()
    if use_special in ("да", "нет"):
        use_special = use_special == "да"
        break
    print("Ошибка: введите «да» или «нет»")

alp = ""
groups = []

if use_digits:
    alp += digits
    groups.append(digits)

if use_low:
    alp += min_b
    groups.append(min_b)

if use_up:
    alp += big_b
    groups.append(big_b)

if use_special:
    alp += special
    groups.append(special)

if alp == "":
    print("Вы не выбрали ни одного типа символов.")
    exit()

while True:
    try:
        count = int(input("Сколько паролей создать?: "))
        if count > 0:
            break
        print("Ошибка...")
    except:
        print("Только цифры!")

for i in range(count):
    password = []

    for group in groups:
        password.append(random.choice(group))

    while len(password) < length:
        password.append(random.choice(alp))

    random.shuffle(password)

    result = "".join(password)

    score = 0
    if use_digits:
        score += 1
    if use_low:
        score += 1
    if use_up:
        score += 1
    if use_special:
        score += 1
    if length >= 12:
        score += 1

    if score <= 2:
        level = "Слабый"
    elif score <= 4:
        level = "Хороший"
    else:
        level = "Отличный"

    print(str(i+1) + ". " + result + " — " + level)

    while True:
        choice = input(
            "Скопировать этот пароль в буфер? (да/нет): ").strip().lower()
        if choice in ("да", "нет", ""):
            if choice in ("да", ""):
                pyperclip.copy(result)
                print("   → скопировано!")
            break
        print("Введите «да» или «нет» (или просто Enter)")