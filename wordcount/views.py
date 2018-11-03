from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	#return HttpResponse("Homepage")
	return render(request, 'homepage.html')

def count(request):
	fulltext = request.GET['fulltext']
	word_list = fulltext.split()

	word_count_dict = {}
	for word in word_list:
		if word in word_count_dict:
			# increase the number
			word_count_dict[word]+=1
		else:
			# add to the dict
			word_count_dict[word]=1

	word_count_dict_sorted = sorted(word_count_dict.items(),key=lambda k:k[1],reverse=True)
	#sorted(word_count_dict.items(),key=operator.itemgetter(1),reverse=True)




	return render(request, 'count.html',{'fulltext':fulltext, \
		'wordcount': len(word_list), 'word_count_dict_sorted':word_count_dict_sorted})


def testpage(request):
	return HttpResponse("Testpage")

def aboutpage(request):
	return render(request,"about.html")