from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('list/', views.notes_list, name='list'),
    path('create_note', views.create_note, name='create_note'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('note_detail/<int:note_id>', views.note_detail, name='note_detail'),
    path('note_detail_edit/<int:note_id>/', views.note_detail_edit, name='note_detail_edit'),
]
