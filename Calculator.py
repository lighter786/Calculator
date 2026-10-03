a, b = map(int, input("Введи два числа в строку: ").split())
operation = input("Что вы хотите сделать с числами? ")

history_oprtations = []

while a > 0 and b > 0:
    if operation == '+':
        ans = a + b
    elif operation == '-':
        ans = a - b
    elif operation == '/':
        ans = a / b
    elif operation == '//':
        ans = a // b
    elif operation == '%':
        ans = a % b
    elif operation == '*':
        ans = a * b
    elif operation == '**':
        ans = a ** b
    else:
        print("Неизвестная операция")
        ans = None

    if ans is not None:
        print(f"{a}{operation}{b} = {ans}")
        history_oprtations.append(ans)

    word = input()
    if word == "stop":
        break

    a, b = map(int, input("Введи два числа в строку: ").split())
    operation = input("Введите операцию: ")

print("\nИстория операций:")
for idx, value in enumerate(history_oprtations, start= 1):
    print(f"{idx}) {value}")

