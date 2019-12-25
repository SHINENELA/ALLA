#!/usr/bin/python
# -*- coding: utf-8 -*-

# **********************************************************
# * Author        : Weibin Meng
# * Email         : m_weibin@163.com
# * Create time   : 2018-07-17 23:43
# * Last modified : 2018-07-24 00:06
# * Filename      : countFreTemplates.py
# * Description   :
'''                    在这里修改了第20行的路径、第62、84行的range(11)和第31、72行的l[1]
'''
# **********************************************************

import os
#import matplotlib
import matplotlib.pyplot as plt
import os

rawlogPath='./env-itsm-was-systemerr0603.log'
logSeqPath='./output/output.learnonebyone.seq'
templatePath='./output/output.template'
out_path='./output/err_top10/'
new_log_path='./new.log'
out_paths='./output/err_top10/content/'


# rawlogPath='./env-itsm-was-systemerr0603.log'
# logSeqPath='./ft_tree/err_logSequence.txt'
# templatePath='./ft_tree/err_logTemplate_order.txt'
countDir={}
with open(logSeqPath) as IN:
    for line in IN:
        l=line.strip().split()
        tag=l[0]
        if tag not in countDir:
            countDir[tag]=0
        countDir[tag]+=1

sorted_final_tuple=sorted(countDir.items(),key=lambda asd:asd[1] ,reverse=True)

print('times:',sorted_final_tuple)
# #画所有模板频率分布（柱状图）

# name_list=[]
# num_list=[]
# for i,n in enumerate(sorted_final_tuple[:10]):
#     name_list.append(n[0])
#     num_list.append(n[1])
# # plt.bar(range(len(num_list)), num_list,color='rgb')
# plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
# plt.yscale('log')#y坐标取对数
# # plt.xticks([])#关闭x坐标
# plt.title('systemout0603 Top10 templates in all logs')
# plt.show()



#保存Top 10的模板 并且输出每条模板对应的日志文件
top10_temp_dir={}# {tag:template}
temp_list=[]
with open(templatePath) as IN:
    for line in IN:                 
        temp_list.append(line.strip())

print ('top10 templates:')
for i in range(10):
    tag=sorted_final_tuple[i][0]
    top10_temp_dir[tag]=temp_list[int(tag)-1]
    print (tag,countDir[tag],top10_temp_dir[tag])#输出前10位的模板标签、出现次数和日志模板
print ('')
index=0
save_dir={}#记录了top10 templates对应的{日志行数(index):tag}
with open(logSeqPath) as IN:
    for line in IN:
        l=line.strip().split()
        tag=l[0]
        if tag in top10_temp_dir:
            save_dir[index]=tag
        index+=1
#tag_log={}#{tag:rawlog_list[]}
f_dir={}#{tag:file_iter}

rank=out_path+'top10_templates.txt'
#文件中包含前十名模板标签、出现次数和对应的模板，没有出现匹配模板的所有原始日志
index=0
temp_list=[]
with open(rank,'w')as ff:
#f=file(out_path+'top10_templates.txt','w')
    for i in range(10):
        tag=sorted_final_tuple[i][0]
        num=sorted_final_tuple[i][1]
        ff.writelines('tag:'+str(tag)+' '+'num:'+str(num)+'\n'+top10_temp_dir[tag]+'\n'+'\n')
    ff.close()

# for tag in top10_temp_dir:
#     print(tag)
#     content = out_paths + str(tag) + '.txt'
#     cur_template = top10_temp_dir[tag]
#     with open(content, 'a')as f:
#         f.writelines('template:' + '\t' + cur_template + '\n' + '\n')
#         f.close()


# 输出前十名模板对应日志的文件输出不对
with open(new_log_path) as IN:
    for log in IN:

        if index in save_dir:
            tag=save_dir[index]
            cur_template=top10_temp_dir[tag]
            content = out_paths + str(tag) + '.txt'

            # if tag not in temp_list:
            #     temp_list.append(tag)
            print ('tag:',tag,'\n','template:',cur_template)
            print ('log:',log.strip())
            print ('\n')
            # 按照New log 中日志正文出现的顺序列出前十名模板的对应Log 不是按照把同一tag下的所有日志放在一起输出的

            with open(content, 'a')as f:
                # f=file(out_path+str(tag)+'.txt','w')

                f.writelines('template:' + '\t' + cur_template + '\n' + '\n')
                f.writelines('log:'+'\n'+'\t'+log + '\n')

        index+=1


print ('end')

