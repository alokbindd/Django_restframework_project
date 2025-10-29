from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeesViewset,basename='employee')


urlpatterns = [
    path('students/',views.StudentView),
    path('students/<int:pk>/',views.StudentdetailView),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/',views.Employeedetail.as_view()),
    path('',include(router.urls)),
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),
]