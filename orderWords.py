#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Weibin Meng
# * Email         : m_weibin@163.com, mwb16@mails.tsinghua.edu.cn
# * Create time   : 2018-07-18 14:53
# * Last modified : 2019-07-20 21:35
# * Filename      : orderWords.py
# * Description   :
'''
'''
# **********************************************************


import os
import re
from ft_tree import getMsgFromNewSyslog


def orderTemplate(para):
    rawlog = para['rawlog']
    templates = para['templates']
    sequences = para['sequences']
    order_templates = para['order_templates']
    variable_symbol = para['variable_symbol']
    # remove_middle = para['remove_middle']

    tag_index={}
    index_tag={}
    tag_temp={}
    tag_log={}

    index=0            #在表中所在的行数
    with open(sequences) as IN:
        for line in IN:
            tag = line.strip()
            # print(tag)
            if tag not in tag_index:
                #print(tag)
                tag_index[tag]=index
                index_tag[index]=tag
            index+=1


    index=0
    with open(rawlog) as IN:
        for line in IN:
            if index in index_tag:
                tag_log[index_tag[index]]=line.strip()
            index+=1

    tag=1
    with open(templates) as IN:
        for line in IN:
            tag_temp[str(tag)]=line.strip()
            tag+=1

    f=open(order_templates,'w')
    for i in range(len(tag_temp)):
        tag=str(i+1)
        out=' '.join(list(set(tag_temp[tag].split())))
        if tag in tag_log:
            # find the correspondent raw log
            log=getMsgFromNewSyslog(tag_log[tag])[1]
            # print(log)
            # find the correspondent template
            temp=tag_temp[tag].split()
            new_temp=[]
            for k in log :
                if k in temp:
                    new_temp.append(k)
                    temp.remove(k)
                else:
                    new_temp.append(variable_symbol)
            # modify the template
            out = ' '.join(new_temp)
        f.writelines(out+'\n')
    print('ordered template_path', order_templates)
    # if remove_middle:
    #     os.remove(templates)

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-middle_templates', help='templates', type=str, default="./output/output.template")
    parser.add_argument('-sequences', help='sequences', type=str, default="./output/output.seq")
    parser.add_argument('-rawlog', help='rawlog', type=str, default="./new.log")
    parser.add_argument('-final_templates', help='rawlog', type=str, default="./output/output.template")
    parser.add_argument('-variable_symbol', help='symbol for variable in templates', type=str, default=" ")
    parser.add_argument('-remove_middle', help='if 1, delete middle results after training', type=int, default=0)
    parser.add_argument('-order_templates', help='rawlog', type=str, default="./output/order/output.order.template")
    args = parser.parse_args()

    para = {
    'rawlog': args.rawlog,
    'templates': args.middle_templates,
    'sequences' : args.sequences,
    'order_templates' : args.order_templates,
    'variable_symbol' : args.variable_symbol,
    'remove_middle': args.remove_middle
    }
    
    orderTemplate(para)
    print('ordered')









