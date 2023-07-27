#!/usr/bin/python3
'''Validate a UTF-8 '''


def validUTF8(data):
    '''validate a give dataset for utf-8 encoding'''
    def num_byte_to_utf8(value):
        '''checks the number of byte the value have'''
        if value < 128:
            return 1
        elif value < 224:
            return 2
        elif value < 240:
            return 3
        elif value < 248:
            return 4
        else:
            return -1

    i = 0
    while i < len(data):
        num_byte = num_byte_to_utf8(data[i] & 0xFF)

        if num_byte == -1:
            return False
        for j in range(1, num_byte):
            if i + j >= len(data) or not 128 <= data[i + j] < 192:
                return False
        i += num_byte
    return True
