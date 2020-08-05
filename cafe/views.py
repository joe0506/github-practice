from django.shortcuts import render

def one(request):
    return render(request, 'one.html')

def ok(request):
    return render(request, 'ok.html')

def two(request):
    wordcount=request.GET['wordcount']
    count=wordcount.count(' ')+1
    return render(request, 'two.html', {'text':wordcount, 'count':count})
# Create your views here.
