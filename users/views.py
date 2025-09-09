from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from books.models import Book


# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'  # default role for new signups
            user.save()
            login(request, user)   # log in immediately after signup
            return redirect('home')  # send them to home after signup
    else:
        form = SignUpForm()
    return render(request, 'books/signup.html', {'form': form})


# Profile view
@login_required
def profile(request):
    """
    Show user profile details and their uploaded books.
    """
    books = Book.objects.filter(uploaded_by=request.user)
    return render(request, 'users/profile.html', {
        'user': request.user,
        'books': books
    })
