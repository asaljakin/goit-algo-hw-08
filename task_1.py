import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів у мінімальну купу
    heapq.heapify(cables)
    total_cost = 0

    # Продовжуємо об'єднувати кабелі, доки в купі більше одного кабеля
    while len(cables) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на їхнє з'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

cables = list(map(int, input("Введіть довжини кабелів через пробіл: ").split()))
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))