import sys

def dictPaser(arg1):
    sent_file = open(arg1)
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)
    sent_file.close()
    return scores 

def tweetPaser(json_line):
    import json
    temp = json.loads(json_line)
#    print temp.keys()
    if temp.keys() == [u"delete"]:
        return "" 
    else : 
        return temp["text"].lower().split()

def getTweetScore(argu2):
    tweet_fo = open(argu2)
    score = []
    for line in tweet_fo:
        temp_score = 0
        tweet_list = tweetPaser(json_line)
        for word in tweet_list:
            if sent_dict.has_key(word):
                score = score + sent_dict[word]
        score.append(temp)
    tweet_fo.close()
    return score

def getScoresMatrix(old_dict,argu2,tweet_scores):
    tweet_fo = open(argu2)
    newDict = {}
    counter = 0
    for line in tweet_fo:
        for word in tweetPaser(line):
             if old_dict.has_key(word) == False:
                 if tweet_scores[counter] !=0:
                     if newDict.has_key(word):
                         newDict[word] = newDict[word] + tweet_scores[counter]
                     else:
                         newDict[word] = tweet_scores[counter]
    return newDict


def main():


if __name__ == '__main__':
    main()