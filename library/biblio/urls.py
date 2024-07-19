from django.urls import path
from .views import *



urlpatterns = [
    path('',index,name='index'),
    path('livres/',livres,name= 'livres'),
    path('modif/',modif,name= 'modif'),
    
    # crud zone
    
    path('delete/<int:id>',delete,name= 'delete'),
    path('update/<int:id>',update,name= 'update'),
    path('add/',add,name= 'add'),

    #zone de filtre

    path('filtre/',filtre,name= 'filtre'),
    path('catego_fil/<str:catego>',catego_fil,name='catego_fil'),
    path('book/<id>',book,name= 'livre'),

    # zone ajout data pour autre table

    path('categorie',categorie,name='categorie'),
    path('auteur',auteur,name='auteur'),
]
