from nltk.corpus import stopwords	
from nltk.stem.wordnet import WordNetLemmatizer
import string 
import gensim
from gensim import corpora
import re
from config import * 

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
	stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
	normalized = "  ".join(lemma.lemmatize(word) for word in punc_free.split())
	return normalized


def extract_topic(doc):
	doc_clean = [clean(d).split() for d in doc]
	dictionary = corpora.Dictionary(doc_clean)
	doc_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
	Lda = gensim.models.ldamodel.LdaModel
	ldamodel = Lda(doc_matrix,num_topics = no_topic,id2word = dictionary, passes = 50)
	topic_list = filter_topics(ldamodel.print_topics(num_topics = no_topic, num_words = no_words))
	return topic_list
def cleanse_topic(txt):
	topic_list = []
	topic_probab = []
	re1='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	
	re2='.*?'	
	re3='((?:[a-z][a-z]+))'	
	re4='.*?'	
	re5='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	
	re6='.*?'	
	re7='((?:[a-z][a-z]+))'	
	re8='.*?'
	re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	
	re10='.*?'	
	re11='((?:[a-z][a-z]+))'
	rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11,re.IGNORECASE|re.DOTALL)
	match = rg.search(txt)
	if match:
		topic_probab.append(match.group(1))
		topic_probab.append(match.group(3))
		topic_probab.append(match.group(5))
		topic_list.append(match.group(2))
		topic_list.append(match.group(4))
		topic_list.append(match.group(6))
	return topic_list,topic_probab

def filter_topics(topics):
	topic_list = []
	topic_probab = []	
	for topic_set in topics:
		_ , topic = topic_set
		x,y = cleanse_topic(topic)
		topic_list.extend(x)
		topic_probab.extend(y)
	#print topic_list,topic_probab
	for i in range(len(topic_probab)):
		if float(topic_probab[i]) < thresh:
			topic_list[i] = ""
	topic_list = [x for x in topic_list if x != u'']
	return list(set(topic_list))
	

