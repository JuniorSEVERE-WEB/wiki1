from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def markdown_to_html(text):
    """
    Convertit le texte Markdown en HTML avec un parseur custom utilisant des regex
    Supporte: headers (h1-h6), gras, italique, liens, listes non ordonnées, paragraphes
    """
    if not text:
        return ""
    
    html = text
    
    # 1. Headers (# ## ### #### ##### ######)
    html = re.sub(r'^#{6}\s+(.+)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^#{5}\s+(.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^#{4}\s+(.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^#{3}\s+(.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#{2}\s+(.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^#{1}\s+(.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # 2. Gras (**texte** ou __texte__)
    html = re.sub(r'\*\*([^\*\n]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'__([^_\n]+)__', r'<strong>\1</strong>', html)
    
    # 3. Italique (*texte* ou _texte_)
    html = re.sub(r'\*([^\*\n]+)\*', r'<em>\1</em>', html)
    html = re.sub(r'_([^_\n]+)_', r'<em>\1</em>', html)
    
    # 4. Liens [texte](url)
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)
    
    # 5. Code inline `code`
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # 6. Listes non ordonnées (- item ou * item)
    lines = html.split('\n')
    processed_lines = []
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        
        # Début d'item de liste
        if re.match(r'^[-\*]\s+(.+)', stripped):
            if not in_list:
                processed_lines.append('<ul>')
                in_list = True
            # Extraire le contenu de l'item
            item_content = re.sub(r'^[-\*]\s+(.+)', r'\1', stripped)
            processed_lines.append(f'<li>{item_content}</li>')
        else:
            # Fin de liste si on était dans une liste
            if in_list:
                processed_lines.append('</ul>')
                in_list = False
            processed_lines.append(line)
    
    # Fermer la liste si on termine par une liste
    if in_list:
        processed_lines.append('</ul>')
    
    html = '\n'.join(processed_lines)
    
    # 7. Paragraphes (lignes séparées par des lignes vides)
    # Diviser en blocs séparés par des lignes vides
    blocks = re.split(r'\n\s*\n', html)
    processed_blocks = []
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        # Ne pas wrapper les blocs qui sont déjà des éléments HTML
        if not (block.startswith('<') and block.endswith('>')):
            # Vérifier si c'est un header, une liste, etc.
            if not re.match(r'^<(h[1-6]|ul|ol|li)', block):
                # C'est un paragraphe normal
                processed_blocks.append(f'<p>{block}</p>')
            else:
                processed_blocks.append(block)
        else:
            processed_blocks.append(block)
    
    html = '\n\n'.join(processed_blocks)
    
    return mark_safe(html)


# Alias pour compatibilité et utilisation avec |safe
@register.filter
def custom_markdown(text):
    """
    Alias du parseur Markdown custom - utilise |safe automatiquement
    """
    return markdown_to_html(text)