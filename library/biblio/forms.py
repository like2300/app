from .models import *
from django.forms import ModelForm

class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = ('__all__')
        





class AuteurForm(ModelForm):
    class Meta:
        model = Auteur
        fields = ('__all__')
        
        




class CategoForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ('__all__')
        
        
                
        
        
        
#bourase soraya
# 15 rue didero 115 reins code postale 5151
     

