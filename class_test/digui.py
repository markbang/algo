# 递归

from typing import List

def sum_list(li: list[int | float]):
    sum_num = 0
    for i in li:
        sum_num += i
    return sum_num

def sum_list1(li: List[int | float]):
    if len(li) == 1:
        return li[0]
    return li[0] + sum_list1(li[1:])

def jiecheng(n):
    if n == 0 or n == 1:
        return 1
    return n * jiecheng(n - 1)
    
def convert_string(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return convert_string(n // base, base) + convert_string(n % base, base)
    
def binary_search(data, target, low, high):
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

if __name__ == '__main__':
    print(sum_list([1, 2.2, 3, 4, 5]))  # 15.2
    print(sum_list1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55
    print(jiecheng(5))
    print(convert_string(10, 2))  # 1010
    print(convert_string(8888888, 16))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 0, 9))  # True