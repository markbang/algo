# 定义range类，实现range函数的功能
class Range:
    
    def __init__(self, start, end=None, step=1):
        self._start = start
        self._end = end
        self._step = step
        
        if end is None:
            self._end = start
            self._start = 0
            
        if step == 0:
            raise ValueError('step cannot be 0')
        
        self._length = max(0, (self._end - self._start + self._step - 1) // self._step)
        
    def __len__(self):
        return self._length
    
    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if 0 <= index < self._length:
            return self._start + index * self._step
        else:
            raise IndexError('index out of range')
        
if __name__ == '__main__':
    r = Range(10)
    print(list(r))
    print(r[1], r[-4])  # r[10] :IndexError: index out of range
    print(len(r), r._length)
    for i in r:
        print(i, end=' ')
        