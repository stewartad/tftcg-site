from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='char_detail'),
    path('stratagems/<int:pk>', views.StratagemDetail.as_view(), name='strat_detail')
]