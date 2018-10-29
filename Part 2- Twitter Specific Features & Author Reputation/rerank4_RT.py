#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 15:42:28 2017

@author: nehal
"""

# Can only use stats from this if third column does not contain -1 (tweet not found)
a = open('BM25b0.75_0.res')
b = open('author_retweet.txt', 'w') # tweet id

for i, line1 in enumerate(a):
    print 'Doing for BM line %d : '%(i)
    bm_fields = line1.split()
    tweet_id = bm_fields[2]
    match = 0
    output = bm_fields[0]+' '+bm_fields[3]+' ' # Query number and Retrieved tweet rank
    print 'Scanning clef_file1...'
    for j, line2 in enumerate(open('clef_microblogs_festival2015-06.txt')):
        fields1 = line2[:-1].split('\t')
        rcount = 0
        if tweet_id == fields1[0]:
            for k, line3 in enumerate(open('clef_microblogs_festival2015-06.txt')):
                fields2 = line3[:-1].split('\t')
                if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                    rcount += 1
            output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
            print output
            b.write(output)        
            match = 1
            break        
    if match == 1:
        continue
    else:
        print 'Scanning clef_file2...'
        for j, line2 in enumerate(open('clef_microblogs_festival2015-07.txt')):
            fields1 = line2[:-1].split('\t')
            rcount = 0
            if tweet_id == fields1[0]:
                for k, line3 in enumerate(open('clef_microblogs_festival2015-07.txt')):
                    fields2 = line3[:-1].split('\t')
                    if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                        rcount += 1
                output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                print output
                b.write(output)        
                match = 1
                break
        if match == 1:
            continue
        else:
            print 'Scanning clef_file3...'
            for j, line2 in enumerate(open('clef_microblogs_festival2015-08.txt')):
                fields1 = line2[:-1].split('\t')
                rcount = 0
                if tweet_id == fields1[0]:
                    for k, line3 in enumerate(open('clef_microblogs_festival2015-08.txt')):
                        fields2 = line3[:-1].split('\t')
                        if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                            rcount += 1
                    output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                    print output
                    b.write(output)        
                    match = 1
                    break
            if match == 1:
                continue
            else:
                print 'Scanning clef_file4...'
                for j, line2 in enumerate(open('clef_microblogs_festival2015-09.txt')):
                    fields1 = line2[:-1].split('\t')
                    rcount = 0
                    if tweet_id == fields1[0]:
                        for k, line3 in enumerate(open('clef_microblogs_festival2015-09.txt')):
                            fields2 = line3[:-1].split('\t')
                            if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                                rcount += 1
                        output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                        print output
                        b.write(output)        
                        match = 1
                        break
                if match == 1:
                    continue
                else:
                    print 'Scanning clef_file5...'
                    for j, line2 in enumerate(open('clef_microblogs_festival2015-10.txt')):
                        fields1 = line2[:-1].split('\t')
                        rcount = 0
                        if tweet_id == fields1[0]:
                            for k, line3 in enumerate(open('clef_microblogs_festival2015-10.txt')):
                                fields2 = line3[:-1].split('\t')
                                if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                                    rcount += 1
                            output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                            print output
                            b.write(output)        
                            match = 1
                            break
                    if match == 1:
                        continue
                    else:
                        print 'Scanning clef_file6...'
                        for j, line2 in enumerate(open('clef_microblogs_festival2015-11.txt')):
                            fields1 = line2[:-1].split('\t')
                            rcount = 0
                            if tweet_id == fields1[0]:
                                for k, line3 in enumerate(open('clef_microblogs_festival2015-11.txt')):
                                    fields2 = line3[:-1].split('\t')
                                    if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                                        rcount += 1
                                output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                                print output
                                b.write(output)        
                                match = 1
                                break
                        if match == 1:
                            continue
                        else:
                            print 'Scanning clef_file7...'
                            for j, line2 in enumerate(open('clef_microblogs_festival2015-12.txt')):
                                fields1 = line2[:-1].split('\t')
                                rcount = 0
                                if tweet_id == fields1[0]:
                                    for k, line3 in enumerate(open('clef_microblogs_festival2015-12.txt')):
                                        fields2 = line3[:-1].split('\t')
                                        if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                                            rcount += 1
                                    output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                                    print output
                                    b.write(output)        
                                    match = 1
                                    break
                            if match == 1:
                                continue
                            else:
                                print 'Scanning clef_file8...'
                                for j, line2 in enumerate(open('clef_microblogs_festival2016-01.txt')):
                                    fields1 = line2[:-1].split('\t')
                                    rcount = 0
                                    if tweet_id == fields1[0]:
                                        for k, line3 in enumerate(open('clef_microblogs_festival2016-01.txt')):
                                            fields2 = line3[:-1].split('\t')
                                            if k!=j and 'RT' in fields2[10] and len(set(fields1[10].split()).intersection(set(fields2[10].split())))>=5: # compared tweet B is not the same as original tweet A, 'RT' exists in tweet B, and atleast 5 words are the same between tweet A and tweet B
                                                rcount += 1
                                        output += tweet_id+' '+str(rcount)+'\n' # tweet id and rt count
                                        print output
                                        b.write(output)        
                                        match = 1
                                        break
                                if match != 1:
                                    output += '-1\n' # Did not match tweet id in corpus
                                    b.write(output)        
                                    print output


b.close()