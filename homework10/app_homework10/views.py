from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


from .forms import AuthorForm, QuoteForm
from .models import Author, Quote


# Create your views here.
def main(request):
    return render(request, 'app_homework10/index.html', context={"title": "Homework 10"})


@login_required
def author_add(request):
    form = AuthorForm(instance=Author())
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=Author())
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            author_name = form.cleaned_data["fullname"]
            messages.success(request, f'Congrats new Author {author_name} was added!')
            return redirect(to="app_homework10:authors")
    return render(request, 'app_homework10/author_add.html', context={"title": "Homework 10", "form": form})


@login_required
def quote_add(request):
    form = QuoteForm(instance=Quote())
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES, instance=Quote())
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            messages.success(request, f'Congrats new Quote was added!')
            return redirect(to="app_homework10:quotes")
    return render(request, 'app_homework10/quote_add.html', context={"title": "Homework 10", "form": form})


def quotes(request):
    quotes_all = Quote.objects.filter().all()
    return render(request, 'app_homework10/quote.html',
                  context={"title": "Homework 10", "quotes": quotes_all, "media": settings.MEDIA_URL})


def authors(request):
    authors_all = Author.objects.filter().all()
    return render(request, 'app_homework10/author.html',
                  context={"title": "Homework 10", "authors": authors_all, "media": settings.MEDIA_URL})


def author_card(request, author_id):
    author = Author.objects.filter(pk=author_id).all()
    return render(request, 'app_homework10/author.html',
                  context={"title": "Homework 10", "authors": author, "media": settings.MEDIA_URL})
