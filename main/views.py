from django.shortcuts import get_object_or_404, render
from main import models
# Create your views here.
def create_author(request):
    context={}
    if(request.method=="POST"):
        author_data={
            "name":request.POST['name']
        }
        author=models.Author.objects.create(**author_data)
        context["success"]=True
    return render(request,'main/create_author.html',context)
def create_article(request):
    authors=models.Author.objects.all()
    context={
        "authors":authors
    }
    if request.method=="POST" :
        article_data={
            "name":request.POST['name'],
            "content":request.POST['content']
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(pk=request.POST['author'])
        article.authors.set(author)
        context["success"]=True
    return render(request,'main/create_article.html',context)

def author(request,pk):
    authors=get_object_or_404(models.Author,pk=pk)
    context={
        "authors":authors
    }
    return render(request,'main/author.html',context)
    
def article(request,pk):
    article=get_object_or_404(models.Article,pk=pk)
    context={
        "article":article
    }
    return render(request,'main/article.html',context)

def index(request):
    authors=models.Author.objects.all()
    articles=models.Article.objects.all()
    context={
        "articles":articles,
        "authors":authors
    }
    return render(request,'main/index.html',context)
