from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class FolderTree(MPTTModel):
    is_file = models.BooleanField(default=False)
    name = models.CharField(max_length=40, unique=True)
    parent = TreeForeignKey('self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        limit_choices_to={'is_file': False})
    
    class MPTTMeta():
        order_insertion_by = ['name']

    def __str__(self):
        return self.name