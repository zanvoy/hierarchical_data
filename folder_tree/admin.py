from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from folder_tree.models import FolderTree
# Register your models here.
admin.site.register(FolderTree, DraggableMPTTAdmin)