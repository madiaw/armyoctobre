from django import forms
from .models import Article, Mouvement

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom', 'description', 'quantite', 'categorie', 'periode_revision']

class MouvementForm(forms.ModelForm):
    class Meta:
        model = Mouvement
        fields = ['article', 'type', 'quantite', 'commentaire']