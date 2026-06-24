from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as gettext

import uuid

class Author(models.Model):
    author_id = models.IntegerField(
        primary_key=True,
        verbose_name=gettext("Auteur"),
        help_text=gettext("Identifiant de l'auteur"),
        null=False
    )

    name = models.TextField(
        verbose_name=gettext("Nom"),
        help_text=gettext("Nom de l'auteur.e"),
        max_length=100,
        null=True
    )

    class Meta:
        """Métadonnées du modèle."""

        verbose_name = gettext("auteur.e")
        verbose_name_plural = gettext("auteur.es")

        ordering = ['name','author_id']

    def __str__(self) -> str:
        """Représentation de l'objet."""
        return self.author_id
    
    def get_absolute_url(self):
        """Cette fonction est requise pour détailler le contenu d'un objet."""
        return reverse('author-detail', args=[str(self.author_id)])


class Publisher(models.Model):
    publisher_id = models.IntegerField(
        primary_key=True,
        verbose_name=gettext("Auteur"),
        help_text=gettext("Identifiant de l'auteur"),
        null=False
    )

    name = models.TextField(
        verbose_name=gettext("Nom"),
        help_text=gettext("Nom de l'auteur.e"),
        # min_length=2,
        max_length=100,
        null=True
    )

    class Meta:
        """Métadonnées du modèle."""

        verbose_name = gettext("Maison d'édition")
        verbose_name_plural = gettext("Maisons d'édition")

        ordering = ['name','publisher_id']

    def __str__(self) -> str:
        """Représentation de l'objet."""
        return self.publisher_id

    def get_absolute_url(self):
        """Cette fonction est requise pour détailler le contenu d'un objet."""
        return reverse('publisher-detail', args=[str(self.publisher_id)])


class Book(models.Model):
    isbn = models.CharField(
        primary_key=True,
        verbose_name=gettext("ISBN"),
        help_text=gettext("Code ISBN du livre"),
        max_length=20,
        unique=True,
    )

    title = models.TextField(
        verbose_name=gettext("Titre"),
        help_text=gettext("Titre du livre"),
        max_length=100,
        unique=True,
    )

    author_id = models.ForeignKey(
        to = "Author",
        on_delete=models.SET_NULL,
        verbose_name=gettext("Auteur"),
        help_text=gettext("Identifiant de l'auteur"),
        null=True
    )

    publisher_id = models.ForeignKey(
        to = "Publisher",
        on_delete=models.SET_NULL,
        verbose_name=gettext("Maison d'édition"),
        help_text=gettext("Identifiant de la Maison d'édition"),
        null=True
    )

    year_pub = models.IntegerField(
        verbose_name=gettext("Année"),
        help_text=gettext("Année de publication"),
        # min_length=4,
        max_length=4,
        null=True
    )

    description = models.TextField(
        verbose_name=gettext("Description"),
        help_text=gettext("Description ou résumé du livre"),
        blank=True,
        null=True
    )

    class Meta:
        """Métadonnées du modèle."""

        verbose_name = gettext("livre")
        verbose_name_plural = gettext("livres")

        ordering = ['title','-year_pub']

    def __str__(self) -> str:
        """Représentation de l'objet."""
        return self.isbn

    def natural_key(self) -> tuple[str]:
        """Renvoie la clé naturelle de l'objet."""
        return (self.isbn)

    def get_absolute_url(self):
        """Cette fonction est requise pour détailler le contenu d'un objet."""
        return reverse('book-detail', args=[str(self.isbn)])

class BookInstance(models.Model):
    """Cet objet permet de modéliser les copies d'un ouvrage (i.e. qui peut être emprunté)."""
    
    READ_STATUS = (
        ('i', 'Inconnu'),
        ('l', 'Lu'),
        ('c', 'En cours'),
        ('p', 'Pause'),
        ('n', 'Pile à Lire'), #pour 'next'
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='ID unique pour ce livre'
    )
    book = models.ForeignKey('Book',
        on_delete=models.SET_NULL,
        null=True
    )
    imprint = models.CharField( max_length=200 )

    due_back = models.DateField(null=True, blank=True )

    status = models.CharField(
        max_length=1,
        choices=READ_STATUS,
        blank=True,
        default='u',
        help_text='statut',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets Book dans la base de données."""
        return f'{self.id} ({self.book.title})'

