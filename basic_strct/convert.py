from ArrayStack import ArrayStack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = ArrayStack()
    
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
        
    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
        
    return new_string