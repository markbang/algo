from deque import Deque

def palchecker(a_string):
    print(a_string)
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_last(ch)

    still_equal = True

    while len(char_deque) > 1 and still_equal:
        print(char_deque.first(), char_deque.last())
        first = char_deque.delete_first()
        last = char_deque.delete_last()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == "__main__":
    # a_string1 = 'lsdkjfskf'
    a_string1 = '上海自来水来自海上'
    print(palchecker(a_string1))
    a_string2 = 'TENET'
    print(palchecker(a_string2))
