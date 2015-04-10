from django.contrib import admin
from blog.models import Article, Categorie, Commentaire
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class ArticleAdmin(MarkdownModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ('titre', 'contenu',)
    list_filter = ['date_de_parution']
    search_fields = ['titre']
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    readonly_fields = ('date_de_parution',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Commentaire)