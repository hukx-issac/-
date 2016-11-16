# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 15:35:34 2016

@author: Issac
"""

#import os,sys
import jieba, codecs
import jieba.posseg as pseg

names = {}  # “人名”：人名出现次数
relationships = {}
lineNames = []

dictfile = r'.\dict.txt'
contentfile = r'.\hls_content.txt'
jieba.load_userdict(dictfile)   #加载词典

with codecs.open(contentfile,'r','utf8') as f:
    for line in f.readlines():
        poss = pseg.cut(line)   # 分词并标注词性
        lineNames.append([])
        for w in poss:
            if w.flag != "nr" or len(w.word)<2:
                continue
            lineNames[-1].append(w.word)  # 将该人名加入该段人物列表
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

for line in lineNames:                    # 对于每一段
    for name1 in line:                    
        for name2 in line:                # 每段中的任意两个人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:        # 若两人尚未同时出现则新建项
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+ 1        # 两人共同出现次数加 1

with codecs.open('node.txt','w','utf8') as f:
    f.write('Id Label Weight\r\n')
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")
        
with codecs.open("edge.txt", 'w','utf8') as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")

        