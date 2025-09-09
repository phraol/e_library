from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Book, College, Department
from .forms import BookForm, UserSignupForm

# Landing page
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'books/welcome.html')

# Library home
@login_required
def home(request):
    books = Book.objects.all().order_by('-created_at')
    colleges = College.objects.all()
    return render(request, 'books/home.html', {'books': books, 'colleges': colleges})

# Upload book (admin & librarian only)
@login_required
def upload_book(request):
    if request.user.role not in ['admin', 'librarian']:
        return redirect('home')

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

# User signup (students only by default)
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'  # default role
            user.save()
            login(request, user)  # automatically log in after signup
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'books/signup.html', {'form': form})



# @login_required
# def profile(request):
#     books = Book.objects.filter(uploaded_by=request.user)
#     return render(request, 'users/profile.html', {
#         'user': request.user,
#         'books': books
#     })
