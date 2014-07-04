import sys
def dictPaser(arg1):
    sent_file = open(arg1)
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)
    sent_file.close()
    return scores 

def tweetTextPaser(json_line):
    import json
    temp = json.loads(json_line)
#    print temp.keys()
    if temp.keys() == [u"delete"]:
        return "" 
    else : 
        return temp["text"].lower().split()
        
def tweetPlacePaser(json_line):
    import json
    temp = json.loads(json_line)
#    print temp.keys()
    if temp.keys() == [u"delete"]:
        return None 
    else : 
        return temp["place"]

def getTweetScore(argu2,sent_dict):
    tweet_fo = open(argu2)
    score = []
    for line in tweet_fo:
        temp_score = 0
        tweet_list = tweetTextPaser(line)
        for word in tweet_list:
            if sent_dict.has_key(word):
                temp_score = temp_score + sent_dict[word]
        score.append(temp_score)
    tweet_fo.close()
    return score
    
def getTweetState(arg2,tweet_score):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}

    tweet_fo = open(arg2)
    counter = 0
    state_dict = {}
    for line in tweet_fo:
        tweet_list = tweetPlacePaser(line)
        if tweet_list is not None: 
            if tweet_list["country_code"].lower() == "us":
                temp_state = tweet_list["full_name"].split(', ')[1]
                if states.has_key(temp_state):
                    if state_dict.has_key(temp_state):
                        state_dict[temp_state] += tweet_score[counter]
                    else:
                        state_dict[temp_state] = tweet_score[counter]
        counter +=1
    return state_dict 

def main():
    import operator
    sent_dict = dictPaser(sys.argv[1])
    tweet_score = getTweetScore(sys.argv[2],sent_dict)
    state_dict = getTweetState(sys.argv[2],tweet_score)
    max_pair = max(state_dict.iteritems(), key = operator.itemgetter(1))[0]
#    result = max_pair[0] +" " + str(max_pair[1])
    print max_pair

    
if __name__ == "__main__":
    main()

