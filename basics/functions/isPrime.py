def isPrime(num):
    if num > 1:
        for i in range(2, num+1):
            if num == 2:
                return True
            else:
                if num % i == 0:
                    break
                else:
                    if i == num-1:
                        return True
                    continue
        return False
    else:
        print("Error, ingresa un valor válido")


for i in range(1, 100):
    if isPrime(i + 1):
        print(i + 1, end=", ")
print()
