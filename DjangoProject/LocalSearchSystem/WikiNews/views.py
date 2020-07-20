from django.shortcuts import render

# Create your views here.

def ItemManagementView(request):
    return render(request, 'item-management.html')

def WebScrappingView(request):
    return render(request, 'web-scrapping.html')

def ItemDetailView(request):
    return render(request, 'details.html')

def SearchView(request):
    return render(request, 'search.html')

def SearchResultView(request):
    return render(request,'search-result.html')

def SearchItemResultView(request):
    return render(request, 'search-item-result.html')

def CollaborationView(request):
    return render(request, 'collaboration.html')

def OpinionsView(request):
    return render(request, 'opinions.html')