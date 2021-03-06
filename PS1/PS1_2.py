# template file for 6.02 PS1, Python Task 2
import numpy,random
import PS1_tests
from PS1_1 import huffman

# arguments:
#   encoding_dict -- dictionary mapping characters to binary encodings,
#                    as provided by your huffman procedure from PS1_1
#   encoded_message -- a numpy array of 0's and 1's representing the encoded message
# return:
#   a list of decoded symbols
def decode(encoding_dict,encoded_message):
    """
    Example:
    encoding_dict: {'A': [1, 1], 'C': [1, 0, 0], 'B': [0], 'D': [1, 0, 1]}
    encoded_msg: [1, 1, 0, 1, 0, 0, 1, 0, 1]
    returns 'ABCD'
    """
    msg = []
    buffer = []
    keys = list(encoding_dict.keys())
    values = list(encoding_dict.values())
    for bit in encoded_message:
       buffer.append(bit)
       if buffer in values:
              msg.append(keys[values.index(buffer)])
              buffer = []
    return msg

if __name__ == '__main__':
    # start by building Huffman tree from probabilities
    plist = ((0.34,'A'),(0.5,'B'),(0.08,'C'),(0.08,'D'))
    cdict = huffman(plist)

    # test case 1: decode a simple message
    message = ['A', 'B', 'C', 'D']
    encoded_message = PS1_tests.encode(cdict,message)
    decoded_message = decode(cdict,encoded_message)
    assert message == decoded_message, \
           "Decoding failed: expected %s, got %s" % \
           (message,decoded_message)

    # test case 2: construct a random message and encode it
    message = [random.choice('ABCD') for i in range(100)]
    encoded_message = PS1_tests.encode(cdict,message)
    decoded_message = decode(cdict,encoded_message)
    assert message == decoded_message, \
           "Decoding failed: expected %s, got %s" % \
           (message,decoded_message)

    print("Tests passed!")
