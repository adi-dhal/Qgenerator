from stackapi import StackAPI,StackAPIError
from nltk.stem import PorterStemmer
from config import *
ps = PorterStemmer()

def identify_questions(tags):
	ques_id = []
	ques_score = []
	ques_body = []
	query = ""
	for i in range(len(tags)):
		tags[i] = ps.stem(tags[i])
		query = query + tags[i] + ';'
	query = query[0:-1]
	try:
		SITE = StackAPI('stackoverflow')
		SITE.page_size = page_size
		SITE.max_pages = max_pages
		questions = SITE.fetch('search' ,tagged = query , sort ='relevance')
		for item in questions[u'items']:
			tags_ques = item[u'tags']
			for i in range(len(tags_ques)):
				tags_ques[i] = ps.stem(tags_ques[i])
			cnt = 0
			for tag in tags_ques:
				if tag not in tags:
					cnt += 1
			temp = len(tags) - len(list(set(tags).intersection(tags_ques)))
			cnt = cnt + (temp - len(tags))
			if cnt < 0:
				ques_id.append(item[u'question_id'])
				ques_score.append(cnt)
				ques_body.append(item[u'title'])
					
	except StackAPIError as e:
		print e.message
	print ques_id[1]
	return ques_id,ques_score,ques_body



		
	
