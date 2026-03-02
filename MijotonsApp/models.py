from django.db import models

# Create your models here.

class Recette(models.Model):
    titre = models.CharField(max_length=60)
    categorie = models.CharField(max_length=60)
    tempspreparation = models.IntegerField()
    imagpath = models.TextField(max_length=300)

    def __str__(self):
        return self.titre