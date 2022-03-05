from asyncio.windows_events import NULL
import json
from msilib.schema import Error
from django.contrib import messages
from telnetlib import STATUS
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,MyBook
from django.contrib.auth.decorators import login_required

# books = [   {
#         'BookTitle':'Pride and Prejudice',
#         'Author':'Jane Austen, Anna Quindlen',
#         'Publisher':'T. Egerton, Whitehall',
#         'Genre':'Romance',
#         'Year':'1813',
#         'Language':'English',
#         'Description':'The Pride of Jane Austen! The story is set in England in the late 18th century. Charles Bingley, a wealthy and charismatic single man, moves to the Netherfield estate, and when he does, the residents there are very thrilled',
#         'Tags':['Romance','Fiction'],
#         'ISBN':'9780140430721'
#     },
#     {
#         'BookTitle':'In Search of Lost Time',
#         'Author':'Marcel Proust',
#         'Publisher':'Grasset and Gallimard',
#         'Genre':'Modernist',
#         'Year':'1913',
#         'Language':'English',
#         'Description':'In Search of Lost Time follows the narrators recollections of childhood and experiences into adulthood in the late 19th-century and early 20th-century high-society France',
#         'Tags':['French','Historic'],
#         'ISBN':'9780099362210'
#     },
#     {
#         'BookTitle':'To Kill a Mockingbird',
#         'BookTitle':'To Kill a Mockingbird',
#         'Author':'Harper Lee',
#         'Publisher':'J. B. Lippincott & Co.',
#         'Genre':'Southern Gothic',
#         'Year':'1960',
#         'Language':'English',
#         'Description':'To Kill a Mockingbird takes place in the fictional town of Maycomb, Alabama, during the Great Depression.',
#         'Tags':['Bildungsroman','Legal'],
#         'ISBN':'9782253115847'
#     }
# ]


@login_required
def booklist(request):
    context ={
        'books':Book.objects.all()
    }
    return render(request, 'Library/booklist.html', context)




@login_required
def IssueBook(request):


    if  MyBook.objects.filter(user=request.user).count()>=1:
        
        response = HttpResponse(json.dumps({'msg': f'You cant issue more books. Please return previous books'}), 
        content_type='application/json')
        response.status_code=400
        return response
        
    else:

        book = request.POST.get("id",None)
        bk=Book.objects.get(pk=book)
        bk.IssuedBy = request.user
        bk.save()
        print("book saved")


        oldbooks= MyBook.objects.filter(book=bk)
        print(oldbooks)
        oldbooks.delete()

        mybk= MyBook(book=bk,user=request.user)
        mybk.save()
        print("My book saved")

        response = HttpResponse(json.dumps({'msg': f'Your book has been issued'}), 
        content_type='application/json')
        response.status_code=200    
        return response




@login_required
def mybooks(request):
    context ={
        'mybooks':MyBook.objects.filter(user=request.user)
    }
    return render(request, 'Library/mybooks.html', context)








@login_required
def returnBook(request):
    book = request.POST.get("id",None)
    bk=Book.objects.get(pk=book)
    bk.IssuedBy = None
    bk.save()
    print("book saved")


    oldbooks= MyBook.objects.filter(book=bk)
    print(oldbooks)
    oldbooks.delete()

    print("book returned")

    return HttpResponse(status=200)




