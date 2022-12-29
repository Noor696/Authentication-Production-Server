from django.urls import path
from .views import NovelListView, NovelDetailView

urlpatterns = [
    path('', NovelListView.as_view(), name='novel_list'),
    path('<int:pk>/', NovelDetailView.as_view(), name='novel_detail'),
   
]