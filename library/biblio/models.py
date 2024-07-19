from django.db import models

class Auteur(models.Model):
    nom_auteur = models.CharField(max_length=100,null=True)
    prof_auteur = models.CharField(max_length=100,null=True)
    genre = [('M','homme'),('F','femme')]
    sexe_auteur = models.CharField(max_length=1,choices= genre,default='M')

    def __str__(self):
        return self.nom_auteur
    

class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nom_categorie

class Livre(models.Model):
    titre_livre =  models.CharField(max_length=100,null=True)
    categorie_livre = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    date_creation_livre = models.DateField(auto_now=True)
    fichier_livre = models.FileField(upload_to='media/image',null=True)
    description = models.TextField(max_length=1200)
    image = models.ImageField(upload_to='media/image',null=True)
    auteur_livre = models.ForeignKey(Auteur,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.titre_livre
    