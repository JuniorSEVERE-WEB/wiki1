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
    
    # Si l'entrée n'existe pas, afficher la page d'erreur
    return render(request, "encyclopedia/error.html", {
        "title": query
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

