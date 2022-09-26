from django.urls import path
from api import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    # path('notes/', views.getNotes, name="notes"),
    # path('notes/<int:pk>/', views.getNote, name="note"),
    # path('notes/<int:pk>/update/', views.updateNote, name="update-note"),
    # path('notes/<int:pk>/delete/', views.deleteNote, name="delete-note"),
    # path('notes/create/', views.createNote, name="create-note"),

    #rest full api
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
]