
from django.shortcuts import render, HttpResponse
from datetime import datetime


def index(request):
    return render(request,'index.html')

def removepunc(request):
    # get text data
    text_data = request.POST.get('text','default')

    # get checkbox value
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    both = request.POST.get('both','off')

    analyse=""
    punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if removepunc == "on":
        for char in text_data:
            if char not in punc:
                analyse= analyse + char
        result={'punc_remo':analyse}
        return render(request,'removepunc.html',result)

    elif uppercase == "on":
        for char in text_data:
            if char in text_data:
                analyse = analyse + char.upper()
        result = {'punc_remo':analyse}
        return render(request,'removepunc.html',result)

    elif both == "on":
        for char in text_data:
            #check for given text don't have punctuation mark ,newline char and captlize it..
            if char not in punc and char !="\n":
                analyse = analyse + char.upper() #captlize full string

        # write given data in next file
        file_write=open('text.txt','a')
        cap_first = analyse.title()
        file_write.write(cap_first)
        file_write.close()

        result = {'punc_remo':cap_first}
        return render(request,'removepunc.html',result)

    else:
        return HttpResponse("Error!!!")
