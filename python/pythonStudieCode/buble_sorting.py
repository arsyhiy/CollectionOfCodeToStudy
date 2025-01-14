def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False  # цикл делится на пермещение числа . если сортировка закончена используется функция False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = (
                    nums[i + 1],
                    nums[i],
                )
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


# Проверяем, что оно работает
random_list_of_nums = [
    5,
    2,
    1,
    8,
    4,
]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

# Алгоритм работает в цикле while и прерывается, когда элементы ни разу не меняются местами.
# Вначале присваиваем swapped значение True, чтобы алгоритм запустился хотя бы один раз.
