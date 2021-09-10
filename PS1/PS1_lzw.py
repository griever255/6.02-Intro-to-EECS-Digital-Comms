# template file for 6.02 PS1, Python Task 4 (LZW Compression/Decompression)
import sys
from optparse import OptionParser
import struct
import array

def compress(filename):
    """
    Compresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to compress.
    Returns:
        None.
    """
    with open(filename, 'rb') as f:
        uncompressed = array.array("B", f.read())

    codewords = {}
    # initialize codewords for ASCII characters
    for i in range(256):
        codewords[struct.pack(">H", i)] = chr(i)

    outname = filename + "test.txt"
    output = ''
    outfile = open(outname, 'wb')
    # compress using LZW compression
    index = 256
    string = chr(uncompressed[0])
    for elem in uncompressed:
        symbol = chr(elem)
        if (string + symbol) in codewords.values():
            string = string + symbol
        else:
            codewords[index.to_bytes(2, 'big')] = string + symbol
            outfile.write(index.to_bytes(2, 'big'))
            # output += str(index.to_bytes(2, 'big'))
            index += 1
            string = symbol
    # print(output)
    
        
    #for i in range(len(codewords)):
        # print(f"key = {struct.pack('>H', i)} value = {codewords[struct.pack('>H', i)]}")
        

def uncompress(filename):
    """
    Decompresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to decompress.
    Returns:
        None.
    """
    with open(filename, 'rb') as f:
        compressed = array.array("H", f.read())

    codewords = {}
    # initialize codewords for ASCII characters
    for i in range(256):
        codewords[struct.pack(">H", i)] = chr(i)
    print(compressed)

    outname = filename + ".u"
    # output = ''
    # outfile = open(outname, 'wb')
    # compress using LZW compression
    index = 256
    code = compressed[0]
    # for elem in uncompressed:
    #     symbol = chr(elem)
    #     if (string + symbol) in codewords.values():
    #         string = string + symbol
    #     else:
    #         codewords[index.to_bytes(2, 'big')] = string + symbol
    #         outfile.write(index.to_bytes(2, 'big'))
    #         # output += str(index.to_bytes(2, 'big'))
    #         index += 1
    #         string = symbol
    # print(output)
    
        
    #for i in range(len(codewords)):
        # print(f"key = {struct.pack('>H', i)} value = {codewords[struct.pack('>H', i)]}")

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--filename", type="string", dest="fname", 
                      default="test", help="file to compress or uncompress")
    parser.add_option("-c", "--compress", action="store_true", dest="uncomp", 
                      default=True, help="compress file")
    parser.add_option("-u", "--uncompress", action="store_true", dest="uncomp", 
                      default=False, help="uncompress file")

    (opt, args) = parser.parse_args()
    
    if opt.uncomp == True:
        uncompress(opt.fname)
    else:
        compress(opt.fname)
