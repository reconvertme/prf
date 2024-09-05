from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
# Journal
class Journal(models.Model):

    class Genre(models.TextChoices): # new
        MANAGEMENT = 'MAN'
        HIGH_TECH = 'IT'
        CUISINE = 'CUI'
        
    nom = models.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5) # new
    editeur = models.CharField(max_length=42)
    description = models.TextField(null=True)
    dispo = models.fields.BooleanField(default=True)
    webpage = models.fields.URLField(null=True, blank=True)
    
    dateparution = models.DateTimeField(
        auto_now_add=True, 
        auto_now=False,
        verbose_name="Date de parution"
    )
    
    year_created = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )

    # Bannière
    # banner = models.ImageField(default = 'fallback.png', blank = True, upload_to='images')
    banner = models.ImageField(default = 'fallback.png', blank = True)
    
    def __str__(self):
        return self.nom[:50]


# Article
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    nbpages = models.fields.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(50)]
    )

     # Clé étrangère
    journal = models.ForeignKey(Journal,null=True, on_delete=models.SET_NULL)

    # Afficher le titre de l'article
    def __str__(self):
        return self.titre[:50]

