import requests
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

API_URL = "http://localhost:3000/recettes"

def index(request):
    response = requests.get(API_URL)
    listRecette = response.json() if response.status_code == 200 else []

    query_titre = request.GET.get('titre', '').lower()
    query_cat = request.GET.get('categorie', '').lower()
    
    resultats = listRecette

    if query_titre:
        resultats = [r for r in resultats if query_titre in r['titre'].lower()]
    
    if query_cat:
        resultats = [r for r in resultats if query_cat == r['categorie'].lower()]

    return render(request, 'MijotonsApp/index.html', { 'listRecette' : resultats })

def recette(request, id):
    response = requests.get(f"{API_URL}/{id}")
    
    if response.status_code == 200 and response.json():
        return render(request, 'MijotonsApp/recette.html', { 'recette': response.json() })
    else:
        raise Http404("Recette introuvable")

@login_required 
def ajouter(request):
    if request.method == "POST":
        nouvelle = {
            "titre": request.POST.get('titre'),
            "categorie": request.POST.get('categorie'),
            "tempspreparation": int(request.POST.get('temps')),
            "imagpath": "images/image.png"
        }
        requests.post(API_URL, json=nouvelle)
        return redirect('/')
    return render(request, 'MijotonsApp/ajouter.html')

@login_required
def supprimer(request, id):
    requests.delete(f"{API_URL}/{id}")
    return redirect('/')

@login_required
def modifier(request, id):
    if request.method == "POST":
        update = {
            "titre": request.POST.get('titre'),
            "categorie": request.POST.get('categorie'),
            "tempspreparation": int(request.POST.get('temps'))
        }
        requests.put(f"{API_URL}/{id}", json=update)
        return redirect('/')
    
    res = requests.get(f"{API_URL}/{id}")
    return render(request, 'MijotonsApp/modifier.html', {'recette': res.json()})