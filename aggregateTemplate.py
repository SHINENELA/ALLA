#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Weibin Meng
# * Email         : m_weibin@163.com
# * Create time   : 2017-05-07 15:56
# * Last modified : 2017-05-07 15:56
# * Filename      : aggregateTemplate.py
# * Description   :
'''
'''
# **********************************************************

import sys
from copy import deepcopy
from log_formatter import LogFormatter        
import time       
import os
import datetime
import re

def aggregateTemplate(indata,outdata):
    """
        
    """
    
    data_dir=indata
    output_dir=outdata
    log_list=[]
    outFile=file(output_dir,'w')
    with open(data_dir) as IN:
        for log in IN:
            log_list.append(log.strip())
    
    temp_dir={}
    for i,log in enumerate(log_list):
        temp_dir[i] = len(log)
    temp_dir = sorted(temp_dir.items(), key=lambda x:(x[1], x[0]), reverse=True)
    temp_index = [x[0] for x in temp_dir]
    new_log_list=[]
    for index in temp_index:
        new_log_list.append(log_list[index])

    for log in new_log_list:
        outFile.writelines(log+"\n")
if __name__ == "__main__":
    input='/home/users/zhangshenglin/data/syslog/S5500_S5800Template/Ziyan_template.dat'
    output='/home/users/zhangshenglin/data/syslog/S5500_S5800Template/arr_Ziyan_template.dat'
    aggregateTemplate(input,output)
    print ('Templates have aggregated ')










