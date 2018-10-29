#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 15:42:28 2017

@author: nehal
"""

# Can only use stats from this if third column in write file is not -1; however it is possible to get -1 -1 in 5th,6th column if user_screen name not matched and -1 only in 6th column if div by 0 for follower rank
import tweepy
a = open('BM25b0.75_0.res')
b = open('author_user_id.txt', 'w') # tweet id and user name

consumer_key = 'J1wBG12GmvwfA1SkVnARHm1Kz'
consumer_secret = 'CGiK0D8OD3QEC5DgTeQ147wLKkV1V9kjZ8j5mup18A2ic7aqE5'
access_token = '3266196758-Ljig3BQQZMPpAc3KHN5zyEOBX90zmyotVi4dJez'
access_token_secret = 'dqEYI6lPAfVPXx8ZOwEZDD7tCCPgwtlmOB0tdNSphludq'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def user_det(user_name):
    try:
        user = api.get_user(user_name)
    except Exception, e:
        print type(e)
        print e
        return '-1\t-1' # no author found
    output = str(user.statuses_count)+'\t'
    try:
        flwrRank = float(user.followers_count)/(float(user.followers_count)+user.friends_count)
    except Exception, e:
        print type(e)
        print e
        flwrRank = -1 # Division by 0
    output += str(flwrRank)
    return output # user name


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
            output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                    output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                        output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                            output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                                output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                                    output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
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
                                        output += tweet_id+' '+fields[1]+' '+user_det(fields[1])+'\n' # tweet id and user_name and (number of tweets(tweet_rank), follower_rank)
                                        print output
                                        b.write(output)        
                                        match = 1
                                        break
                                if match != 1:
                                    output += '-1\n' # Did not match tweet id in corpus
                                    b.write(output)        
                                    print output

b.close()
