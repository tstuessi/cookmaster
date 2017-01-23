# Views page for overall site

# right now I want the index to redirect to the 
# recipe api page

import django.shortcuts

def index(request):
    return django.shortcuts.redirect('recipe index')
