# template file for 6.02 PS1, Python Task 1
import PS1_tests, numpy

def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0

def get_tree(pList):
    """
    Returns a list of lists of the Huffman Tree
    """
    sorted_pList = sorted(pList, key=lambda p: p[0], reverse = True)   # Sort based on descending probabilities
    if len(sorted_pList) == 1:
        return sorted_pList[0][1]
    else:
        last = sorted_pList[-1]
        second_last = sorted_pList[-2]
        new_prob = last[0] + second_last[0]
        new_name = [last[1], second_last[1]]
        new_entry = (new_prob, new_name)
        sorted_pList = sorted_pList[:-2]
        sorted_pList.append(new_entry)
        return get_tree(sorted_pList)

def get_huffman_encoding(symbol, huff_tree, path):
    print(f"{symbol}, {huff_tree}")
    left_side = huff_tree[0]
    right_side = huff_tree[1]
    if str(symbol) == left_side:
        path.append(0)
        print(f"Symbol = {symbol}, Path = {path}")
        code = path
        return code
    elif str(symbol) == right_side: 
        path.append(1)
        print(f"Symbol = {symbol}, Path = {path}")
        code = path
        return code
    elif isinstance(huff_tree[0], list): # and symbol in huff_tree[0]:
        path += [0]
        print(f"Symbol = {symbol}, Path = {path}")
        backtrack_len = len(path)
        code = get_huffman_encoding(symbol, huff_tree[0], path)
        if code == None: # isinstance(huff_tree[1], list): # and symbol in huff_tree[1]:
            path = path[:backtrack_len-1]
            path += [1]
            print(f"Symbol = {symbol}, Path = {path}")
            code = get_huffman_encoding(symbol, huff_tree[1], path)
    elif isinstance(huff_tree[1], list):
        path += [1]
        print(f"Symbol = {symbol}, Path = {path}")
        backtrack_len = len(path)
        code = get_huffman_encoding(symbol, huff_tree[1], path)
        if code == None: # isinstance(huff_tree[1], list): # and symbol in huff_tree[1]:
            path = path[:backtrack_len-1]
            path += [0]
            print(f"Symbol = {symbol}, Path = {path}")
            code = get_huffman_encoding(symbol, huff_tree[0], path)
    else:
        return None
    return code

# arguments:
#   plist -- sequence of (probability,object) tuples
# return:
#   a dictionary mapping object -> binary encoding
def huffman(pList):
    """
    Example:
    plist: ((0.50,'A'),(0.25,'B'),(0.125,'C'),(0.125,'D'))
    returns: {'A': [0], 'B': [1, 0], 'C': [1, 1, 0], 'D': [1, 1, 1]} 
    """
    huff_tree = get_tree(pList)
    huffman_dict = {symbol[1]:get_huffman_encoding(symbol[1], huff_tree, []) for symbol in pList}
    return huffman_dict


if __name__ == '__main__':
    # test case 1: four symbols with equal probability
    PS1_tests.test_huffman(huffman,
                           # symbol probabilities
                           ((0.25,'A'),(0.25,'B'),(0.25,'C'),
                            (0.25,'D')),
                           # expected encoding lengths
                           ((2,'A'),(2,'B'),(2,'C'),(2,'D')))

    # test case 2: example from section 22.3 in notes
    PS1_tests.test_huffman(huffman,
                           # symbol probabilities
                           ((0.34,'A'),(0.5,'B'),(0.08,'C'),
                            (0.08,'D')),
                           # expected encoding lengths
                           ((2,'A'),(1,'B'),(3,'C'),(3,'D')))

    # test case 3: example from Exercise 5 in notes
    PS1_tests.test_huffman(huffman,
                           # symbol probabilities
                           ((0.07,'I'),(0.23,'II'),(0.07,'III'),
                            (0.38,'VI'),(0.13,'X'),(0.12,'XVI')),
                           # expected encoding lengths
                           ((4,'I'),(3,'II'),(4,'III'),
                            (1,'VI'),(3,'X'),(3,'XVI')))

    # test case 4: 3 flips of unfair coin
    phead = 0.9
    plist = []
    for flip1 in ('H','T'):
        p1 = phead if flip1 == 'H' else 1-phead
        for flip2 in ('H','T'):
            p2 = phead if flip2 == 'H' else 1-phead
            for flip3 in ('H','T'):
                p3 = phead if flip3 == 'H' else 1-phead
                plist.append((p1*p2*p3,flip1+flip2+flip3))
    expected_sizes = ((1,'HHH'),(3,'HTH'),(5,'TTT'))
    PS1_tests.test_huffman(huffman,plist,expected_sizes)
