# Generated by Django 4.1 on 2022-08-08 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('resume', models.CharField(blank=True, max_length=200, null=True, verbose_name='Resume')),
                ('description', django_quill.fields.QuillField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles_images', verbose_name='Image')),
                ('statut', models.BooleanField(default=False, verbose_name='Statut')),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_user', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCategorie',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('nom_categorie', models.CharField(max_length=100, verbose_name='Libelle')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Categorie des Articles',
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('contenu', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_blog_comment', to='blog.article')),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_user_comment', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_categorie', to='blog.articlecategorie', verbose_name='Categorie'),
        ),
    ]
