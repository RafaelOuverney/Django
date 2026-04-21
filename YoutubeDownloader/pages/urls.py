from django.urls import path
from .views import IndexView, DownloadsView, HistoricoView, SobreView, AjudaView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('download/', IndexView.as_view(), name='download'),
    path('downloads/', DownloadsView.as_view(), name='downloads'),
    path('historico/', HistoricoView.as_view(), name='historico'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('ajuda/', AjudaView.as_view(), name='ajuda'),
]
