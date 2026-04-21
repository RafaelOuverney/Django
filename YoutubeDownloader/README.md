# Mistral Downloader

Projeto simples para baixar vídeos e áudios de plataformas (YouTube, Spotify, SoundCloud, etc.) via uma interface web.

## Propósito
- Permitir que usuários coletem uma URL de mídia e baixem o arquivo no formato desejado (MP4, MP3, WEBM, FLAC, etc.).
- Ferramenta de estudo/pessoal para integrar `yt-dlp` em uma aplicação Django com frontend leve (HTML/CSS/JS).

## Tecnologias
- Backend: Django (Python)
- Download/extração: `yt-dlp` (requer `ffmpeg` para extração/conversão de áudio)
- Frontend: HTML5, CSS3, JavaScript (Fetch API)
- Ambiente: virtualenv/venv (recomendado)

## Requisitos
- Python 3.8+ instalado
- `ffmpeg` instalado no sistema (usado pelo `yt-dlp` para conversão de áudio)

## Iniciar o projeto (Windows - PowerShell)
1. Criar e ativar venv

```powershell
cd path\to\YoutubeDownloader
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# ou, no cmd
# .\.venv\Scripts\activate.bat
```

2. Instalar dependências

```powershell
pip install -r requirements.txt
# Se não existir requirements.txt, instale ao menos:
# pip install django yt-dlp
```

3. Configurar banco e rodar servidor (desenvolvimento)

```powershell
python manage.py migrate
python manage.py runserver
```

4. Acessar
- Abra `http://127.0.0.1:8000/` no navegador.

## Observações importantes
- `ffmpeg` é necessário para extrair/convertar áudio (ex.: mp3). No Windows, baixe em https://ffmpeg.org/ e adicione ao `PATH`.
- Para produção **não** é seguro expor um serviço que baixa conteúdo de terceiros sem validações; este projeto é para uso local/pessoal.
- Se pretende suportar uploads de avatar (criado no frontend), ajuste as views e o armazenamento (Media settings) no Django.

## Desenvolvimento
- Arquivo principal do frontend: `pages/templates/index.html`
- Estilos: `pages/static/pages/style.css`
- Scripts JS: `pages/static/pages/main.js`
- Views: `pages/views.py`

## Contato
Projeto pessoal — use localmente para testes e estudo.
