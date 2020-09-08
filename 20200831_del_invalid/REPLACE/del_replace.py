#!/usr/bin/env python
# coding: utf=8

import sys

if __name__ == '__main__':
    print('start to do work')

    input_file = sys.argv[1]

    i = 0

    with open(input_file, 'r') as fp:
        list_line = fp.readlines()
        for line in list_line:
            if 'REPLACE' in line:
                # 容错
                if "<ECUC-TEXTUAL-PARAM-VALUE>" not in list_line[i-2] and \
                    "<DEFINITION-REF" not in list_line[i-1] and \
                    "<VALUE>" not in list_line[i] and \
                    "</ECUC-TEXTUAL-PARAM-VALUE>" not in list_line[i+1]:
                    print("error:input file has unknown format, please check it")
                    sys.exit(1)
                list_line[i-2] = 'meng_to_del'
                list_line[i-1] = 'meng_to_del'
                list_line[i] = 'meng_to_del'
                list_line[i+1] = 'meng_to_del'
            i += 1

    list_line = filter(lambda x: x!='meng_to_del', list_line)

    fp1 = open('./output.txt', 'w')
    fp1.writelines(list_line)
    fp1.close()
    print('generate output.txt success')