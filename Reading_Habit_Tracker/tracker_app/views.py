from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.utils import timezone
from datetime import datetime
from calendar import month_name

def home(request):
    currently_reading = Book.objects.filter(status='READING').count()
    total_completed = Book.objects.filter(status='DONE').count()
    
    # Get books read this month
    current_month = timezone.now().month
    current_month_name = month_name[current_month]
    books_this_month = Book.objects.filter(
        status='DONE', 
        date_added__month=current_month
    ).count()
    
    context = {
        'currently_reading': currently_reading,
        'total_completed': total_completed,
        'books_this_month': books_this_month,
        'current_month_name': current_month_name,
        'tech_books': Book.objects.filter(category='TECH').order_by('-date_added')[:5],
        'novels': Book.objects.filter(category='NOVEL').order_by('-date_added')[:5],
    }
    return render(request, 'index.html', context)

def current_books(request):
    books = Book.objects.filter(status='READING').order_by('-date_added')
    return render(request, 'current_books.html', {'books': books})

def tech_books(request):
    books = Book.objects.filter(category='TECH').order_by('-date_added')
    return render(request, 'tech_books.html', {'books': books})

def novel_books(request):
    books = Book.objects.filter(category='NOVEL').order_by('-date_added')
    return render(request, 'novel_books.html', {'books': books})

def update_book_status(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Book.STATUS_CHOICES):
            book.status = new_status
            book.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def add_tech_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        if name:
            Book.objects.create(
                name=name,
                category='TECH',
                status=status
            )
            return redirect('tech_books')
    return render(request, 'book_form.html', {'category': 'TECH'})

def add_novel_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        if name:
            Book.objects.create(
                name=name,
                category='NOVEL',
                status=status
            )
            return redirect('novel_books')
    return render(request, 'book_form.html', {'category': 'NOVEL'})