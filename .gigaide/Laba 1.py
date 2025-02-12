def printset(name, s):
    print(f"Множество {name}: {s}, количество элементов: {len(s)}")

def input_sequence(prompt):
    while True:
        sequence = input(prompt)
        if not sequence:
            print("Ошибка: последовательность не может быть пустой. Попробуйте снова.")
            continue
        return sequence


def task1():
    sequence = input_sequence("Введите последовательность чисел, букв и символов через пробел: ")
    elements = sequence.split()
    comparison_symbols = {'<', '>', '=', '!=', '<=', '>='}
    result_set = {element for element in elements if element in comparison_symbols}
    printset("результат", result_set)

def task2():
    A = input_set("Введите элементы множества A через пробел: ")
    B = input_set("Введите элементы множества B через пробел: ")
    C = input_set("Введите элементы множества C через пробел: ")

    # Проверка условий
    if not B.issubset(A):
            print("Ошибка: B не является подмножеством A.")
            return
    if not A.isdisjoint(C):
            print("Ошибка: A и C не являются непересекающимися множествами.")
            return

    # Вычисление множества X
    X = (A - B).union(C)
    printset("X", X)

def input_set(prompt):
    while True:
        elements = input(prompt).split()
        if elements:
            return set(elements)
        print("Ошибка: множество не может быть пустым. Попробуйте снова.")

def main():
    print("Задание 1")
    task1()
    print("Задание 2")
    task2()
if __name__ == "__main__":
    main()