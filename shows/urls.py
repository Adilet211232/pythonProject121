from django.urls import path
from  . import  views
app_name = 'shows'
urlpatterns = [
    path('shows/',views.KnigaListView.as_view(), name ='shows_all'),
    path('shows/<int:id>/',views.KnigaDetailView.as_view(), name ='shows_detail'),
    path('shows/<int:id>/update/',views.KnigaUpdateView.as_view(), name ='show_update'),
    path('shows/<int:id>/delete/',views.KnigaDeleteView.as_view(), name ='show_delete'),
    path('add-show/',views.KnigaCreateView.as_view(), name ='add-shows'),




]