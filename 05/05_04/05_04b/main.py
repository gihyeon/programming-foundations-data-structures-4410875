"""
Problem: use a queue to generate the first n binary numbers
e.g. input: 5, output: the first 5 binary numbers
Consider looking for a pattern an using that pattern with a queue to generate future binary numbers
"""

from collections import deque

def gen_bin_num(n):

    if n <= 0:
        return

    bin_queue = deque()
    bin_queue.append('1')

    for _ in range(n):
        current_bin = bin_queue.popleft()
        print(current_bin)
        bin_queue.append(current_bin + '0')
        bin_queue.append(current_bin + '1')

gen_bin_num(5)
