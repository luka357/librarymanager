from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})

def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'authors/author_add.html', {'form': form})

def author_update(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/author_update.html', {'form': form})

def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'authors/author_delete.html', {'author': author})