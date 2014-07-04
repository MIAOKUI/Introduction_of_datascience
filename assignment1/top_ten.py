import sys
def tweetObjectPaser(json_line):
    import json
    temp = json.loads(json_line)
    if temp.keys() == [u"delete"]:
        return [] 
    elif temp["entities"].has_key("hashtags"):
        return temp["entities"]["hashtags"]
    else:
        return []

def getHashtageMatrix(arg1):
    tweet_fo = open(arg1)
    tage_matrix = {}
    for line in tweet_fo:
        for subdict in tweetObjectPaser(line):
            if tage_matrix.has_key(subdict[u'text']):
                tage_matrix[subdict[u'text']] +=1
            else :
                tage_matrix[subdict[u'text']] = 1
    return tage_matrix
            
def sortPrint(tage_matrix):
    import operator
    sorted_matrix = sorted(tage_matrix.iteritems(),reverse = True,key = operator.itemgetter(1))
    for i in range(10):
        print sorted_matrix[i][0],sorted_matrix[i][1]

def main():
    tage_matrix = getHashtageMatrix(sys.argv[1])
    sortPrint(tage_matrix)

if __name__ == "__main__":
    main()