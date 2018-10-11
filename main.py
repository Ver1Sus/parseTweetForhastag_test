#-*- coding: utf-8 -*-
import re
import datetime
import operator
from hashtag import Hastag


def findAllHashtags(fileName):
    with open(fileName, 'r') as f:
        return re.findall(r'#(\w+)', f.read().encode('cp1251').decode())


def getDictOfCounterWords(hashtagList):
    ##--- uniqe values (lowerCase) from the all list
    hashtagListLower = [hashtag.lower() for hashtag in hashtagList]
    uniqueHashtags = set(hashtagListLower)

    ##--count all and add to dictionary
    resultDict = {}
    for hastag in uniqueHashtags:
        resultDict[hastag] = hashtagListLower.count(hastag)
    return resultDict

def getTopTenHashtags(hashtagList):
    sortedHashtags = sorted(hashtagList.items(), key=operator.itemgetter(1), reverse=True)
    topTenHashtags = [Hastag(hashtag[0], hashtag[1]) for hashtag in sortedHashtags[:10]]
    return topTenHashtags






def getTweetsFromFile(fileName):
    result = []
    with open(fileName, 'r') as f:
        line = " "
        while line != "":
            line = f.readline().encode('cp1251').decode()
            result.append(line)
    return result


def findTweetWordsByHastag(allMessages, hashtagName):
    #TODO: регуляркой убрать знаки препинания, цифры,
    #  выбрать слова начинающиеся с буквы рус. англ. (поэтому другие хэштеги не считаются значимым словом)
    allWords = []
    for message in allMessages:
        if hashtagName in message.lower():
            message = re.sub(r'\w*[#0-9]\w*', '', message)
            message = re.sub(r'\w*[\!?@$№%&]\w+', '', message)
            allWords += re.findall(r'[А-яA-z]\w+', message.lower())
    return allWords

def getTopFiveWords(allWords):
    sortedHashtags = sorted(allWords.items(), key=operator.itemgetter(1), reverse=True)
    listOnlyWords = [word[0] for word in sortedHashtags[:5]]
    return listOnlyWords



def mainFunction():
    ##--- work with Hastags
    allHashtags = findAllHashtags('in.txt')
    resultDict = getDictOfCounterWords(allHashtags)
    topTenHashtags = getTopTenHashtags(resultDict)

    ##--- work with words
    allTweets = getTweetsFromFile('in.txt')

    resultDictWotds = {}
    for hashtag in (topTenHashtags):
        allWords = findTweetWordsByHastag(allTweets, hashtag.hastagName)

        ##--- get top 5 words in messages using the same logic as when searching for Hastags
        dictCounterWords = getDictOfCounterWords(allWords)
        topWords = getTopFiveWords(dictCounterWords)
        hashtag.addPopularWord(topWords)
        resultDictWotds[hashtag.hastagName] = topWords

    ##-- вывод для зания
    print([hashtag.hastagName for hashtag in topTenHashtags])
    print(resultDictWotds)

    ###--- информативный вывод
    # ([print(hashtag) for hashtag in topTenHashtags])


if __name__ == '__main__':
    mainFunction()
