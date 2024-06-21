def max_min_in_s(s, n):
    if len(s) == 0:
        return None
    if n ==0:
        return s[0], s[0]
    s_max, s_min = max_min_in_s(s, n-1)
    if s_max < s[n]:
        s_max = s[n]
    if s_min > s[n]:
        s_min = s[n]
    return s_max, s_min


s = [1, 3, 4, 55, 6, 7, 8, 3, 10]
print(max_min_in_s(s, len(s)-1))