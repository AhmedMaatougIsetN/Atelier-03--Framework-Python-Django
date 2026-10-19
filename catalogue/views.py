from django.shortcuts import get_object_or_404, render

from .models import Author, Book, Category


def livre_list(request):
    """Show books priced below 50 TND, newest publication first."""
    livres = (
        Book.objects.filter(price__lt=50)
        .order_by("-publication_date", "title")
    )
    return render(
        request,
        "catalogue/livre_list.html",
        {"livres": livres, "titre_page": "Catalogue des livres"},
    )


def livre_detail(request, pk):
    livre = get_object_or_404(Book, pk=pk)
    return render(request, "catalogue/livre_detail.html", {"livre": livre})


def auteur_list(request):
    auteurs = Author.objects.all().order_by("last_name", "first_name")
    return render(request, "catalogue/auteur_list.html", {"auteurs": auteurs})


def auteur_detail(request, pk):
    auteur = get_object_or_404(Author, pk=pk)
    livres = auteur.books.all().order_by("title")
    return render(
        request,
        "catalogue/auteur_detail.html",
        {"auteur": auteur, "livres": livres, "nombre_livres": livres.count()},
    )


def categorie_list(request):
    categories = Category.objects.all().order_by("name")
    return render(
        request, "catalogue/categorie_list.html", {"categories": categories}
    )
