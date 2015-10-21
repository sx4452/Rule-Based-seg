__author__ = 'ben'

import jieba
import time
import sys
import codecs

reload(sys)                                                                          #Set the coding as 'utf-8' or you will get chaos
sys.setdefaultencoding('utf8')

from CONSTANT import USERDICTPATH
from CONSTANT import INPUTPATH
from CONSTANT import OUTPUTPATH
from CONSTANT import NEWDICTPATH

def main():
    userDict = open(USERDICTPATH, 'r')
    newDict = open(NEWDICTPATH, 'w+')
    userDictLines = userDict.readlines()
    curstr = ''
    for line in userDictLines:
        linelist = line.split(',')
        curstr = linelist[0] + '\n'
        newDict.write(curstr)
    newDict.close()
    userDict.close()

    jieba.load_userdict(NEWDICTPATH)
    inputFile = open(INPUTPATH, 'r')
    outputFile = open(OUTPUTPATH, 'w+')
    inputRead = inputFile.read()
    outputString = jieba.cut(inputRead)
    for i in outputString:
        curstr = i + '\\'
        outputFile.write(curstr)
    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print 'running time is'
    print end