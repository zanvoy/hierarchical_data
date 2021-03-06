# Generated by Django 3.0.7 on 2020-06-15 22:39

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('folder_tree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foldertree',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, limit_choices_to={'self.is_file': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='folder_tree.FolderTree'),
        ),
    ]
