from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Mouvement
from .forms import ArticleForm, MouvementForm

@login_required
def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'stock/liste_articles.html', {'articles': articles})

@login_required
def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    mouvements = Mouvement.objects.filter(article=article).order_by('-date')
    return render(request, 'stock/detail_article.html', {'article': article, 'mouvements': mouvements})

@login_required
def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'stock/formulaire_article.html', {'form': form})

@login_required
def modifier_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('detail_article', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'stock/formulaire_article.html', {'form': form})

@login_required
def ajouter_mouvement(request):
    if request.method == 'POST':
        form = MouvementForm(request.POST)
        if form.is_valid():
            mouvement = form.save()
            article = mouvement.article
            if mouvement.type == 'E':
                article.quantite += mouvement.quantite
            else:
                article.quantite -= mouvement.quantite
            article.save()
            return redirect('detail_article', pk=article.pk)
    else:
        form = MouvementForm()
    return render(request, 'stock/formulaire_mouvement.html', {'form': form})