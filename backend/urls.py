from django.urls import path
from backend import views
urlpatterns = [
    path('dashboard/', views.dashborad, name='dashboard'),
    path('carausel/', views.carausel, name='carausel'),
    path('editcarausel/<int:id_carausel>', views.editcaruasel, name='editcarausel'),
    path('deletecarausel/<int:id_carausel>', views.deletecarausel, name='deletecarausel')
]
