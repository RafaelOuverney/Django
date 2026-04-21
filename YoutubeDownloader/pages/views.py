from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse, FileResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import yt_dlp
import os
import json
from pathlib import Path


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            from .models import Historico
            context['recent_historicos'] = Historico.objects.all()[:5]
        except Exception:
            context['recent_historicos'] = []
        return context

    def post(self, request, *args, **kwargs):
        try:
            url = request.POST.get('url', '').strip()
            format_choice = request.POST.get('format', 'mp4').strip()

            if not url:
                return JsonResponse({'error': 'URL não fornecida'}, status=400)

            # Definir opções de download conforme formato
            format_map = {
                'mp4': 'best[ext=mp4]/best',
                'webm': 'best[ext=webm]/best',
                'avi': 'best[ext=avi]/best',
                'mov': 'best[ext=mov]/best',
                'mp3': 'bestaudio/best',
                'wav': 'bestaudio/best',
                'aac': 'bestaudio/best',
                'flac': 'bestaudio/best',
            }

            format_selection = format_map.get(format_choice, 'best')
            
            # Configurar diretório de download
            download_dir = os.path.join(os.path.dirname(__file__), '..', 'downloads')
            os.makedirs(download_dir, exist_ok=True)

            # Opções do yt-dlp
            ydl_opts = {
                'format': format_selection,
                'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }

            # Para áudio, converter para formato específico
            if format_choice in ['mp3', 'wav', 'aac', 'flac']:
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': format_choice,
                    'preferredquality': '192',
                }]

            # Fazer download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            # Retornar arquivo para download
            file_path = Path(filename)
            if file_path.exists():
                response = FileResponse(open(file_path, 'rb'))
                response['Content-Disposition'] = f'attachment; filename="{file_path.name}"'
                return response
            else:
                return JsonResponse({'error': 'Arquivo não encontrado após download'}, status=500)

        except Exception as e:
            return JsonResponse({'error': f'Erro ao processar download: {str(e)}'}, status=500)


class DownloadsView(TemplateView):
    template_name = 'downloads.html'


class HistoricoView(TemplateView):
    template_name = 'historico.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'


class AjudaView(TemplateView):
    template_name = 'ajuda.html'


# CRUD for Historico
from .models import Historico


class HistoricoListView(ListView):
    model = Historico
    template_name = 'pages/historico_list.html'
    context_object_name = 'historicos'


class HistoricoDetailView(DetailView):
    model = Historico
    template_name = 'pages/historico_detail.html'
    context_object_name = 'historico'


class HistoricoCreateView(CreateView):
    model = Historico
    fields = ['title', 'url', 'format', 'file_path']
    template_name = 'pages/historico_form.html'
    success_url = reverse_lazy('historico_list')


class HistoricoUpdateView(UpdateView):
    model = Historico
    fields = ['title', 'url', 'format', 'file_path']
    template_name = 'pages/historico_form.html'
    success_url = reverse_lazy('historico_list')


class HistoricoDeleteView(DeleteView):
    model = Historico
    template_name = 'pages/historico_confirm_delete.html'
    success_url = reverse_lazy('historico_list')