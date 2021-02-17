# I have created this file - Siddhartha
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Siddhartha', 'place':'New York'}
    return render(request,'index.html',params)

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps',' off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"Removing Punctutations", 'analyzed_text':analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Change to upper case", 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': "Removed new line", 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': "Removed extra spaces", 'analyzed_text': analyzed}

    # elif charcount == "on":
    #     analyzed = 0
    #     for i in range(0,len(djtext)):
    #         if (djtext[i] == ' '):
    #             analyzed += 1
    #     params = {'purpose': "Count total characters", 'analyzed_text': analyzed}
    #     #djtext = analyzed
    #     return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please select any appropriate operation and try again")

    return render(request,'analyze.html',params)



