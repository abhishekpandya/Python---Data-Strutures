## Return Index of words present in sentenceList 

def simpleTextQueries(sentenceList,query):
    result=[]
    finalResult=[]
    flag=False
    for queryToken in query:
        words=queryToken.split(" ")
        for sentence in sentenceList:
            for word in words:
                if word in sentence: 
                    index=sentenceList.index(sentence)
                    flag=True
                else:
                    flag= False
                    break
            if flag: 
                result.append(index)
        if len(result)>0:finalResult.append(result)
        else:finalResult.append(-1)
        result=[]
    return finalResult