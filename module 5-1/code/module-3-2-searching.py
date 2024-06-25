# # Модуль 3. Алгоритмы
# ## Алгоритмы поиска

# ### Последовательный (линейный) поиск

# def linear_search(lst, key):
    # for idx, item in enumerate(lst):
        # if key == item:
            # return idx
    # return -1


# def ordered_linear_search(lst, key):
    # for idx, item in enumerate(lst):
        # if item == key:
            # return idx
        # elif item > key:
            # return -1
        # return -1


# ### Бинарный поиск

# def binary_search(lst, key):
    # first = 0
    # last = len(lst)-1
    
    # while first<=last:
        # mid = (first + last) // 2
        # if lst[mid] == key:
            # return mid
        # else:
            # if key < lst[mid]:
                # last = mid-1
            # else:
                # first = mid+1
    # return -1
