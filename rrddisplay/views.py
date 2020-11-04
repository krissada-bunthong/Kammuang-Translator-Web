from django.shortcuts import render
from django.http import HttpResponse
from pythainlp.corpus.common import thai_words
from pythainlp import word_tokenize

def index(request):
    # return HttpResponse("<h1>H1</h1>")
    return render(request, "rrddisplay/index.html") 

def result(request):
    # text = "ขอน้ำบะดาย อู้บ่าดาย อู้เล่นบะได้ก๋า จะไปบึงกาฬ"
    # list_t = word_tokenize(text,engine='mm')
    return HttpResponse("E %s" %(read_csv()))

def read_csv(request):
    #read csv file
    import csv
    KammuangDB = []
    with open('./KammuangDB.csv','rt')as f:
        data = csv.reader(f)
    for row in data:
      KammuangDB.append(row)
    return KammuangDB

def data_visualization():
    return 0

def tokenize(request):
    import csv
    KammuangDB = list()
    with open('./KammuangDB.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            KammuangDB.append(row)
    # return KammuangDB
    
    from pythainlp.corpus.common import thai_words
    from pythainlp.tokenize import Tokenizer

    text = "ขอน้ำบะดาย อู้บ่าดาย อู้เล่นบะได้ก๋า จะไปบึงกาฬ"
    PATH_TO_CUSTOM_DICTIONARY = './custom_dictionary.txt'
    _tokenizer = Tokenizer(custom_dict=PATH_TO_CUSTOM_DICTIONARY)
    text_af = _tokenizer.word_tokenize(text)
    # return HttpResponse("E %s" %_tokenizer.word_tokenize(text))
    # def index(request):
    # testvar = 'value'
    # return render(request, 'template.html', {'testvar': testvar})
    
    return render(request, "rrddisplay/tokenize.html", {'text':text,'text_af':text_af,'KammuangDB':KammuangDB})