from array_stack import ArrayStack
import string

def infix_to_post_fix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    op_stack = ArrayStack()
    post_fix_list = []

    token_list = infix_expr.split()

    for token in token_list:
        if token in string.ascii_uppercase:
            post_fix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                post_fix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                (prec[op_stack.top()] >= prec[token]):
                post_fix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        post_fix_list.append(op_stack.pop())

    return " ".join(post_fix_list)


if __name__ == "__main__":
    # infix_expr = "( A + B ) * ( C + D )"
    # infix_expr = "( A + B ) * C"
    infix_expr = "A + B * C"
    print(infix_to_post_fix(infix_expr))
