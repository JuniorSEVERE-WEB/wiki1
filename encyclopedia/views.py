from django.shortcuts import render, redirect
from django.http import Http404

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    query = request.GET.get('q', '').strip()
    
    if not query:
        return redirect('index')
    
    # Vérifier si l'entrée existe exactement
    content = util.get_entry(query)
    if content is not None:
        # Rediriger vers la page de l'entrée si elle existe
        return redirect('entry', title=query)
    
    # Recherche par sous-chaîne si pas de correspondance exacte
    all_entries = util.list_entries()
    matching_entries = []
    
    for entry in all_entries:
        if query.lower() in entry.lower():
            matching_entries.append(entry)
    
    # Afficher les résultats de recherche
    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "entries": matching_entries
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

