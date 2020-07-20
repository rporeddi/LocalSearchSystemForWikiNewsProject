from django.urls import path
from .import views

app_name = 'WikiNews'

urlpatterns = [
    path('item-management/', views.ItemManagementView, name='itemmanagement'),
    path('web-scrapping/', views.WebScrappingView, name = "webscrapping"),
    path('Item-details/', views.ItemDetailView, name = "itemdetails"),
    path('search-result/', views.SearchResultView, name = "searchresult"),
    path('search-item-result/', views.SearchItemResultView, name='searchitemresult'),
    path('collaboration/', views.CollaborationView, name='collaboration'),
    path('opinions/', views.OpinionsView, name='opinions')

]