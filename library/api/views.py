
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookissue.models import Book, BookIssue
from .serializers import BookIssueSerialiaer, memberSerializer
from .serializers import BookSerializer
from libmembership.models import member
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView






# @api_view(['GET'])
# def memberList(request):




#@api_view(['POST'])
class Member(APIView):
    def get(self,request):
        member_list = member.objects.all()
        serializer = memberSerializer(member_list, many=True)
        return Response(serializer.data)

    def post(request):
        serializer = memberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class findMember(APIView):
    def get(self,request):






        
    


@api_view(['POST'])
def addMember(request):
    serializer = memberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getBookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# (def addBook(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['PUT'])
def issue(request):
    serializer = BookIssueSerialiaer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        _book = Book.objects.get(name=serializer.data['bookName'])
        _book.avl = False
        _book.issued_to = serializer.data['reader_id']
        _book.save()
        serializer2 = BookSerializer(_book)
        return Response(serializer2.data)

from bookissue.forms import NameForm, addBookForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/book/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


class ProileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_detail.html'

    def get(self, request, pk):
        temp_book = get_object_or_404(Book,  pk=pk)
        serializer = BookSerializer(temp_book)
        return Response({'serializer': serializer, 'temp_book': temp_book})
    
    def post(self, request, pk):
        temp_book = get_object_or_404(Book, pk=pk)
        serializer =  BookSerializer(temp_book, data=request.data)
        if not serializer.is_valid():

            return Response({'serializer': serializer, 'temp_book': temp_book})
        serializer.save()
        return redirect('book/list/')

class addBook(APIView):
    def get(self,request):
        form = addBookForm()
        return render(request, 'name.html', {'form':form})
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('/book/list/')
class findMember(APIView):
    def get(self,request):
        
    




