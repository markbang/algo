import timeit

words = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
)


def solution(st1, st2):  # O(n*log(n))
    if len(st1) == len(st2):
        for i in range(len(st1)):
            if st1[i] not in words or st2[i] not in words:
                return False
        li1 = list(st1).sort()
        li2 = list(st2).sort()
        return li1 == li2
    else:
        return False


def solution2(st1, st2):  # O(n^2)
    if len(st1) == len(st2):
        for i in range(len(st1)):
            if st1[i] not in words or st2[i] not in words:
                return False
        li2 = list(st2)
        for m in range(len(st1)):
            index = li2.index(st1[m])
            li2[index] = ""
        return "".join(li2) == ""
    else:
        return False


def solution3(st1, st2):  # O(n)
    dic1 = {}
    dic2 = {}
    if len(st1) == len(st2):
        for i in range(len(st1)):
            dic1[st1[i]] = dic1.get(st1[i], 0) + 1
            dic2[st2[i]] = dic2.get(st2[i], 0) + 1
        return dic1 == dic2
    else:
        return False


if __name__ == "__main__":
    print(
        "solution1: ",
        timeit.timeit("solution('abc', 'bca')", setup="from __main__ import solution"),
    )
    print(
        "solution2: ",
        timeit.timeit(
            "solution2('abc', 'bca')", setup="from __main__ import solution2"
        ),
    )
    print(
        "solution3: ",
        timeit.timeit(
            "solution3('abc', 'bca')", setup="from __main__ import solution3"
        ),
    )
