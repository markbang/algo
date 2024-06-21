def bubble_sort(a_list):
    lenth = len(a_list)
    for i in range(lenth-1):
        if len(a_list) == 1:
            return a_list
        for j in range(lenth-1-i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

if __name__=="__main__":
    a_list = [3, 2, 1, 4, 5, 6, 7, 8, 12, 10]
    print(bubble_sort(a_list))