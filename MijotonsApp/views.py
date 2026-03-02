from django.shortcuts import render

# Create your views here.

listRecette = [
    { 'id': 1, 'titre': 'recette 1', 'categorie': 'plat', 'tempspreparation': 10, 'imagpath': 'images/image.png' },
    { 'id': 2, 'titre': 'recette 2', 'categorie': 'plat', 'tempspreparation': 20, 'imagpath': 'images/image.png' },
    { 'id': 3, 'titre': 'recette 3', 'categorie': 'dessert', 'tempspreparation': 80, 'imagpath': 'images/image.png' },
    { 'id': 4, 'titre': 'recette 4', 'categorie': 'cocktail', 'tempspreparation': 30, 'imagpath': 'images/image.png' },
]
 
def index(request):
    query_titre = request.GET.get('titre', '').lower()
    query_cat = request.GET.get('categorie', '').lower()
    
    resultats = listRecette

    if query_titre:
        resultats = [r for r in resultats if query_titre in r['titre'].lower()]
    
    if query_cat:
        resultats = [r for r in resultats if query_cat == r['categorie'].lower()]

    context = { 'listRecette' : resultats }
    return render(request, 'MijotonsApp/index.html', context)
 
def recette(request, id):
    recette_trouvee = next((r for r in listRecette if r['id'] == id), None)
    
    if recette_trouvee:
        context = { 'recette': recette_trouvee }
        return render(request, 'MijotonsApp/recette.html', context)
    else:
        from django.http import Http404
        raise Http404("Recette introuvable")
 