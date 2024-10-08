from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stock.models import Article, Mouvement

@login_required
def dashboard(request):
    articles_a_reviser = Article.objects.filter(est_a_reviser=True)
    stock_faible = Article.objects.filter(quantite__lt=10)
    derniers_mouvements = Mouvement.objects.order_by('-date')[:10]
    
    context = {
        'articles_a_reviser': articles_a_reviser,
        'stock_faible': stock_faible,
        'derniers_mouvements': derniers_mouvements,
    }
    return render(request, 'dashboard/dashboard.html', context)