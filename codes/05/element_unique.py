def element_unique(s, n):
    if len(s) == 0:
        return None
    if n == 0:
        return True
    return s[n] not in s[0:n] and element_unique(s, n-1)


s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s2 = [1, 2, 3, 4, 5, 6, 7, 8, 8]
print('s1序列元素唯一', element_unique(s1, len(s1)-1))
print('s2序列元素唯一', element_unique(s2, len(s2)-1))