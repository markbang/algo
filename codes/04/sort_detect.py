def sort_detect(s1, s2):
    # print('s1:', s1)
    # print('s2:', s2)
    # transform the str to the list
    s1_list = list(s1)
    s2_list = list(s2)
    # print('s1 list:', s1_list)
    # print('s2 list:', s2_list)
    # sort the two lists
    s1_list.sort()
    s2_list.sort()
    # print('sorted s1 list:', s1_list)
    # print('sorted s2 list:', s2_list)
    # if the sorted lists are equal, return True
    # else, return False
    if s1_list == s2_list:
        return True
    else:
        return False


if __name__ == "__main__":
    # s1, s2 = 'earth', 'heart'
    # s1, s2 = 'python', 'typhon'
    s1, s2 = "eearth", "hearrt"
    output = sort_detect(s1, s2)
    print("output:", output)
