from django.contrib import admin
from .models import Journal, Article

# On veut afficher plus de colonnes
class JournalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'editeur', 'description')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'nbpages') 

# Register your models here.
admin.site.register(Journal, JournalAdmin)
admin.site.register(Article, ArticleAdmin)
