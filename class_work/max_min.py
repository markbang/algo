# 写一个简短的递归程序，用于在不使用任何循环的条件下查找一个序列中的最小值和最大值

# def find_max(seq):
#     if len(seq) == 1:
#         return (f'Max num: {seq[0]}')
#     else:
#         if seq[0] > seq[1]:
#             return find_max([seq[0]] + seq[2:])
#         else:
#             return find_max(seq[1:])
        
# def fin_min(seq):
#     if len(seq) == 1:
#         return (f'Min num: {seq[0]}')
#     else:
#         if seq[0] < seq[1]:
#             return fin_min([seq[0]] + seq[2:])
#         else:
#             return fin_min(seq[1:])
        
def find_max_min(seq, mod):
    if len(seq) == 1:
        return (f'{mod} num: {seq[0]}')
    else:
        if mod == 'Max':
            return find_max_min([seq[0]] + seq[2:], mod) if seq[0] > seq[1] else find_max_min(seq[1:], mod)
        if mod == 'Min':
            return find_max_min([seq[0]] + seq[2:], mod) if seq[0] < seq[1] else find_max_min(seq[1:], mod)

if __name__ == '__main__':
    seq = [5, 3, 8, 2, 9, 1]
    print(find_max_min(seq, 'Max'), find_max_min(seq, 'Min'))    