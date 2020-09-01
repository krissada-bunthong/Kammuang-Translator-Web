from django.shortcuts import render
from django.http import HttpResponse
from pythainlp.corpus.common import thai_words
from pythainlp import word_tokenize

def index(request):
    return HttpResponse("<h1>H1</h1>")

def result(request):
    text = "ขอน้ำบะดาย อู้บ่าดาย อู้เล่นบะได้ก๋า จะไปบึงกาฬ"
    list_t = word_tokenize(text,engine='mm')
    return HttpResponse("E %s" %(read_csv()))

def read_csv():
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