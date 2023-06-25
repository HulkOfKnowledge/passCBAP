from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('exam-hall/<int:exam_id>/', views.exam_hall, name='exam-hall'),
    path('exam-hall', views.exam_hall, name='exam-hall'),
    path('exam-board/<int:exam_id>/', views.evaluate_exam, name='exam-board'),
    path('review/<int:user_exam_id>/', views.review_exam, name='review'),
]