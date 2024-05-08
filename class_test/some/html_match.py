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
    
def is_matched_html(raw: str):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()


if __name__ == '__main__':
    html = '''
    <body>
<h1>Hello World!</h1>
<div></div></body>
    '''
    print(is_matched_html(html))