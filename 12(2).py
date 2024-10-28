import random

def random_num():
    first_num = random.randint(0,9)
    second_num = random.randint(0,9)
    third_num = random.randint(0,9)
    print(f"All numbers: {first_num}, {second_num}, {third_num}")
    return first_num + second_num + third_num

def shoot():
    N = int(input("Numbers of shoots: "))  # Запитуємо у користувача кількість пострілів
    total = 0

    for i in range(N):
        total += random_num()

    print(f"Sum of shooting is {total}")

shoot()