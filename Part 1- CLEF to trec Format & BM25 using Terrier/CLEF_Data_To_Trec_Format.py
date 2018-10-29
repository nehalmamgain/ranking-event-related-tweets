# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:56:01 2017

@author: Nikhil
"""
import os

os.chdir('Data')
files=os.listdir('.')
for i in range(len(files)):
    f=files[i]
    op='tweets_'+f[-11:]
    outputFile=open(op,'w')
    inputFile=open(f)
    inputData=inputFile.readlines()

    for j in range(len(inputData)):
        k=inputData[j].split('\t')
        outputFile.write('<DOC>\n')
        outputFile.write('<DOCNO>'+k[0]+'</DOCNO>\n')
        outputFile.write(k[-1])
        outputFile.write('</DOC>\n')
        
    outputFile.close()
