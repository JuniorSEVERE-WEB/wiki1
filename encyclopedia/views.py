from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

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


def create_page(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        if not title:
            messages.error(request, "Title is required.")
            return render(request, "encyclopedia/create.html", {
                'content': content
            })
        
        if not content:
            messages.error(request, "Content is required.")
            return render(request, "encyclopedia/create.html", {
                'title': title
            })
        
        # Vérifier si l'entrée existe déjà
        if util.get_entry(title) is not None:
            messages.error(request, f"An encyclopedia entry with the title '{title}' already exists.")
            return render(request, "encyclopedia/create.html", {
                'title': title,
                'content': content
            })
        
        # Sauvegarder la nouvelle entrée
        util.save_entry(title, content)
        messages.success(request, f"Encyclopedia entry '{title}' has been created successfully!")
        
        # Rediriger vers la nouvelle page créée
        return redirect('entry', title=title)
    
    # GET request - afficher le formulaire vide
    return render(request, "encyclopedia/create.html")


def edit_page(request, title):
    # Vérifier que l'entrée existe
    existing_content = util.get_entry(title)
    if existing_content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    
    if request.method == "POST":
        content = request.POST.get('content', '').strip()
        
        if not content:
            messages.error(request, "Content is required.")
            return render(request, "encyclopedia/edit.html", {
                'title': title,
                'content': existing_content
            })
        
        # Sauvegarder le contenu modifié
        util.save_entry(title, content)
        messages.success(request, f"Encyclopedia entry '{title}' has been updated successfully!")
        
        # Rediriger vers la page de l'entrée
        return redirect('entry', title=title)
    
    # GET request - afficher le formulaire avec le contenu existant
    return render(request, "encyclopedia/edit.html", {
        'title': title,
        'content': existing_content
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

