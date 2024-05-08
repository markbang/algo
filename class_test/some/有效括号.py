class ArrayStack:
    
    def __init__(self):
        self._stack = []
        
    def __len__(self):
        return len(self._stack)
    
    def __str__(self) -> str:
        return str(self._stack)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self._stack.append(e)
        
    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._stack[-1]
    
    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._stack.pop()

def is_matched(expr):
    lefty = '([{'
    righty = ')]}'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()
            
            
if __name__ == '__main__':
    print(is_matched('({{}[][({})]})'))