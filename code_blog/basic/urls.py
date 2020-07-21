from django.urls import path
from . import views

urlpatterns = [
    path('', views.CodeListView.as_view(), name='code_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('code/<int:pk>/', views.CodeDetailView.as_view(), name='code_detail'),
    path('code/new/', views.CodeCreateView.as_view(), name='code_new'),
    path('code/<int:pk>/edit/', views.CodeUpdateView.as_view(), name='code_edit'),
    path('code/<int:pk>/remove/', views.CodeDeleteView.as_view(), name='code_remove'),
    path('drafts/', views.DraftListView.as_view(), name='code_draft_list'),
    path('code/<int:pk>/publish/', views.codes_publish, name='code_publish'),
]