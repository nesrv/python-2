# # Модуль 3. Алгоритмы
# ## Алгоритмы сортировки

# ### Сортировка пузырьком

# def bubble_sort(lst):
    
    # for cnt in range(len(lst)-1, 0, -1):
        
        # for i in range(cnt):
            
            # if lst[i] > lst[i+1]:
                
                # lst[i], lst[i+1] = lst[i+1], lst[i]


# ### Сортировка вставками 


# def insertion_sort(lst):
    
    # for i in range(1, len(lst)):
        
        # current = lst[i]
        # pos = i

        # while pos>0 and lst[pos-1]>current:
            
            # lst[pos] = lst[pos-1]
            # pos = pos-1

        # lst[pos] = current


# ### Сортировка слиянием

# def merge_sort(lst):
    
    # if len(lst) > 1:
        # mid = len(lst) // 2
        # left = lst[:mid]
        # right = lst[mid:]
        
        # mergeSort(left)
        # mergeSort(right)
        
        # i = 0
        # j = 0
        # k = 0
        
        # while i<len(left) and j<len(right):
            # if left[i] < right[j]:
                # lst[k] = left[i]
                # i += 1
            # else:
                # lst[k] = right[j]
                # j += 1
            # k += 1

        # while i < len(left):
            # lst[k] = left[i]
            # i += 1
            # k += 1

        # while j < len(right):
            # lst[k] = right[j]
            # j += 1
            # k += 1

