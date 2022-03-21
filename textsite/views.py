# i have creted the file -Ashish
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request ,'index.html')
    
# def about(request):
#     f='''about<br> <a href ='/cntact'>contact</a><br><a href ='/'>index</a> <br>'''
#     return HttpResponse(f)    

def operations(request):

    #getting the text 
    djtext=request.GET.get('text_data','NULL')

    rempuc=request.GET.get('rempuc','rempunc=off')
    capital=request.GET.get('capital','capital=off')
    space=request.GET.get('space','space=off')
    new=request.GET.get('new','new=off')
    
    #performing operatins on text
    
    
    if rempuc=="on":
        analayzed=""
        punctuations ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                if char == '\n':
                    analayzed = analayzed + "\n"
                else:
                    analayzed = analayzed +char
        djtext=analayzed

    if capital =="on":
        analayzed=""
        for char in djtext:
            analayzed = analayzed +char.upper()
        djtext=analayzed
    

    if space =="on":
        analayzed=""
        for index in range(len(djtext)-1): 
            if djtext[index] == " " and djtext[index+1]== " ":
                pass
            else:
                analayzed = analayzed +djtext[index]
        djtext=analayzed

    if new =="on":
        U=djtext
        A=""
    else:
        A=djtext    
        U=""
    count=0
    for char in djtext :
        if char==" ":
            continue
        else:
            count+=1
    c=count
    
    params={'purpose': 'upon performing operations' ,'analyze_txt':A, 'cahrc':c ,"newline" :U }
            
    #analayzing the text
    return render(request ,'analyze.html',params)    