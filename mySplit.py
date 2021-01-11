# 
# 画像フォルダを指定して，train,testに使用する画像を指定する
# trainval.txt test.txt を作成する
# 

import numpy as np
import os
import os.path

sourcedir = '../egohands_mine/images/'
targetdir = '../egohands_mine/'
trainfile = 'trainval.txt'
testfile = 'test.txt'
trainRatio = 0.8 #分割の割合

# get file list
filelist = os.listdir(sourcedir)
filelist = np.array(filelist)

# random permutation
numfile = filelist.shape[0]
randindex = np.random.permutation(numfile)

# number of files
numtrain = np.floor(numfile*trainRatio)

# open target files
trainpath=os.path.join(targetdir,trainfile)
testpath=os.path.join(targetdir,testfile)
ftrain=open(trainpath,'w')
ftest=open(testpath,'w')
cnt = 1

# write to target files
for index in randindex:
        splits = filelist[index].split(".")

        if cnt <= numtrain:
                ftrain.write(splits[0]+"\n")
        else:
                ftest.write(splits[0]+"\n")
        cnt=cnt+1

ftrain.close()
ftest.close()