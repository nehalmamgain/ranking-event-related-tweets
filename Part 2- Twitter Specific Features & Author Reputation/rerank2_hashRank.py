#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 15:42:28 2017

@author: nehal
"""

# Can only use stats from this if third column does not contain -1 (tweet not found)
import math
a = open('BM25b0.75_0.res')
b = open('author_hash_rank.txt', 'w') # tweet id and user name

setHash = set()
dictHash = {}

print 'Preparing hash for file 1'
for line in open('clef_microblogs_festival2015-06.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 2'
for line in open('clef_microblogs_festival2015-07.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 3'
for line in open('clef_microblogs_festival2015-08.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 4'
for line in open('clef_microblogs_festival2015-09.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 5'
for line in open('clef_microblogs_festival2015-10.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 6'
for line in open('clef_microblogs_festival2015-11.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 7'
for line in open('clef_microblogs_festival2015-12.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1
print 'Preparing hash for file 8'

for line in open('clef_microblogs_festival2016-01.txt'):
    fields = line[:-1].split('\t')
    for word in fields[10].split():
        if word[0]=='#':
            if word not in setHash:
                setHash.add(word)
                dictHash[word] = 0
            dictHash[word] += 1


listHash = []
for key, value in sorted(dictHash.iteritems(), reverse = True, key=lambda (k,v): (v,k)):
    listHash.append((key, value))
print 'dictHash and listHash prepared\n\n\n'

def hashScore(content):
    divby = -1
    num = 0
    deno = 0
    for word in content.split():
        divby += 1
        if word[0]=='#':
            num += 1 + math.log(dictHash[word], 2)
            deno += 1 + math.log(listHash[divby][1], 2)
    try:
        hash_score = float(num)/deno
    except Exception, e:
        hash_score = 0
    return hash_score

for i, line1 in enumerate(a):
    print 'Doing for BM line %d : '%(i)
    bm_fields = line1.split()
    tweet_id = bm_fields[2]
    match = 0
    output = bm_fields[0]+' '+bm_fields[3]+' ' # Query number and Retrieved tweet rank
    print 'Scanning clef_file1...'
    for line2 in open('clef_microblogs_festival2015-06.txt'):
        fields = line2[:-1].split('\t')
        if tweet_id == fields[0]:
            output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                    output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                        output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                            output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                                output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                                    output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
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
                                        output += tweet_id+' '+str(hashScore(fields[10]))+'\n' # tweet id and hash_score
                                        print output
                                        b.write(output)        
                                        match = 1
                                        break
                                if match != 1:
                                    output += '-1\n' # Did not match tweet id in corpus
                                    b.write(output)        
                                    print output


b.close()
