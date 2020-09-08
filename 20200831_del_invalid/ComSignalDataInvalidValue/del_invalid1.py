#!/usr/bin/env python
# coding:utf-8

import sys

if __name__ == '__main__':
    print("start to do work")

    input_file = sys.argv[1]

    list_index = []
    i = 0

    # 记录index
    with open(input_file, 'r') as fp:
        list_line = fp.readlines()
        for line in list_line:
            line = line.strip()
            if "ComSignalDataInvalidValue" in line:
                # 容错
                if "<ECUC-NUMBERICAL-PARAM-VALUE>" not in list_line[i-1] and \
                    "<DEFINITION-REF" not in list_line[i] and \
                    "<VALUE>" not in list_line[i+1] and \
                    "</ECUC-NUMBERICAL-PARAM-VALUE>" not in list_line[i+2]:
                    print("error:input file has unknown format, please check it")
                    sys.exit(1)

                list_index.append(i)
            i += 1

    j = 0

    # 删除元素
    for index in list_index:
        # 删除后，list会缩短，下标也会移动，此代码用于消除下标移动的影响；
        index = index - 4*j

        # 删除前一个后，下标又移动了，所以只需将最小的下标对应的元素删除4遍；
        list_line.pop(index-1)
        # list_line.pop(index)
        list_line.pop(index-1)
        # list_line.pop(index +1)
        list_line.pop(index-1)
        # list_line.pop(index +2)
        list_line.pop(index-1)
        j += 1

    fp1 = open('./output.txt', 'w')
    for line in list_line:
        fp1.write(line)

    fp1.close()

    print("generate output.txt success")
