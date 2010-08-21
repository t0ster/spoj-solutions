'''
6692. B - Esperanto Lessons
Problem code: BOLESSON
Problem url: https://www.spoj.pl/problems/BOLESSON/
'''
import sys
from itertools import chain

def main():
    try:
        input = open(sys.argv[1]).read()
    except IndexError:
        print("Usage: %s <input>" % sys.argv[0].split('/')[-1])
    input = [i for i in input.split("\n")]
    input = split1(input)
    input = split2(input)
    for testcase in input:
        print get_min_accumulated_difference(testcase)
    
def split1(iterable, result=[]):
    '''
    2
    2
    1 2
    2
    3 4
    2
    2
    1 4
    2
    2 3
    -->
    [['2', '1 2', '2', '3 4'], ['2', '1 4', '2', '2 3']]
    '''
    if len(iterable) < 3:
        return result
    value = int(iterable[0])
    part = iterable[1:value*2+1]
    del(iterable[:value*2+1])
    result.append(part)
    return split1(iterable, result)

def split2(iterable):
    '''
    [['2', '1 2', '2', '3 4'], ['2', '1 4', '2', '2 3']]
    -->
    [[[1, 2], [3, 4]], [[1, 4], [2, 3]]]
    '''
    result = []
    for part in iterable:
        result.append(
                [[int(j) for j in i.split(' ')] for i in part if ' ' in i]
        )
    return result

def get_min_accumulated_difference(testcase):
    return min(
        [count_accumulated_difference(testcase, t) for t in chain(*testcase)]
    )
    
def count_accumulated_difference(testcase, t):
    ad = 0
    for division in testcase:
        basic_count = len(filter(lambda x: x < t, division))
        advanced_count = len(filter(lambda x: x >= t, division))
        ad += abs(basic_count-advanced_count)
    return ad
    
if __name__ == "__main__":
    main()