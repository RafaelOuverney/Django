from django.views.generic import TemplateView
from django.http import JsonResponse, FileResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import yt_dlp
import os
import json
from pathlib import Path


class IndexView(TemplateView):
    template_name = 'index.html'

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