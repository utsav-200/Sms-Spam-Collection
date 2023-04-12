import pandas as pd
messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t' ,names=["label","message"])

import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#create Object for stemming
ps=PorterStemmer() 
#corpus is used to stored clean sentences
corpus=[]
#Code For Sentence Cleaning And Stemming
for i in range (0,len(messages)):
    #we are replacing everything except a-z with spaces or lemmatize
    review = re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review = review.lower()
    review=review.split()
    #for stemming-review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)