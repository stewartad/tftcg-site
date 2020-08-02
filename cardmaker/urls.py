from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/<int:card_id>/', views.char_detail, name='char_detail'),
    path('stratagems/<int:card_id>', views.strat_detail, name='strat_detail')
]