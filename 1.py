import random
import time

class MemoryManager:
    def __init__(self):
        self.array = []
        self.size = 0
        self.statistics = []

    def array(self):
        while True:
            try:
                size = int(input("Введите размер массива: "))
                if size <= 0:
                    print("Размер должен быть положительным числом.")
                    continue
                self.size = size
                self.array = [random.randint(0, 100) for _ in range(size)]
                break
            except ValueError:
                print("Ошибка: введите корректное целое число.")

    def insertion_sort(self):
        arr = self.array.copy()
        stats = self._init_stats()
        start = time.time()
        print("Исходный массив:", arr)
        for i in range(1, len(arr)):
            stats['iterations'] += 1
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                stats['comparisons'] += 1
                arr[j + 1] = arr[j]
                stats['swaps'] += 1
                j -= 1
            if j >= 0:
                stats['comparisons'] += 1
            arr[j + 1] = key

        stats['time'] = time.time() - start
        self.statistics.append(("Сортировка вставками", stats))
        return arr

    def selection_sort(self):
        arr = self.array.copy()
        stats = self._init_stats()
        start = time.time()

        for i in range(len(arr)):
            stats['iterations'] += 1
            min_index = i
            for j in range(i + 1, len(arr)):
                stats['comparisons'] += 1
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                stats['swaps'] += 1

        stats['time'] = time.time() - start
        self.statistics.append(("Сортировка выборкой", stats))
        return arr

    def bubble_sort(self):
        arr = self.array.copy()
        stats = self._init_stats()
        start = time.time()

        for i in range(len(arr)):
            stats['iterations'] += 1
            swapped = False
            for j in range(len(arr) - i - 1):
                stats['comparisons'] += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    stats['swaps'] += 1
                    swapped = True
            if not swapped:
                break

        stats['time'] = time.time() - start
        self.statistics.append(("Сортировка пузырьком", stats))
        return arr

    def quick_sort(self, arr=None, stats=None):
        if arr is None:
            arr = self.array.copy()
            stats = self._init_stats()
            start = time.time()
            self._quick_sort_recursive(arr, 0, len(arr) - 1, stats)
            stats['time'] = time.time() - start
            self.statistics.append(("Быстрая сортировка", stats))
            return arr
        else:
            self._quick_sort_recursive(arr, 0, len(arr) - 1, stats)
    def _quick_sort_recursive(self, arr, low, high, stats):
        if low < high:
            stats['iterations'] += 1
            pivot_index = self._partition(arr, low, high, stats)
            self._quick_sort_recursive(arr, low, pivot_index - 1, stats)
            self._quick_sort_recursive(arr, pivot_index + 1, high, stats)

    def _partition(self, arr, low, high, stats):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            stats['comparisons'] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                stats['swaps'] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats['swaps'] += 1
        return i + 1

    def _init_stats(self):
        return {
            'iterations': 0,
            'comparisons': 0,
            'swaps': 0,
            'time': 0
        }

    def print_statistics(self):
        print("\nСтатистика сортировок:")
        print("{:<30} {:<12} {:<12} {:<12} {:<12}".format("Метод", "Итерации", "Сравнения", "Обмены", "Время (с)"))
        for name, stats in self.statistics:
            print("{:<30} {:<12} {:<12} {:<12} {:.6f}".format(
                name, stats['iterations'], stats['comparisons'], stats['swaps'], stats['time']
            ))

    def compare_sizes(self):
        sizes = [20, 500, 1000, 3000, 5000, 10000]
        for size in sizes:
            self.size = size
            self.array = [random.randint(0, 100) for _ in range(size)]
            self.statistics = []

            print(f"\nРазмер массива: {size}")
            print("-" * 30)

            self.insertion_sort()
            self.selection_sort()
            self.bubble_sort()
            self.quick_sort()

            self.print_statistics()

    def compare_ordering(self):
        try:
            size = int(input("Введите размер массива: "))
        except ValueError:

            print("Ошибка: введите целое число.")
            return


        self.array = list(range(size))
        self._run_all_sorts("Полностью отсортированный")


        self.array = list(range(size, 0, -1))
        self._run_all_sorts("Обратно отсортированный")


        massa = [random.randint(0, 100) for _ in range(size)]

        for percent in [25, 50, 75]:
            part = int(size * percent / 100)

            tipo_copy = massa.copy()

            sorted_section = sorted(tipo_copy[:part])
            remaining_section = tipo_copy[part:]

            self.array = sorted_section + remaining_section
            self._run_all_sorts(f"Частично отсортированный ({percent}%)")

    def _run_all_sorts(self, description):
        print(f"\n{description}:")
        self.statistics = []

        self.insertion_sort()
        self.selection_sort()
        self.bubble_sort()
        self.quick_sort()

        self.print_statistics()

    def _digits_product(self, number):
        product = 1
        for digit in str(abs(number)):
            product *= int(digit)
        return product

    def zadanie(self):
        try:
            size = int(input("Введите количество элементов: "))
            if size <= 0:
                print("Размер должен быть больше нуля.")
                return
        except ValueError:
            print("Ошибка: введите целое число.")
            return

        self.array = [random.randint(10, 99) for _ in range(size)]
        print("Исходный массив:", self.array)

        arr = self.array.copy()
        stats = self._init_stats()
        start = time.time()

        for i in range(len(arr)):
            stats['iterations'] += 1
            min_index = i
            for j in range(i + 1, len(arr)):
                stats['comparisons'] += 1
                if self._digits_product(arr[j]) < self._digits_product(arr[min_index]):
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                stats['swaps'] += 1

        stats['time'] = time.time() - start
        self.statistics = [("Сортировка по произведению цифр", stats)]

        print("Отсортированный массив:", arr)
        self.print_statistics()

    def main(self):
        while True:
            print("\nМеню:")
            print("1. Сравнение по размерам")
            print("2. Сравнение по упорядоченности")
            print("3. Задание. Сортировка по произведению цифр")
            print("0. Выход")

            choice = input("Выберите пункт меню: ").strip()

            if choice == '1':
                self.compare_sizes()

            elif choice == '2':
                self.compare_ordering()

            elif choice == '3':
                self.zadanie()

            elif choice == '0':
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    manager = MemoryManager()
    manager.main()