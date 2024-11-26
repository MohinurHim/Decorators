# Домашнее задание по теме "Декораторы":
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        is_prime = True
        if result > 1:
            for i in range(2, result): # проверки на простоту числа, выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно).
                if result % i == 0:
                    is_prime = False
            if is_prime == True:
                print("Простое")
            else:
                print("Составное")
        return result
    return wrapper
@is_prime
def sum_three(*numbers):
    return sum(numbers)
result = sum_three(2, 3, 6)
print(result)
