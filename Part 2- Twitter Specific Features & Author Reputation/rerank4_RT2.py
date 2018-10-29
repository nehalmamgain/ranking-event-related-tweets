#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 15:42:28 2017

@author: nehal
"""

a = open('author_retweet.txt').readlines()
b = open('reranked_by_author_retweet.txt', 'w')
rankdict = {}
ranklist = []


for query in range(1,54):
    print 'Doing for query %d'%query
    rankdict = {}
    ranklist = []
    for line_index in range((query-1)*10, (query-1)*10+10):
        fields = a[line_index][:-1].split()
        rankdict[fields[0]+' '+fields[1]+' '+fields[2]] = fields[3]
    for key, value in sorted(rankdict.iteritems(), reverse = True, key=lambda (k,v): (v,k)):
        ranklist.append((key, value))
    for index, i in enumerate(ranklist):
        #match i[0].split()[2] to tweet content and append that
        tweet_id = i[0].split()[2]
        match = 0
        print 'Scanning clef_file1...'
        for line2 in open('clef_microblogs_festival2015-06.txt'):
            fields = line2[:-1].split('\t')
            if tweet_id == fields[0]:
                output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                print output
                b.write(output)        
                match = 1
                break        
        if match == 1:
            continue
        else:
            print 'Scanning clef_file2...'
            for line2 in open('clef_microblogs_festival2015-07.txt'):
                fields = line2[:-1].split('\t')
                if tweet_id == fields[0]:
                    output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                    print output
                    b.write(output)        
                    match = 1
                    break
            if match == 1:
                continue
            else:
                print 'Scanning clef_file3...'
                for line2 in open('clef_microblogs_festival2015-08.txt'):
                    fields = line2[:-1].split('\t')
                    if tweet_id == fields[0]:
                        output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                        print output
                        b.write(output)        
                        match = 1
                        break
                if match == 1:
                    continue
                else:
                    print 'Scanning clef_file4...'
                    for line2 in open('clef_microblogs_festival2015-09.txt'):
                        fields = line2[:-1].split('\t')
                        if tweet_id == fields[0]:
                            output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                            print output
                            b.write(output)        
                            match = 1
                            break
                    if match == 1:
                        continue
                    else:
                        print 'Scanning clef_file5...'
                        for line2 in open('clef_microblogs_festival2015-10.txt'):
                            fields = line2[:-1].split('\t')
                            if tweet_id == fields[0]:
                                output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                                print output
                                b.write(output)        
                                match = 1
                                break
                        if match == 1:
                            continue
                        else:
                            print 'Scanning clef_file6...'
                            for line2 in open('clef_microblogs_festival2015-11.txt'):
                                fields = line2[:-1].split('\t')
                                if tweet_id == fields[0]:
                                    output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                                    print output
                                    b.write(output)        
                                    match = 1
                                    break
                            if match == 1:
                                continue
                            else:
                                print 'Scanning clef_file7...'
                                for line2 in open('clef_microblogs_festival2015-12.txt'):
                                    fields = line2[:-1].split('\t')
                                    if tweet_id == fields[0]:
                                        output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                                        print output
                                        b.write(output)        
                                        match = 1
                                        break
                                if match == 1:
                                    continue
                                else:
                                    print 'Scanning clef_file8...'
                                    for line2 in open('clef_microblogs_festival2016-01.txt'):
                                        fields = line2[:-1].split('\t')
                                        if tweet_id == fields[0]:
                                            output = i[0]+"\t"+i[1]+"\t"+str(index)+'\t'+fields[10]+'\n'
                                            print output
                                            b.write(output)        
                                            match = 1
                                            break
                                    if match != 1:
                                        output += '-1\n' # Did not match tweet id in corpus
                                        b.write(output)        
                                        print output
            
b.close()    
