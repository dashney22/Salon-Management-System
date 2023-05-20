from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .models import Book
from rest_framework import viewsets, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from django.contrib.auth.decorators import login_required


# Create your views here[Function-Based View].
@login_required
def firstFunction(request):
    books = Book.objects.all()
    return render(request,'index.html',{'books': books})

#CLASS based View
'''
class Another(View):
    
    books = Book.objects.all()
    output = f'We only have {books[0].name} and {str(books[1].name)} in our store!'
    def get(self, request):
        return HttpResponse(self.output)
    
### Serializers
class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all() 

@api_view(['GET'])   #GET ALL BOOKS
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])  #UPDATE AN EXISTING BOOK
def book_detail(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])  #CREATE A NEW BOOK
def create_book(request):
    if request.method != 'POST':
        raise MethodNotAllowed(request.method)
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
monthly_chall = {
    "dashney": "Lazy as fuck",
    "felicity": "Acts all holly and shit",
    "retang": "mf wants to be praised all the time",
    "phuti": "Too quiet, why?"
}
def monthly_challenge(request, month):
    try:
        challenge = monthly_chall(month)
        return HttpResponse(challenge)
    except: 
        return HttpResponseNotFound("Month is not cartered in this application")
'''   