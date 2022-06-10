from socket import getnameinfo
from django.urls import path
from . import views


urlpatterns = [
    path('book/list/',views.getBookList),
    path('book/add/list/',views.getBookList),
    path('book/add/', views.addBook.as_view(), name='add_book2'),
    path('book/issue/',views.issue),
    path('member/view/',views.Member.as_view()),
    path('member/add/',views.addMember),
    path('member/find/',views.findMember),

    #rendering the data in a html template
    #path('book/forms/<int:pk>',views.ProileList.as_view(), name='add_book')
]

