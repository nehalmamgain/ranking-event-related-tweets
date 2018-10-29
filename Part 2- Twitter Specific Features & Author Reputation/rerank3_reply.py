#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 15:42:28 2017

@author: nehal
"""

# Can only use stats from this if third column does not contain -1 (tweet not found)
a = open('BM25b0.75_0.res')
b = open('author_reply.txt', 'w')

for i, line1 in enumerate(a):
    print 'Doing for BM line %d : '%(i)
    bm_fields = line1.split()
    tweet_id = bm_fields[2]
    match = 0
    output = bm_fields[0]+' '+bm_fields[3]+' ' # Query number and Retrieved tweet rank
    print 'Scanning clef_file1...'
    for line2 in open('clef_microblogs_festival2015-06.txt'):
        fields = line2[:-1].split('\t')
        reply = 0
        if tweet_id == fields[0]:
            if len(fields[10])>1 and fields[10][0]=='@':
                reply = '1'
            else:
                reply = '0'
            output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
            reply = 0
            if tweet_id == fields[0]:
                if len(fields[10])>1 and fields[10][0]=='@':
                    reply = '1'
                else:
                    reply = '0'
                output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
                reply = 0
                if tweet_id == fields[0]:
                    if len(fields[10])>1 and fields[10][0]=='@':
                        reply = '1'
                    else:
                        reply = '0'
                    output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
                    reply = 0
                    if tweet_id == fields[0]:
                        if len(fields[10])>1 and fields[10][0]=='@':
                            reply = '1'
                        else:
                            reply = '0'
                        output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
                        reply = 0
                        if tweet_id == fields[0]:
                            if len(fields[10])>1 and fields[10][0]=='@':
                                reply = '1'
                            else:
                                reply = '0'
                            output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
                            reply = 0
                            if tweet_id == fields[0]:
                                if len(fields[10])>1 and fields[10][0]=='@':
                                    reply = '1'
                                else:
                                    reply = '0'
                                output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
                                reply = 0
                                if tweet_id == fields[0]:
                                    if len(fields[10])>1 and fields[10][0]=='@':
                                        reply = '1'
                                    else:
                                        reply = '0'
                                    output += tweet_id+' '+reply+'\n' # tweet id and hash_score
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
                                    reply = 0
                                    if tweet_id == fields[0]:
                                        if len(fields[10])>1 and fields[10][0]=='@':
                                            reply = '1'
                                        else:
                                            reply = '0'
                                        output += tweet_id+' '+reply+'\n' # tweet id and hash_score
                                        print output
                                        b.write(output)        
                                        match = 1
                                        break
                                if match != 1:
                                    output += '-1\n' # Did not match tweet id in corpus
                                    b.write(output)        
                                    print output


b.close()
