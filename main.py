#-*- coding: utf-8 -*-
import re
import datetime
import operator


def getTopTenHashtags(hashtagList):
    #TODO: сделать класс или нормальный массив, хотя хз как потом сортировать массив
    sortedHashtags = sorted(hashtagList.items(), key=operator.itemgetter(1), reverse=True)
    return sortedHashtags[:10]

def showTopTen(topTenHashtags):
    print("Top 10 hashtags:")
    for num, hashtag in enumerate(topTenHashtags):
        print("     {0}: {1} ({2})".format(num+1, hashtag[0], hashtag[1]))

def getDictOfCounterWords(hashtagList):
    print("All count of founded words: {0}".format(len(hashtagList)))

    ##--- uniqe values (lowerCase) from the all list
    hashtagListLower = [hashtag.lower() for hashtag in hashtagList]
    uniqueHashtags = set(hashtagListLower)
    print("All unique words: {0}".format(len(uniqueHashtags)))

    ##--count all and add to dictionary
    resultDict = {}
    for hastag in uniqueHashtags:
        resultDict[hastag] = hashtagListLower.count(hastag)
    return resultDict


def findAllHashtags():
    with open('test.txt', 'r') as f:
        return re.findall(r'#(\w+)', f.read().encode('cp1251').decode())




def getTweetsFromFile(fileName):
    result = []
    with open(fileName, 'r') as f:
        line = " "
        while line != "":
            line = f.readline().encode('cp1251').decode()
            result.append(line)
    return result


def findWordsForHastag(allMessages, hashtag):
    #TODO: регуляркой убрать знаки препинания, выбрать слова начинающиеся с буквы рус. англ. (поэтому другие хэштеги не считаются значимым словом)
    allWords = []
    for message in allMessages:
        if '#'+hashtag in message.lower():
            message = re.sub(r'\w*[#0-9]\w*', '', message)
            message = re.sub(r'\w*[\!?@$№%&]\w+', '', message)
            allWords += re.findall(r'[А-яA-z]\w+', message.lower())
    print(allWords)
    return allWords

def getTopFiveWords(allWords):
    sortedHashtags = sorted(allWords.items(), key=operator.itemgetter(1), reverse=True)
    listOnlyWords = [word[0] for word in sortedHashtags[:5]]
    return listOnlyWords



if __name__ == '__main__':
    ##--- work with Hastags
    allHashtags = findAllHashtags()
    resultDict = getDictOfCounterWords(allHashtags)
    topTenHashtags = getTopTenHashtags(resultDict)
    # showTopTen(topTenHashtags)

    ##--- work with words
    allTweets = getTweetsFromFile('test.txt')

    resultDictWotds={}
    #TODO: вот тут не ясно что представляет собой topTenHastag - надо в класс обернуть, будет лучше
    for  hashtag, numbers in (topTenHashtags):
        ##--- в ищем все сообщения где встречаются популя тэги поочереди
        # hashtag = topTenHashtags[0]
        print("\n"+"*"*10)
        print("Find 5 top words for #{0}".format( hashtag))
        allWords = findWordsForHastag(allTweets, hashtag)

        ##---и находим там 5 популярных слов по той же логике что и ищем хэштеги
        dictCounterWords = getDictOfCounterWords(allWords)
        topWords = getTopFiveWords(dictCounterWords)
        resultDictWotds[hashtag] = topWords

    print(resultDictWotds)

