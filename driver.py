from answer import get_answers
from stack import identify_questions
from topic import *

d1 = "An array is a group of variables (called elements or components) containing values that all have the same type"
d2 = "Arrays are objects, so they're considered reference types."
d3 = "As you'll soon see, what we typically think of as an array is actually a reference to an array object in memory."
d4 = "The elements of an array can be either primitive types or reference types (including arrays, as we'll see in Section 7.9)."
d5 = "To refer to a particular element in an array,we specify the name of the reference to the array and the position number of the element in the array."
#########################################################################################################
doc = [d1,d2,d3,d4,d5]

topic_list = extract_topic(doc)
topic_list.append(global_tag)
ques_id,ques_score,ques_body = identify_questions(topic_list)
answers_body = get_answers(ques_id)
for i in range(len(ques_id)):
	print ques_body[i]
	print answers_body[i]
	print "_" * 80
