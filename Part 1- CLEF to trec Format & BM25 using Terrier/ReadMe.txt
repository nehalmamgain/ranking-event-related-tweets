This ReadMe file contains the steps to convert CLEF Dataset into trec format (input format for Terrier). It then explains how to run the BM25 Ranking model of Terrier & evaluate the results.

Before beginning, create a parent/root folder with any name. All further steps will be performed either in this folder or its subdirectories. For this readme file, let’s assume the root folder name is IR. The root folder from hereon is the IR folder.
Also, read the important notes given at the end.


Part 1: Converting CLEF Dataset to trec format.

1. Download the CLEF dataset from the following link:
 https://drive.google.com/drive/u/1/folders/0B9C_Ok-9klI8ME4xUXF3WjJUSVk

2. Extract all the .txt files in a folder named 'Data' inside root(IR) directory.

3. Copy the python program provided with the name 'CLEF_Data_To_Trec_Format.py' in the IR folder.
 
4. Execute the above program. It will create 8 new files in the Data folder with name beginning with 'tweets_'. Move these files to a new folder with name 'tweets' in root(IR) directory.

This completes the conversion of data to trec format for input to terrier.

Part 2: Running BM25 using Terrier & evaluating results.

1. Download the Terrier tool from its website or the following link:

http://terrier.org/download/

2. Extract the tool from the zip/tar file in the root(IR) folder.

3. Copy the bat files provided in the terrier folder.

4. Run the ‘setup.bat’ file using cmd.

5. Copy the terrier.properties & task3-topics.trec files provided to the ‘etc’ folder inside Terrier folder.

6.Copy the qrel_all.qrels, qrel_pool.qrels & qrel_7s.qrels from 'mc2task3eval\topics\2016' folder inside CLEF dataset to the ‘etc’ folder inside Terrier folder.

7. Run the ‘BM25.bat’ file using cmd.

8. After successful execution, the \var\index folder inside terrier will contain the index files. The \var\results folder will contain the ‘.res’ file containing results & ‘.eval’ file will contain the evaluation results.

This completes the BM25 indexing using Terrier & its evaluation.


Important Notes:

1. Re-running the setup.bat will reset the properties file & it will have to be copied again.

2. If re-running, make sure the \var\index folder in terrier is empty.

3. The properties file is set to give 100 results per query. However in the next part of project, only top-10 tweets are considered due to computation constraints.

3. This ReadMe files is made according to Windows OS.

4. In case the directory names are different, please change them accordingly in the codes/commands.

5. batch file will not run on linux. Instead it can opened to run the commands with some changes.

- change the '.bat' extension in commands to '.sh’ .
- change '\' to '/' in the path.
- add 'sh' in front of each command, if required.