#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 15:42:28 2017

@author: nehal
"""

a = open('author_url.txt').readlines()
b = open('reranked_by_author_url.txt', 'w')
rankdict = {}
ranklist = []


for query in range(1,54):
    print 'Doing for query %d'%query
    rankdict = {}
    ranklist = []
    for line_index in range((query-1)*10, (query-1)*10+10):
        fields = a[line_index][:-1].split('\t')
        sub_fields = fields[0].split()
        rankdict[sub_fields[0]+' '+sub_fields[1]+' '+sub_fields[2]+'\t'+fields[1]] = sub_fields[3]
    for key, value in sorted(rankdict.iteritems(), reverse = True, key=lambda (k,v): (v,k)):
        ranklist.append((key, value))
    for index, i in enumerate(ranklist):
        output = i[0]+"\t"+i[1]+"\t"+str(index)+'\n'
        print output
        b.write(output)            
b.close()    
