
The folder contains 15 code (.py) files and 1 .res file:



CODE FILES:

rerank1_tweetRank.py : This file will be used to rerank results of BM25. It will find the number of tweets tweeted by the author of the tweet (tweet rank) and the follower rank (wrt our slides) of the author. 

rerank1_tweetRank2.py : This file will present the result in the following output - query ID, BM25 rank, tweet ID, follower rank, the rank of tweet according to this feature (follower rank), and the content of the tweet.

rerank1_tweetRank3.py : This file will present the result in the following output - query ID, BM25 rank, tweet ID, tweet rank (number of tweets posted by user), the rank according to this feature (tweet rank), and the content of the tweet.

rerank2_hashRank.py : This file will be used to rerank results of BM25. It will find the hashtag score (wrt our slides) for every line of BM25.res file

rerank2_hashRank2.py : This file will present the result in the following output - query ID, BM25 rank, tweet ID, hashtag score, the rank according to this feature (hash rank), and the content of the tweet.

rerank3_reply.py : This file will be used to rerank results of BM25. It will find whether a tweet is a reply or not.

rerank3_reply2.py : This file will present the result in the following output - query ID, BM25 rank, tweet ID, reply score, the rank according to this feature (reply rank), and the content of the tweet.

rerank4_RT.py : This file will be used to rerank results of BM25. It will find the retweet count of the tweet.

rerank4_RT2.py :  This file will present the result in the following output - query ID, BM25 rank, tweet ID, retweet score, the rank according to this feature (retweet rank), and the content of the tweet.

rerank5_timeline.py : This file will be used to rerank results of BM25. It will find how relevant the tweet is considering its date compared to the event (topic) date (wrt our slides).

rerank5_timeline2.py : This file will present the result in the following output - query ID, BM25 rank, tweet ID, tweet content, timeline score and the rank according to this feature (timeline rank).

rerank6_length.py : This file will be used to rerank results of BM25. It will find the length (number of words in the tweet) for each tweet.

rerank6_length2.py : This file will present the result in the following output - query ID, BM25 rank, tweet ID, tweet content, length score and the rank according to this feature (length rank).

rerank7_url.py :  This file will be used to rerank results of BM25. It will find whether a URL is present in the tweet.

rerank7_url2.py :  This file will present the result in the following output - query ID, BM25 rank, tweet ID, tweet content, URL score and the rank according to this feature (URL rank).



INPUT FILES:

BM25b0.75_0.res : This file is required as input for some of the programs.

Additional input: The CLEF dataset is required as input for these files. Link to download: https://drive.google.com/drive/u/1/folders/0B9C_Ok-9klI8ME4xUXF3WjJUSVk
This data (.txt.gz) needs to be extracted before it can be taken as input for the code files.

Note: Please ensure all input files are kept in the same folder as these codes.
