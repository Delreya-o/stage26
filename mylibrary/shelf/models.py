from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as gettext

import uuid

class Author(models.Model):
    author_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        verbose_name=gettext("Auteur"),
        help_text=gettext("Identifiant de l'auteur"),
        null=False,
        unique=True,
        blank=False,
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
        return f'{self.name} ({self.author_id})'
    
    def get_absolute_url(self):
        """Cette fonction est requise pour détailler le contenu d'un objet."""
        return reverse('author-detail', args=[str(self.author_id)])


class Publisher(models.Model):
    publisher_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        verbose_name=gettext("Maison d'édition"),
        help_text=gettext("Identifiant de la maison d'édition"),
        null=False,
        unique=True,
        blank=False,
    )

    name = models.TextField(
        verbose_name=gettext("Nom"),
        help_text=gettext("Nom de la maison d'édition.e"),
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
        return f'{self.name} ({self.publisher_id})'

    def get_absolute_url(self):
        """Cette fonction est requise pour détailler le contenu d'un objet."""
        return reverse('publisher-detail', args=[str(self.publisher_id)])


class Book(models.Model):
    SERIE_TYPE = (
        ('i', 'inconnu'),
        ('os', 'one-shot'),
        ('s', 'serie'),
        ('hs', 'hors-serie'),
    )

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

    serie_type = models.CharField(
        choices=SERIE_TYPE,
        max_length=2,
        blank=True,
        default='i',
        help_text=gettext('Serie ? One-shot ? Hors-série (/spin-off) ?'),
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
        help_text=gettext("Identifiant de la maison d'édition"),
        null=True
    )

    year_pub = models.IntegerField(
        verbose_name=gettext("Année"),
        help_text=gettext("Année de publication"),
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
        return f'{self.title} - {self.year_pub} ({self.isbn})'

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
        help_text='ID unique pour ce livre',
        null=False,
        unique=True,
        blank=False,
    )
    
    book = models.ForeignKey('Book',
        on_delete=models.SET_NULL,
        null=True
    )
    
    tome_nb = models.IntegerField(
        blank=True,
        verbose_name=gettext("Tome n°"),
        help_text=gettext('Numéro du tome'),
    )

    status = models.CharField(
        choices=READ_STATUS,
        max_length=1,        
        blank=True,
        default='u',
        help_text='statut',
    )

    class Meta:
        ordering = ['book', 'tome_nb']

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets Book dans la base de données."""
        return f' {self.book.title} - tome {self.tome_nb} [{self.status}] ({self.id})'

