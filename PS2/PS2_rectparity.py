# template for 6.02 rectangular parity decoding using error triangulation
import PS2_tests
import numpy as np

def rect_parity(codeword,nrows,ncols): 
    bits = (nrows+1)*(ncols+1)-1
    packet = np.array([[0]*(ncols+1)]*(nrows+1))
    bit = 0
    for row in range(nrows):
        for col in range(ncols):
            packet[row][col] = codeword[bit]
            bit += 1
    for row in range(nrows):
        packet[row][ncols] = codeword[bit]
        bit += 1
    for col in range(ncols):
        packet[nrows][col] = codeword[bit]
        bit += 1

    # Get the row, col of all parity errors 
    col_sums = packet.sum(axis=0)%2
    row_sums = packet.sum(axis=1)%2
    error_locs = []
    for r_index, r_parity in enumerate(row_sums):
        for c_index, c_parity in enumerate(col_sums):
            if c_parity == 1 and r_parity == 1:
                error_locs.append([r_index,c_index])
    
    # Remove parity bit errors
    for row in range(nrows):
        for col in range(ncols):
            if [row, ncols] in error_locs:
                error_locs.remove([row, ncols])
            elif [nrows, col] in error_locs:
                error_locs.remove([nrows, col])
            elif [nrows, ncols] in error_locs:
                error_locs.remove([nrows, ncols])

    # Default is to return the codeword data
    message = codeword[:(nrows*ncols)]

    # Correct all single-bit errors
    if len(error_locs) == 1:
        index = error_locs[0]
        if index[0] < nrows and index[1] < ncols:
            bit = index[0]*ncols + index[1]
            if packet[index[0]][index[1]] == 0:
                codeword[bit] = 1
            else:
                codeword[bit] = 0
            message = codeword[:(nrows*ncols)]
    return message

if __name__ == '__main__':
    PS2_tests.test_correct_errors(rect_parity)
