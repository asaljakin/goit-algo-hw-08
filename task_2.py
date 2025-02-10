import heapq

def merge_k_lists(lists):
    # Мінімальна купа для зберігання кортежів (значення, індекс списку, індекс елемента)
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:  # Якщо список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []

    # Продовжуємо витягувати найменший елемент з купи
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Якщо в поточному списку є наступний елемент, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))

    return merged_list

k = int(input("Введіть кількість списків: "))
lists = []
for i in range(k):
    lst = list(map(int, input(f"Введіть список {i+1} через пробіл: ").split()))
    lists.append(lst)
    
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)