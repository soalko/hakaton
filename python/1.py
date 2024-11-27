
import math
import time


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] > arr[j - 1]:
                break
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start


def improved_insert_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        pos = binary_search(arr, val, 0, i)
        arr[pos + 1:i + 1] = arr[pos:i]
        arr[pos] = val
    return arr


if __name__ == '__main__':
    print("Для 100 чисел:")
    print()
    time_start = time.time()
    insert_sort([i for i in range(100, 0, -1)])
    print("Обычная сортировка вставками:   ", time.time() - time_start)

    time_start = time.time()
    improved_insert_sort([i for i in range(100, 0, -1)])
    print("Улучшенная сортировка вставками:", time.time() - time_start)
    print()
    print("Для 10 тыс чисел:")
    print()
    time_start = time.time()
    insert_sort([i for i in range(10000, 0, -1)])
    print("Обычная сортировка вставками:   ", time.time() - time_start)

    time_start = time.time()
    improved_insert_sort([i for i in range(10000, 0, -1)])
    print("Улучшенная сортировка вставками:", time.time() - time_start)
    print()
    print("Для 20 тыс чисел:")
    print()
    time_start = time.time()
    insert_sort([i for i in range(20000, 0, -1)])
    print("Обычная сортировка вставками:   ", time.time() - time_start)

    time_start = time.time()
    improved_insert_sort([i for i in range(20000, 0, -1)])
    print("Улучшенная сортировка вставками:", time.time() - time_start)

    print()
    print("Для 40 тыс чисел:")
    print()
    time_start = time.time()
    insert_sort([i for i in range(40000, 0, -1)])
    print("Обычная сортировка вставками:   ", time.time() - time_start)

    time_start = time.time()
    improved_insert_sort([i for i in range(40000, 0, -1)])
    print("Улучшенная сортировка вставками:", time.time() - time_start)




