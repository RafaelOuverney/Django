from django.urls import path
from .views import (
    IndexView,
    DownloadsView,
    HistoricoView,
    SobreView,
    AjudaView,
    HistoricoListView,
    HistoricoDetailView,
    HistoricoCreateView,
    HistoricoUpdateView,
    HistoricoDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('download/', IndexView.as_view(), name='download'),
    path('downloads/', DownloadsView.as_view(), name='downloads'),
    path('historico/', HistoricoView.as_view(), name='historico'),
    # CRUD for historico
    path('historico/list/', HistoricoListView.as_view(), name='historico_list'),
    path('historico/add/', HistoricoCreateView.as_view(), name='historico_add'),
    path('historico/<int:pk>/', HistoricoDetailView.as_view(), name='historico_detail'),
    path('historico/<int:pk>/edit/', HistoricoUpdateView.as_view(), name='historico_edit'),
    path('historico/<int:pk>/delete/', HistoricoDeleteView.as_view(), name='historico_delete'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('ajuda/', AjudaView.as_view(), name='ajuda'),
]
