import sys
def tweetPaser(json_line):
    import json
    temp = json.loads(json_line)
#    print temp.keys()
    if temp.keys() == [u"delete"]:
        return "" 
    else : 
        return temp["text"].lower().split()

def getTermFreq(arg1):
    tweet_fo = open(arg1)
    freq_matrix = {}
    for line in tweet_fo:
        for word in tweetPaser(line):
            if freq_matrix.has_key(word):
                freq_matrix[word] +=1
            else:
                freq_matrix[word] = 1
    freq_sum = sum(freq_matrix.values())
    for key in iter(freq_matrix):
        freq_matrix[key] = freq_matrix[key]/float(freq_sum)
        print key,freq_matrix[key]
    return freq_matrix

def main():
    freq_matrix = getTermFreq(sys.argv[1])
       
if __name__ == '__main__':
    main()
    
    
            
