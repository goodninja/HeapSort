# Реализация пирамидальной сортировки на Python

# Преобразование в двоичную кучу с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1   
    r = 2 * i + 2  

  # Проверка, существует ли левый дочерний элемент, больший чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент, больший чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r


    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  

        
        heapify(arr, n, largest)



def heapSort(arr):
    n = len(arr)


    for i in range(n, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)


# Код для тестирования
arr = [13, 10, 12, 8, 4, 9]
heapSort(arr)
n = len(arr)
print("Отсортированный массив")
for i in range(n):
    print("%d" % arr[i])
