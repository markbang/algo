from array_stack import ArrayStack


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""

    lefty = "({["  # opening delimiters
    righty = ")}]"  # respective closing delims
    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched?


if __name__ == "__main__":
    # expr = '((()(()){([()])}))' # '[(5+x)-(y+z)]'
    # expr = '[(5+x)-(y+z)]'
    expr = "[(5+x)-(y+z)"
    print(is_matched(expr))
