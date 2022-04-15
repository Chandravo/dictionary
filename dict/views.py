from django.shortcuts import render
import json
import urllib.request
import requests
# Create your views here.
def index(request):
    if request.method=="POST":
        word=request.POST['word']
        url="https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        # r=requests.get(url=url)
        # res=r.json()
        r=urllib.request.urlopen(url).read()
        res=json.loads(r.decode('utf-8'))
        dictt=res[0]
        
        data={
            'word':str(dictt['word']),
            'Phonetics':str(dictt['phonetics'][-1]['text']),
            'def':dictt['meanings']
            
        }
    else:
        data={}
    
    
    return render(request,'index.html',{'data':data})