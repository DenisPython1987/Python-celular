from time import sleep

saudação = "FizzBuzz"
print("\033[35m")
print("-*-" * 20)
print(f"{saudação:^66}")
print("-*-" * 20)
print("\033[m")

n = int(input("\033[32mDigite um ponto de parada: \033[m"))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("\033[36mFizzBuzz\033[m")
        sleep(1)
    elif i % 3 == 0:
        print("\033[33mFizz\033[m")
        sleep(1)
    elif i % 5 == 0:
        print("\033[33mBuzz\033[m")
        sleep(1)
    else:
        print(f"\033[31m{i}\033[m")
        sleep(1)