from __future__ import print_function
import sys
import time

def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    start_time = time.time()
    input = open(input_filename, 'r')
    input.r
    output = open(output_filename, 'w')
    for line in input:
        arr = line.split('\t')
        if arr[0] == arr[1]:
            continue
        output.write(line)

    print('clean time ', time.time() - start_time)

if __name__ == '__main__':
    main()