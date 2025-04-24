import random
import time
import matplotlib.pyplot as plt


class MemoryManager:
    def __init__(self):
        self.array = []
        self.size = 0
        self.statistics = [] 
    
    def generate_array(self,size):
        array = [random.randint(0, 1000) for _ in range(size)]
        return array

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

    def linear_search(self, arr, target):
        comparisons = 0
        for i, val in enumerate(arr):
            comparisons += 1
            if val == target:
                return i, comparisons
        return -1, comparisons

    def linear_search_with_barrier(self, arr, target):
        comparisons = 0
        arr.append(target)
        i = 0
        while arr[i] != target:
            comparisons += 1
            i += 1 
        comparisons += 1
        arr.pop()
        if i == len(arr):
            return -1, comparisons
        return i, comparisons

    def binary_search(self, arr, target):
        comparisons = 0
        left, right = 0, len(arr) - 1
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid, comparisons
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1, comparisons

    def search_linear_demo(self):
        sizes = [20, 500, 1000, 3000, 5000, 10000]
        times = []
        comparisons_list = []
        try:
            target = int(input("Введите элемент для поиска: "))
        except ValueError:
            print("Ошибка: введите целое число.")
            return

        print("{:<10} {:<20} {:<20}".format("Размер", "Время (сек)", "Сравнения"))
        for size in sizes:
            arr = self.generate_array(size)
            start = time.time()
            _, comparisons = self.linear_search(arr.copy(), target)
            duration = time.time() - start

            times.append(duration)
            comparisons_list.append(comparisons)

            print("{:<10} {:<20.6f} {:<20}".format(size, duration, comparisons))

        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(sizes, times, marker='o')
        plt.title('Время линейного поиска от размера массива')
        plt.xlabel('Размер массива')
        plt.ylabel('Время (сек)')

        plt.subplot(1, 2, 2)
        plt.plot(sizes, comparisons_list, marker='s', color='orange')
        plt.title('Сравнения при линейном поиске')
        plt.xlabel('Размер массива')
        plt.ylabel('Количество сравнений')

        plt.tight_layout()
        plt.show()

    def search_with_barrier(self):

        sizes = [20, 500, 1000, 3000, 5000, 10000]
        comp_normal_list = []
        comp_barrier_list = []
        time_normal_list = []
        time_barrier_list = []

        try:
            target = int(input("Введите элемент для поиска: "))
        except ValueError:
            print("Ошибка: введите целое число.")
            return

        print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(
            "Размер", "Вр. обычный (сек)", "Сравн. обычный",
            "Вр. с барьером (сек)", "Сравн. с барьером"
        ))

        for size in sizes:
            arr = [random.randint(0, 22) for _ in range(size)]

            start = time.perf_counter()
            _, comp_normal = self.linear_search(arr.copy(), target)
            duration_normal = time.perf_counter() - start

            start = time.perf_counter()
            _, comp_barrier = self.linear_search_with_barrier(arr.copy(), target)
            duration_barrier = time.perf_counter() - start

            comp_normal_list.append(comp_normal)
            comp_barrier_list.append(comp_barrier)
            time_normal_list.append(duration_normal)
            time_barrier_list.append(duration_barrier)

            print("{:<10} {:<20.6f} {:<20} {:<20.6f} {:<20}".format(
                size, duration_normal, comp_normal, duration_barrier, comp_barrier
            ))

        plt.figure(figsize=(10, 5))
        plt.plot(sizes, time_normal_list, marker='o', label='Время обычный поиск')
        plt.plot(sizes, time_barrier_list, marker='s', label='Время поиск с барьером')
        plt.title('Время работы поиска с барьером и без')
        plt.xlabel('Размер массива')
        plt.ylabel('Время (сек)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10, 5))
        plt.plot(sizes, comp_normal_list, marker='o', label='обычный поиск')
        plt.plot(sizes, comp_barrier_list, marker='s', label='поиск с барьером')
        plt.title('Сравнение количества сравнений')
        plt.xlabel('Размер массива')
        plt.ylabel('Количество сравнений')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    def search_srav(self):
        try:
            size = int(input("Введите размер массива: "))
            target = int(input("Введите элемент для поиска: "))
        except ValueError:
            print("Ошибка: введите целое число.")
            return

        results = []

        def test_search(title, arr, target):
            start = time.time()
            _, comp1 = self.linear_search(arr.copy(), target)
            t1 = time.time() - start

            start = time.time()
            _, comp2 = self.binary_search(sorted(arr.copy()), target)
            t2 = time.time() - start

            results.append((title, t1, comp1, t2, comp2))

            print(f"\n{title}:")
            print("{:<30} {:<15} {:<15}".format("Метод", "Время (сек)", "Сравнения"))
            print("{:<30} {:<15.6f} {:<15}".format("Линейный поиск", t1, comp1))
            print("{:<30} {:<15.6f} {:<15}".format("Бинарный поиск", t2, comp2))

        base_array = [random.randint(0, 1000) for _ in range(size)]

        arr_sorted = sorted(base_array)
        test_search("Полностью отсортированный", arr_sorted, target)

        arr_reverse = sorted(base_array, reverse=True)
        test_search("Обратно отсортированный", arr_reverse, target)

        for percent in [25, 50, 75]:
            part = int(size * percent / 100)
            arr_partial = base_array.copy()
            arr_partial[:part] = sorted(arr_partial[:part])  
            test_search(f"Частично отсортированный {percent}%", arr_partial, target)

        labels = [r[0] for r in results]
        lin_comparisons = [r[2] for r in results]
        bin_comparisons = [r[4] for r in results]

        x = range(len(labels))

        plt.figure(figsize=(10, 5))
        plt.bar(x, lin_comparisons, width=0.4, label='Линейный поиск', align='center')
        plt.bar([i + 0.4 for i in x], bin_comparisons, width=0.4, label='Бинарный поиск', align='center')
        plt.xticks([i + 0.2 for i in x], labels, rotation=25)
        plt.ylabel('Количество сравнений')
        plt.title('Сравнение линейного и бинарного поиска на разных массивах')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    def main(self):
        while True:
            print("\nМеню:")
            print("1. Сравнение линейного поиска")
            print("2. Сравнение линейного и бинарного поиска")
            print("3. Эффективность линейного поиска с барьером")
            print("0. Выход")

            choice = input("Выберите пункт меню: ").strip()

            if choice == '1':
                self.search_linear_demo()
            elif choice == '2':
                self.search_srav()
            elif choice == '3':
                self.search_with_barrier()
            elif choice == '0':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    manager = MemoryManager()
    manager.main()