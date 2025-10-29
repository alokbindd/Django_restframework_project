from django.shortcuts import render,HttpResponse

def students(request):
    students = [
        {'id':1,'name':'john doe','age':25}
    ]

    return HttpResponse(students)