# Задача 1: Метод середины квадратов Неймана
def neumann_method(n, r0, length):
    random_numbers = [r0]
    for _ in range(n):
        squared = str(int(r0 * (10 ** length)) ** 2).zfill(2 * length)  # Квадрат числа, дополненный до 2*length знаков
        middle_index = len(squared) // 2
        r0 = int(squared[middle_index - length//2: middle_index + length//2]) / (10 ** length)  # Берем средние цифры
        random_numbers.append(r0)
    return random_numbers


# Задача 2: Модифицированный метод Неймана
def modified_neumann_method(n, r0, r1, length):
    random_numbers = [r0,r1]
    for i in range(n):
        if i % 2 == 0:  # Если четный индекс, используем R0
            squared = str(int(r0 * (10 ** length)) ** 2).zfill(2 * length)
            middle_index = len(squared) // 2
            r0 = int(squared[middle_index - length//2: middle_index + length//2]) / (10 ** length)
            random_numbers.append(r0)
        else:  # Если нечетный индекс, используем R1
            squared = str(int(r1 * (10 ** length)) ** 2).zfill(2 * length)
            middle_index = len(squared) // 2
            r1 = int(squared[middle_index - length//2: middle_index + length//2]) / (10 ** length)
            random_numbers.append(r1)
    return random_numbers

# Задача 3: Алгоритм Лемера
def lemer_method(n, r0, g):
    random_numbers = []
    for _ in range(n):
        r0 = (g * r0) % 1  # Берем дробную часть от произведения
        random_numbers.append(r0)
    return random_numbers

# Задача 4: Мультипликативный конгруэнтный метод Лемера
def multiplicative_congruential_method(n, a, m, x0):
    random_numbers = []
    for _ in range(n):
        x0 = (a * x0) % m  # Вычисляем новое Xi
        random_numbers.append(x0/m)  # Делим на m чтобы получить базовую последовательность
    return random_numbers

# Пример использования всех методов
if __name__ == "__main__":
    # Задача 1
    print("Метод Неймана:", neumann_method(6, 0.583,4))

    # Задача 2
    print("Модифицированный метод Неймана:", modified_neumann_method(6, 0.5836, 0.2176,4))# Длина 4 знака

    # Задача 3
    print("Алгоритм Лемера:", lemer_method(5, 0.585, 927))

    # Задача 4
    print("Мультипликативный конгруэнтный метод:", multiplicative_congruential_method(6, 265, 129, 122))
