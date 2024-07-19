from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

from .forms import *




livre = Livre.objects.all()

categorie = Categorie.objects.all()

auteur = Auteur.objects.all()

def index(request):
    categorie = Categorie.objects.all()
  
    context = {
        'livre':livre,
        'categorie':categorie
    }
  
    return render(request,'index.html',context)

def livres(request):
    categorie = Categorie.objects.all()
    livre = Livre.objects.all()
    
    context = {
        'livre':livre,
        'categorie':categorie
    }
    
    return render(request,'livres.html',context)


def modif(request):
    categorie = Categorie.objects.all()
    
    context ={
        'livre':livre,
        'categorie':categorie
    }

    return render(request,'modif.html',context)

#zone de filtrage(recherche)

def filtre(request):
    categorie = Categorie.objects.all()
    if request.method == 'GET':
    
        liv = request.GET['search1']
        
        livre = Livre.objects.filter(
                Q(titre_livre__icontains = liv)|
                Q(categorie_livre__nom_categorie__icontains = liv)|
                Q(auteur_livre__nom_auteur__icontains = liv)
            )

        conteur = livre.count()
        
        if conteur > 0:

            context = {
            'livre':livre,
            'categorie':categorie,
            'conteur':conteur
            }
        
        context =  {
            'livre':livre,
            'livres':livres,
            'categorie':categorie,
            'conteur':conteur
        }

    return render(request,'filtre.html',context)

def catego_fil(request, catego):
    categorie = Categorie.objects.all()
    categorie_id = Categorie.objects.get(nom_categorie = catego)
    
    livre = Livre.objects.filter(categorie_livre = categorie_id)
    
    conteur = livre.count()
        
    if conteur > 0:

        context = {
            'livre':livre,
            'categorie':categorie,
            'conteur':conteur
            }
        
    context =  {
            'livre':livre,
            'categorie':categorie,
            'conteur':conteur
        }

    return render(request, 'catego_fil.html', context)


def book(request,id):
    categorie = Categorie.objects.all()
    livre = Livre.objects.filter(id = id)
    
    livre_s = Livre.objects.all()
    
    context = {
        'livre': livre,
        'categorie': categorie,
        'livre_s': livre_s
    }
    
    return render(request, 'livre.html', context)


# creation du crud


def delete(request,id):
    categorie = Categorie.objects.all()
    delete_id = Livre.objects.get(id = id)
    delete_id.delete()
    
    return redirect('livres')


def update(request,id):
    Livre.objects.all().order_by('-id')
    modif = Livre.objects.get(id=id)
    form = LivreForm(instance=modif)
    if request.method == 'POST':
        form = LivreForm(request.POST or None,request.FILES or None,instance=modif)
        if form.is_valid:
            form.save()

        return redirect('livres')

    else:
        form = LivreForm()
    context = {
            'livre':livre,
            'modif':modif,
            'categorie':categorie,
            'auteur':auteur,
            'form':form
            }
    return render(request,'edit.html',context)


def add(request):
    categorie = Categorie.objects.all()
    livre = Livre.objects.all()

    if request.method == "POST":
        form = LivreForm(request.POST or None,request.FILES or None)
        if form.is_valid:
            form.save()

        return redirect('livres')

    else:
        form = LivreForm()

    context = {
            'livre':livre,
            'categorie':categorie,
            'auteur':auteur,
            'form':form
        }

    return render(request,'add.html',context,)




def categorie(request):
    categorie = Categorie.objects.all()
    if request.method =="POST":
        form = CategoForm(request.POST or None)
        if form.is_valid:
            form.save()

        return redirect('modif')
    else:
         form = CategoForm()
    context = {
            'livre':livre,
            'categorie':categorie,
            'form':form
            }

    return render(request,'categorie.html',context)

def auteur(request):
    categorie = Categorie.objects.all()
    if request.method =="POST":
        form = AuteurForm(request.POST or None)
        if form.is_valid:
            form.save()

        return redirect('modif')
    else:
         form = AuteurForm()
    context = {
            'livre':livre,
            'categorie':categorie,
            'form':form
            }
    return render(request,'auteur.html',context)