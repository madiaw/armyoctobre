from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    quantite = models.IntegerField(default=0)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_derniere_revision = models.DateTimeField(null=True, blank=True)
    periode_revision = models.IntegerField(help_text="Période de révision en jours")

    def __str__(self):
        return self.nom

    def est_a_reviser(self):
        if not self.date_derniere_revision:
            return True
        return (timezone.now() - self.date_derniere_revision).days >= self.periode_revision

class Mouvement(models.Model):
    TYPES = (
        ('E', 'Entrée'),
        ('S', 'Sortie'),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPES)
    quantite = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_type_display()} de {self.quantite} {self.article.nom}"