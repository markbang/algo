from array_stack import ArrayStack


def post_fix_eval(post_fix_expr):
    operand_stack = ArrayStack()
    token_list = post_fix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == "__main__":
    # post_fix_expr = "7 8 + 3 2 + /"
    post_fix_expr = "4 5 6 * +"
    print(post_fix_eval(post_fix_expr))
