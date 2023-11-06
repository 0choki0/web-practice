from django.shortcuts import render , redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터를 저장 

    # ======
    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 사용자가 입력한 데이터를 저장

    # 1. POST 요청
    if request.method == 'POST':
        # 2. 사용자가 입력한 정보를 담아서 form을 생성
        form = ArticleForm(request.POST)
        # 3. 입력된 정보가 올바른지 판단
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    # 1. GET 요청
    else:
        # 2. 비어있는 form을 만들어서
        form = ArticleForm()

    # 3 or 4. context dict에 담고
    context = {
        'form': form,
    }
    # form.html을 rendering
    return render(request, 'form.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)

        context = {
            'form': form,
        }
    
    return render(request, 'form.html', context)