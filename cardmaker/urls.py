from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='char_detail'),
    path('characters/<int:pk>/edit/', views.EditCharacter.as_view(), name='char_edit'),
    path('characters/create/', views.CreateCharacter.as_view(), name='char_create'),
    path('stratagems/<int:pk>', views.StratagemDetail.as_view(), name='strat_detail'),
    path('stratagems/<int:pk>/edit/', views.EditStratagem.as_view(), name='strat_edit'),
    path('stratagems/create/', views.CreateStratagem.as_view(), name='strat_create'),
]