from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

def welcome(request):
    return render(request, 'books/welcome.html')  # landing page

@login_required
def home(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'books/home.html', {'books': books})

@login_required
def upload_book(request):
    if request.user.role not in ['admin', 'librarian']:
        return redirect('home')  # students cannot upload

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user
            book.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'books/upload_book.html', {'form': form})

