def anagram_solution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    return alist1 == alist2

    # while pos < len(s1) and matches:
    #     if alist1[pos] == alist2[pos]:
    #         pos = pos + 1
    #     else:
    #         matches = False

    # return matches


if __name__ == "__main__":
    # s1, s2 = 'heart', 'earth'
    s1, s2 = "heert", "earth"
    # s1, s2 = 'python', 'typhon'
    print(anagram_solution2(s1, s2))
