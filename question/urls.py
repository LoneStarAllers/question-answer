from django.urls import path
from question import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_questions/', views.all_questions, name='all_questions'),
    path('questions/<int:id>', views.question_detail, name='question_detail'),
    path('categories/<int:category_id>', views.category_questions, name='category_questions'),
    path('like/<int:pk>', views.likeQuestion, name='like_question'),
]