def sequnential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            return True
        else:
            pos += 1
            
    return found

def ordered_sequnential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            return True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found

def binary_search(data, target, low=0, high=None): # 递归 log(n)
    low = 0
    high = len(data) - 1
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

def binary_search_for(a_list, item): # 循环 log(n)
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        mid_point = (first + last) // 2
        if a_list[mid_point] == item:
            return True
        else:
            if item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return found

if __name__=="__main__":
    a_list = [1,2,3,4,5,6,7,8,9,10]
    print(sequnential_search(a_list, 5))
    print(sequnential_search(a_list, 11))
    print(ordered_sequnential_search(list(range(1,11)), 5))
    print(binary_search(list(range(1,11)), 5))