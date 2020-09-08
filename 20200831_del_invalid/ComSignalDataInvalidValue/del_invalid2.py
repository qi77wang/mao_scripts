#!/usr/bin/env python
# coding:utf-8

import sys

if __name__ == '__main__':
    print("start to do work")

    # 从1的实现发现，发现处理list时，删除某个元素，后面的所有元素会平移，导致下标也随之变化
    # 所以尽量不要直接删除list中的某个元素，可以选择新建list，把不需要的元素剔除；

    input_file = sys.argv[1]

    i = 0

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

                list_line[i-1] = 'meng_to_del'
                list_line[i] = 'meng_to_del'
                list_line[i+1] = 'meng_to_del'
                list_line[i+2] = 'meng_to_del'
            i += 1

    # 现在问题转化为删除list中的某个重复元素
    # del meng_to_del

    # 方法1，遍历list，碰到符合条件的，删除，但因为list是动态的，需要倒序删除；
    # for i in range(len(list_line)-1, -1, -1):
    #     if list_line[i] == 'meng_to_del':
    #         list_line.pop(i)

    # 方法2，遍历list，将元素赋给新的list，如果符合条件，则跳过，此处用filter实现；
    list_line = filter(lambda x: x != 'meng_to_del', list_line)

    fp1 = open('./output.txt', 'w')
    for line in list_line:
        fp1.write(line)

    fp1.close()

    print("generate output.txt success")
