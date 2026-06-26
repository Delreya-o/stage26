from django.shortcuts import render

def bookstore_view(request):
    return render(request, 'bookstore.html')
