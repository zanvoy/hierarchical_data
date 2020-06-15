from django.shortcuts import render
from folder_tree.models import FolderTree

# Create your views here.
def index(request):
    data = {'FolderTree': FolderTree.objects.all()}
    return render(request, 'index.html',data)