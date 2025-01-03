from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'books', BookViewSet)
router.register(r'book_copies', BookCopiesViewSet)
router.register(r'reservations', ReservationsViewSet)
router.register(r'waitlist', WaitlistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('add_author/', add_author, name='add_author'),
    path('add_genre/', add_genre, name='add_genre'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<str:book_id>/', edit_book, name='edit_book'),
    path('delete_book/', delete_book, name='delete_book'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('edit_info/<str:user_id>/', edit_user_info, name='edit_user_info'),
    path('make_reservation/', make_reservation, name='make_reservation'),
    path('extend_reservation/', extend_reservation, name='extend_reservation'),
    path('return_book/', return_book, name='return_book'),
    path('add_to_waitlist/', add_to_waitlist, name='add_to_waitlist'),
]
