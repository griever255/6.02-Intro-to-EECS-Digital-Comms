# template file for 6.02 PS1, Python Task 1
import PS1_tests

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
    # Initialize a dictionary of symbols with empty lists of huffman encoding
    huffman = {}
    for tup in pList:
        huffman[tup[1]] = []
    
    # Sort the pList from greatest to least symbol probability
    sorted_pList = sorted(pList, key=lambda p: p[0], reverse = True)
    while not len(sorted_pList) == 1:   # Until there is only 1 item in the list
        last = sorted_pList[-1]         # Get the least probable symbol
        last_list = last[1].split(",")  # If it's a grouped symbol get the individual symbols
        for item in last_list:          # For each item in the group
            huffman[item].insert(0, 0)  # Add a "0" to the beginning of the huffman encoding
        second_last = sorted_pList[-2]  # Do the same for the second-least probable symbol
        second_last_list = second_last[1].split(",")
        for item in second_last_list:
            huffman[item].insert(0, 1)  # Except add a "1" to the beginning of the huffman encoding
        new_item = (last[0]+second_last[0], last[1]+","+second_last[1]) # Join the two least probable to a new entry
        sorted_pList = sorted_pList[:-2]    # Drop the two least probable
        sorted_pList.append(new_item)       # Add the grouped two least probable
        sorted_pList = sorted(sorted_pList, key=lambda p: p[0], reverse = True) # Sort the list by most probable
    return huffman
    

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
