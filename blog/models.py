from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Categorie(models.Model):
    nom = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.nom


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(ouvert=True)


class Article(models.Model):
    titre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    categorie = models.ManyToManyField(Categorie)
    ouvert = models.BooleanField(default=True)
    date_de_parution = models.DateTimeField(auto_now_add=True)
    date_de_modification = models.DateTimeField(auto_now=True)
    contenu = models.TextField()

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-date_de_parution"]


class Commentaire(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.TextField()
    article = models.ForeignKey(Article)
    utilisateur = models.ForeignKey(User)
    date_de_parution = models.DateTimeField(auto_now_add=True)
    date_de_modification = models.DateTimeField(auto_now=True)