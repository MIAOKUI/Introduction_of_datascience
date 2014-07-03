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


    
    
def main():
    sent_dict = dictPaser(sys.argv[1])
#    print sent_dict.items()
    tweets_fo = open(sys.argv[2])
    for json_line in tweets_fo:
        tweet_list = tweetPaser(json_line)
        score = 0
        for word in tweet_list:
            if sent_dict.has_key(word):
#                print sent_dict.has_key(word)
#                print word
                score = score + sent_dict[word]
        print score 
        
    tweets_fo.close()
if __name__ == '__main__':
    main()
