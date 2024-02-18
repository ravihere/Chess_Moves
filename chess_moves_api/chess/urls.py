from django.urls import path
from . import views

urlpatterns = [
    path('chess/<slug>', views.chess_moves, name='chess-moves'),
]
