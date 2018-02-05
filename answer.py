from stackapi import StackAPI,StackAPIError
from bs4 import BeautifulSoup

def get_answers(ques_id):
	answers_id = []
	answers_body = []
	try:
		SITE = StackAPI('stackoverflow')
		SITE.page_size = 10
		SITE.max_pages = 5
		for item in ques_id:
			answers = SITE.fetch('questions/{}/answers'.format(item) ,page = 1,pagesize = 1,order = 'desc',sort ='votes',filter = 'withbody')
			answers_id.append(answers[u'items'][0][u"answer_id"])
			answers_body.append(BeautifulSoup(answers[u'items'][0][u"body"], "lxml").text)
		
	except StackAPIError as e:
		print e.message
	return answers_body

