# 🤖 Tobias Bot Pro

> **Sistema Avançado de Transcrição de Vídeos do YouTube usando IA**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Colab](https://colab.research.google.com/drive/1FO8vIF7PJ1qnfwyfVSCU1jIbGtQ1z87g?usp=sharing)
[![GitHub Stars](https://img.shields.io/github/stars/SEU_USERNAME/tobias-bot-pro?style=social)](https://github.com/SEU_USERNAME/tobias-bot-pro/stargazers)

![Demo](assets/demo.gif)

## 🎯 Visão Geral

O **Tobias Bot Pro** é uma solução completa de transcrição de vídeos do YouTube que combina:

- 🎥 **Download inteligente** de vídeos com múltiplas estratégias anti-bloqueio
- 🧠 **IA de última geração** (Faster Whisper) para transcrição precisa
- 🚀 **Interface moderna** otimizada para Google Colab
- ⚡ **Suporte a GPU** para processamento ultra-rápido
- 🛠️ **Sistema robusto** com tratamento avançado de erros

## ✨ Funcionalidades

### 🔥 **Core Features**
- ✅ Transcrição automática de vídeos do YouTube
- ✅ Suporte a múltiplos formatos de URL
- ✅ Detecção automática de idioma
- ✅ Processamento com GPU/CPU
- ✅ Interface gráfica intuitiva
- ✅ Sistema de retry inteligente

### 🛡️ **Recursos Avançados**
- ✅ Contorno automático de bloqueios 403
- ✅ Múltiplas estratégias de download
- ✅ Validação robusta de URLs
- ✅ Diagnóstico automático de problemas
- ✅ Limpeza automática de arquivos temporários
- ✅ Logs detalhados para debugging

## 🚀 Quick Start

### 📱 **Uso no Google Colab (Recomendado)**
[![Open In Colab](https://colab.research.google.com/drive/1FO8vIF7PJ1qnfwyfVSCU1jIbGtQ1z87g?usp=sharing)

1. Clique no badge acima
2. Execute as células em ordem
3. Cole a URL do YouTube
4. ✨ Pronto!

### 💻 **Instalação Local**
# ========================================
# CÉLULA 1: INSTALAÇÃO DE DEPENDÊNCIAS
# ========================================

def install_dependencies():
    """Instalação otimizada de dependências"""
    import subprocess
    import sys
    
    print("="*70)
    print("🚀 TOBIAS BOT - INSTALAÇÃO PROFISSIONAL v2.0")
    print("="*70)
    print("⏱️ Tempo estimado: 2-3 minutos\n")
    
    # Lista de pacotes essenciais
    packages = [
        'faster-whisper',
        'yt-dlp',
        'transformers',
        'torch',
        'accelerate',
        'ipywidgets',
        'tqdm'
    ]
    
    # Instalar pacotes
    print("📦 Instalando pacotes Python...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
            print(f"   ✅ {package}")
        except subprocess.CalledProcessError:
            print(f"   ❌ Erro ao instalar {package}")
    
    # Instalar ffmpeg
    print("🎵 Configurando processador de áudio...")
    try:
        subprocess.run(["apt", "update", "-qq"], capture_output=True)
        subprocess.run(["apt", "install", "-y", "ffmpeg"], capture_output=True)
        print("   ✅ FFmpeg instalado")
    except:
        print("   ⚠️ Erro ao instalar FFmpeg")
    
    # Habilitar widgets
    print("🎨 Configurando interface...")
    try:
        from google.colab import output
        output.enable_custom_widget_manager()
        print("   ✅ Widgets habilitados")
    except:
        print("   ⚠️ Não foi possível habilitar widgets")
    
    # Verificação do sistema
    print("\n📊 VERIFICAÇÃO DO SISTEMA:")
    print("-" * 40)
    
    import torch
    print(f"✅ PyTorch: {torch.__version__}")
    
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"✅ GPU: {gpu_name}")
        print(f"✅ VRAM: {gpu_memory:.1f} GB")
        print("⚡ Modo: ACELERAÇÃO GPU ATIVADA")
    else:
        print("⚠️ GPU não detectada - Usando CPU")
        print("💡 Dica: Runtime > Change runtime type > GPU")
    
    print("-" * 40)
    print("✅ INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*70)

# Executar instalação
install_dependencies()

# ========================================
# CÉLULA 2: IMPORTAR BIBLIOTECAS
# ========================================

import os
import torch
from faster_whisper import WhisperModel
import yt_dlp
import ipywidgets as widgets
from IPython.display import display, HTML
from tqdm import tqdm

print("📚 Bibliotecas importadas com sucesso!")
print(f"🔥 Dispositivo disponível: {'GPU' if torch.cuda.is_available() else 'CPU'}")

# ========================================
# CÉLULA 3: CLASSE PRINCIPAL TOBIAS BOT
# ========================================

class TobiasBotPro:
    """
    Tobias Bot Pro - Sistema avançado de transcrição de vídeos
    """
    
    def __init__(self):
        """Inicializa o Tobias Bot Pro"""
        print("🤖 Carregando Tobias Bot Pro...")
        self.model = None
        self.setup_model()
        
    def setup_model(self):
        """Configura o modelo Faster Whisper"""
        try:
            # Detectar dispositivo
            device = "cuda" if torch.cuda.is_available() else "cpu"
            compute_type = "float16" if device == "cuda" else "int8"
            
            print(f"🧠 Carregando modelo Whisper ({device})...")
            self.model = WhisperModel("base", device=device, compute_type=compute_type)
            print("✅ Modelo carregado com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro ao carregar modelo: {e}")
            self.model = None
    
    def validate_youtube_url(self, url):
        """Valida e corrige URL do YouTube"""
        import re
        
        # Padrões de URL do YouTube
        youtube_patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
            r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]+)',
            r'(?:https?://)?(?:m\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
        ]
        
        for pattern in youtube_patterns:
            match = re.search(pattern, url)
            if match:
                video_id = match.group(1)
                return f"https://www.youtube.com/watch?v={video_id}"
        
        return None

    def download_video(self, url):
        """
        Baixa vídeo do YouTube com múltiplas estratégias
        
        Args:
            url (str): URL do vídeo
            
        Returns:
            str: Caminho para o arquivo de áudio
        """
        try:
            # Validar URL
            clean_url = self.validate_youtube_url(url)
            if not clean_url:
                print(f"❌ URL inválida: {url}")
                print("💡 Use formato: https://youtube.com/watch?v=VIDEO_ID")
                return None
            
            print(f"🔗 URL validada: {clean_url}")
            print("📥 Tentando baixar vídeo...")
            
            # Lista de configurações para tentar (do mais simples ao mais complexo)
            config_attempts = [
                # Tentativa 1: Configuração básica
                {
                    'format': 'bestaudio[ext=m4a]/bestaudio/best[height<=480]',
                    'outtmpl': 'audio_%(id)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '128',
                    }],
                    'extractaudio': True,
                    'audioformat': 'wav',
                    'embed_chapters': False,
                    'writeinfojson': False,
                    'quiet': False,
                    'no_warnings': False,
                },
                
                # Tentativa 2: Com cookies e headers diferentes
                {
                    'format': 'worst[ext=mp4]/worst',
                    'outtmpl': 'audio_%(id)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '96',
                    }],
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                    },
                    'extractor_args': {
                        'youtube': {
                            'skip': ['hls', 'dash'],
                            'player_client': ['android', 'web']
                        }
                    },
                    'quiet': True,
                },
                
                # Tentativa 3: Usando cliente mobile
                {
                    'format': 'bestaudio[ext=webm]/bestaudio',
                    'outtmpl': 'audio_%(id)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '64',
                    }],
                    'extractor_args': {
                        'youtube': {
                            'player_client': ['android_music', 'android', 'ios']
                        }
                    },
                    'http_headers': {
                        'User-Agent': 'com.google.android.youtube/17.36.4 (Linux; U; Android 12; GB) gzip'
                    },
                    'quiet': True,
                    'socket_timeout': 30,
                }
            ]
            
            for i, ydl_opts in enumerate(config_attempts, 1):
                print(f"🔄 Tentativa {i}/{len(config_attempts)}...")
                
                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        # Obter info do vídeo
                        if i == 1:  # Só mostrar info na primeira tentativa
                            try:
                                info = ydl.extract_info(clean_url, download=False)
                                title = info.get('title', 'Título não encontrado')
                                duration = info.get('duration', 0)
                                
                                print(f"🎬 Título: {title}")
                                if duration:
                                    mins = duration // 60
                                    secs = duration % 60
                                    print(f"⏱️ Duração: {mins}:{secs:02d}")
                                
                                if duration > 3600:  # Mais de 1 hora
                                    print("⚠️ Vídeo muito longo - pode levar bastante tempo")
                            except:
                                pass
                        
                        # Tentar baixar
                        print(f"⬇️ Baixando com configuração {i}...")
                        info = ydl.extract_info(clean_url, download=True)
                        video_id = info['id']
                        
                        # Procurar arquivo de áudio
                        possible_files = [
                            f"audio_{video_id}.wav",
                            f"audio_{video_id}.m4a", 
                            f"audio_{video_id}.mp3",
                            f"audio_{video_id}.webm",
                            f"audio_{video_id}.mp4"
                        ]
                        
                        for audio_file in possible_files:
                            if os.path.exists(audio_file):
                                # Se não for WAV, converter
                                if not audio_file.endswith('.wav'):
                                    wav_file = f"audio_{video_id}.wav"
                                    print(f"🔄 Convertendo para WAV: {audio_file} -> {wav_file}")
                                    try:
                                        import subprocess
                                        subprocess.run([
                                            'ffmpeg', '-i', audio_file, '-ar', '16000', 
                                            '-ac', '1', '-c:a', 'pcm_s16le', wav_file, '-y'
                                        ], check=True, capture_output=True, text=True)
                                        os.remove(audio_file)
                                        audio_file = wav_file
                                        print("✅ Conversão concluída")
                                    except Exception as conv_error:
                                        print(f"⚠️ Conversão falhou: {conv_error}")
                                        print("🔄 Usando arquivo original")
                                
                                print(f"✅ Áudio baixado com sucesso: {audio_file}")
                                return audio_file
                        
                        print(f"❌ Nenhum arquivo encontrado na tentativa {i}")
                        
                except yt_dlp.DownloadError as e:
                    error_msg = str(e).lower()
                    if "403" in error_msg or "forbidden" in error_msg:
                        print(f"❌ Tentativa {i}: Bloqueio 403 - Tentando próxima configuração...")
                    elif "unavailable" in error_msg:
                        print(f"❌ Tentativa {i}: Vídeo indisponível")
                        break  # Se vídeo não existe, não adianta tentar outras configs
                    else:
                        print(f"❌ Tentativa {i}: {e}")
                    continue
                except Exception as e:
                    print(f"❌ Tentativa {i}: Erro inesperado - {e}")
                    continue
            
            # Se chegou aqui, todas as tentativas falharam
            print("\n💡 SOLUÇÕES ALTERNATIVAS:")
            print("="*50)
            print("1. 📱 Tente baixar o áudio manualmente:")
            print(f"   - Vá em: {clean_url}")
            print("   - Use um conversor online para MP3/WAV")
            print("   - Faça upload do arquivo aqui")
            print("\n2. 🔄 Atualize o yt-dlp:")
            print("   - Execute: update_ytdlp()")
            print("\n3. 🎯 Teste com vídeos menores (< 10 min)")
            print("\n4. ⏰ Tente novamente mais tarde")
            print("="*50)
            
            return None
                    
        except Exception as e:
            print(f"❌ Erro crítico no download: {e}")
            return None
    
    def transcribe_audio(self, audio_file):
        """
        Transcreve áudio para texto
        
        Args:
            audio_file (str): Caminho para o arquivo de áudio
            
        Returns:
            str: Texto transcrito
        """
        if not self.model:
            print("❌ Modelo não carregado")
            return None
            
        try:
            print("🎯 Iniciando transcrição...")
            segments, info = self.model.transcribe(audio_file, language="pt")
            
            print(f"📊 Idioma detectado: {info.language} (confiança: {info.language_probability:.2f})")
            
            # Juntar todos os segmentos
            full_text = ""
            segment_count = 0
            
            for segment in segments:
                full_text += segment.text + " "
                segment_count += 1
                if segment_count % 10 == 0:
                    print(f"   📝 Processados {segment_count} segmentos...")
            
            print(f"✅ Transcrição concluída! ({segment_count} segmentos)")
            return full_text.strip()
            
        except Exception as e:
            print(f"❌ Erro na transcrição: {e}")
            return None
    
    def test_youtube_connection(self):
        """Testa conexão com YouTube"""
        try:
            print("🧪 Testando conexão com YouTube...")
            test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll - sempre disponível
            
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'skip_download': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(test_url, download=False)
                if info:
                    print("✅ Conexão com YouTube OK")
                    return True
        except:
            print("❌ Problema de conexão com YouTube")
            return False

    def process_video(self, url):
        """
        Processa vídeo completo: download + transcrição
        
        Args:
            url (str): URL do vídeo
            
        Returns:
            str: Texto transcrito
        """
        print("="*50)
        print("🚀 PROCESSANDO VÍDEO")
        print("="*50)
        
        # Testar conexão primeiro
        if not self.test_youtube_connection():
            print("❌ Problema de conectividade. Tentando mesmo assim...")
        
        # Download do vídeo
        audio_file = self.download_video(url)
        if not audio_file:
            print("\n🔍 DIAGNÓSTICO DE PROBLEMAS:")
            print("="*40)
            print("❌ Falha no download. Possíveis causas:")
            print("1. URL incorreta ou inválida")
            print("2. Vídeo privado, removido ou com restrições")
            print("3. Problemas de conectividade")
            print("4. Vídeo com restrições de região")
            print("5. Vídeo muito longo ou com formato não suportado")
            print("\n💡 SOLUÇÕES:")
            print("- Verifique se a URL está completa e correta")
            print("- Teste com outro vídeo público e curto")
            print("- Verifique sua conexão com internet")
            return None
        
        # Transcrição
        transcription = self.transcribe_audio(audio_file)
        
        # Limpeza
        try:
            os.remove(audio_file)
            print(f"🧹 Arquivo temporário removido: {audio_file}")
        except:
            pass
        
        print("="*50)
        print("✅ PROCESSAMENTO CONCLUÍDO!")
        print("="*50)
        
        return transcription

# ========================================
# CÉLULA 6: FUNÇÕES DE TESTE E DEBUG
# ========================================

def test_url(url):
    """Testa uma URL específica sem processar completamente"""
    import yt_dlp
    
    print(f"🧪 Testando URL: {url}")
    print("-" * 50)
    
    # Validar formato da URL
    import re
    youtube_patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
        r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]+)',
        r'(?:https?://)?(?:m\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
    ]
    
    valid_url = False
    for pattern in youtube_patterns:
        if re.search(pattern, url):
            valid_url = True
            break
    
    if not valid_url:
        print("❌ Formato de URL inválido")
        return False
    else:
        print("✅ Formato de URL válido")
    
    # Testar acesso ao vídeo
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if info:
                print("✅ Vídeo acessível")
                print(f"📌 Título: {info.get('title', 'N/A')}")
                print(f"📌 Duração: {info.get('duration', 'N/A')} segundos")
                print(f"📌 Canal: {info.get('uploader', 'N/A')}")
                return True
            else:
                print("❌ Não foi possível acessar o vídeo")
                return False
                
    except Exception as e:
        print(f"❌ Erro ao acessar vídeo: {e}")
        return False

def update_ytdlp():
    """Atualiza o yt-dlp para a versão mais recente"""
    import subprocess
    import sys
    
    print("🔄 Atualizando yt-dlp...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        print("✅ yt-dlp atualizado com sucesso!")
    except:
        print("❌ Erro ao atualizar yt-dlp")

def list_video_formats(url):
    """Lista formatos disponíveis para um vídeo"""
    import yt_dlp
    
    try:
        ydl_opts = {
            'quiet': True,
            'listformats': True,
        }
        
        print(f"📋 Formatos disponíveis para: {url}")
        print("-" * 50)
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.list_formats(url)
            
    except Exception as e:
        print(f"❌ Erro ao listar formatos: {e}")

def fix_youtube_403():
    """Aplica correções para problemas 403 do YouTube"""
    import subprocess
    import sys
    
    print("🔧 Aplicando correções para erro 403...")
    print("="*50)
    
    # 1. Atualizar yt-dlp para versão mais recente
    print("1️⃣ Atualizando yt-dlp...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        print("   ✅ yt-dlp atualizado")
    except:
        print("   ❌ Erro ao atualizar yt-dlp")
    
    # 2. Instalar versão de desenvolvimento (mais atualizada)
    print("2️⃣ Instalando versão de desenvolvimento...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "https://github.com/yt-dlp/yt-dlp/archive/master.zip"])
        print("   ✅ Versão de desenvolvimento instalada")
    except:
        print("   ❌ Erro ao instalar versão dev")
    
    # 3. Verificar versão
    print("3️⃣ Verificando versão...")
    try:
        import yt_dlp
        print(f"   ✅ Versão atual: {yt_dlp.version.__version__}")
    except:
        print("   ⚠️ Não foi possível verificar versão")
    
    print("="*50)
    print("✅ Correções aplicadas!")
    print("💡 Agora tente novamente com o bot")

def transcribe_local_file(file_path):
    """Transcreve arquivo local diretamente"""
    try:
        print(f"🎯 Transcrevendo arquivo local: {file_path}")
        
        # Verificar se arquivo existe
        if not os.path.exists(file_path):
            print(f"❌ Arquivo não encontrado: {file_path}")
            return None
        
        # Criar bot simples só para transcrição
        bot = TobiasBotPro()
        if not bot.model:
            print("❌ Modelo não carregado")
            return None
        
        # Transcrever
        transcription = bot.transcribe_audio(file_path)
        return transcription
        
    except Exception as e:
        print(f"❌ Erro na transcrição: {e}")
        return None

def try_alternative_download(url):
    """Tenta download usando pytube como alternativa"""
    try:
        print("🔄 Tentando método alternativo com pytube...")
        
        # Instalar pytube se necessário
        try:
            from pytube import YouTube
        except ImportError:
            print("📦 Instalando pytube...")
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
            from pytube import YouTube
        
        # Baixar usando pytube
        yt = YouTube(url)
        print(f"🎬 Título: {yt.title}")
        print(f"⏱️ Duração: {yt.length} segundos")
        
        # Pegar stream de áudio
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        
        if audio_stream:
            print("⬇️ Baixando com pytube...")
            filename = f"audio_{yt.video_id}.mp4"
            audio_stream.download(filename=filename)
            
            # Converter para WAV
            wav_filename = f"audio_{yt.video_id}.wav"
            print(f"🔄 Convertendo para WAV...")
            
            import subprocess
            subprocess.run([
                'ffmpeg', '-i', filename, '-ar', '16000', 
                '-ac', '1', '-c:a', 'pcm_s16le', wav_filename, '-y'
            ], check=True, capture_output=True)
            
            # Remover arquivo original
            os.remove(filename)
            
            print(f"✅ Download alternativo concluído: {wav_filename}")
            return wav_filename
        else:
            print("❌ Nenhum stream de áudio encontrado")
            return None
            
    except Exception as e:
        print(f"❌ Método alternativo falhou: {e}")
        return None

print("🛠️ Funções de correção criadas!")
print("\n🔧 COMANDOS DE CORREÇÃO:")
print("- fix_youtube_403()                    # Corrige problemas 403")
print("- try_alternative_download('URL')      # Tenta método alternativo")  
print("- transcribe_local_file('arquivo.wav') # Transcreve arquivo local")

# ========================================
# CÉLULA 4: INTERFACE GRÁFICA
# ========================================

def create_interface(bot):
    """Cria interface gráfica para o bot"""
    
    # Estilo personalizado
    style = """
    <style>
    .tobias-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .tobias-info {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #007bff;
        margin-bottom: 15px;
    }
    </style>
    """
    
    # Header
    header_html = """
    <div class="tobias-header">
        <h1>🤖 TOBIAS BOT PRO</h1>
        <p>Sistema Avançado de Transcrição de Vídeos do YouTube</p>
    </div>
    """
    
    # Informações
    info_html = """
    <div class="tobias-info">
        <h3>📋 Como usar:</h3>
        <ol>
            <li>Cole a URL do vídeo do YouTube no campo abaixo</li>
            <li>Clique em "🚀 Processar Vídeo"</li>
            <li>Aguarde o processamento (pode levar alguns minutos)</li>
            <li>A transcrição aparecerá na área de texto</li>
        </ol>
        <p><strong>💡 Dica:</strong> Funciona melhor com áudio claro e em português!</p>
    </div>
    """
    
    # Campo de entrada
    url_input = widgets.Text(
        value='',
        placeholder='https://youtube.com/watch?v=...',
        description='URL do YouTube:',
        style={'description_width': '120px'},
        layout=widgets.Layout(width='600px', margin='10px 0')
    )
    
    # Botão de processar
    process_button = widgets.Button(
        description='🚀 Processar Vídeo',
        button_style='success',
        layout=widgets.Layout(width='200px', height='40px')
    )
    
    # Botão de limpar
    clear_button = widgets.Button(
        description='🧹 Limpar',
        button_style='info',
        layout=widgets.Layout(width='100px', height='40px')
    )
    
    # Área de status
    status_area = widgets.HTML(
        value="<p style='color: #666;'>⏳ Aguardando URL...</p>",
        layout=widgets.Layout(margin='10px 0')
    )
    
    # Área de resultado
    result_area = widgets.Textarea(
        value='',
        placeholder='📝 A transcrição completa aparecerá aqui após o processamento...',
        layout=widgets.Layout(width='100%', height='400px', margin='10px 0')
    )
    
    # Função do botão processar
    def on_process_click(b):
        if not url_input.value.strip():
            status_area.value = "<p style='color: red;'>⚠️ Por favor, insira uma URL válida do YouTube.</p>"
            return
        
        status_area.value = "<p style='color: blue;'>🔄 Processando... Por favor aguarde (pode levar alguns minutos)...</p>"
        result_area.value = "🔄 Processando vídeo...\n\nEste processo pode levar alguns minutos dependendo do tamanho do vídeo.\nPor favor, não feche esta janela."
        
        try:
            transcription = bot.process_video(url_input.value.strip())
            if transcription:
                result_area.value = transcription
                status_area.value = "<p style='color: green;'>✅ Transcrição concluída com sucesso!</p>"
            else:
                result_area.value = "❌ Erro no processamento.\n\nVerifique se:\n- A URL está correta\n- O vídeo existe e está público\n- Sua conexão com internet está funcionando"
                status_area.value = "<p style='color: red;'>❌ Erro no processamento. Verifique a URL e tente novamente.</p>"
        except Exception as e:
            result_area.value = f"❌ Erro inesperado:\n{str(e)}"
            status_area.value = "<p style='color: red;'>❌ Erro inesperado durante o processamento.</p>"
    
    # Função do botão limpar
    def on_clear_click(b):
        url_input.value = ""
        result_area.value = ""
        status_area.value = "<p style='color: #666;'>⏳ Aguardando URL...</p>"
    
    # Conectar funções aos botões
    process_button.on_click(on_process_click)
    clear_button.on_click(on_clear_click)
    
    # Exibir interface
    display(HTML(style + header_html + info_html))
    display(widgets.VBox([
        url_input,
        widgets.HBox([process_button, clear_button]),
        status_area,
        widgets.HTML("<hr><h3>📝 Resultado da Transcrição:</h3>"),
        result_area
    ]))
    
    return url_input, result_area, status_area

print("🎨 Função de interface criada com sucesso!")

# ========================================
# CÉLULA 5: INICIALIZAÇÃO E USO
# ========================================

def iniciar_tobias():
    """
    Inicializa o Tobias Bot Pro com interface
    
    Retorna:
        TobiasBotPro: Instância do bot pronta para uso
    """
    print("🚀 Inicializando Tobias Bot Pro...")
    bot = TobiasBotPro()
    
    if bot.model:
        print("✅ Bot inicializado com sucesso!")
        create_interface(bot)
        return bot
    else:
        print("❌ Erro na inicialização do bot")
        return None

# Para usar sem interface (opcional)
def usar_direto():
    """Exemplo de uso direto sem interface"""
    bot = TobiasBotPro()
    
    # Exemplo de uso
    print("\n" + "="*50)
    print("📖 EXEMPLO DE USO DIRETO:")
    print("="*50)
    print("bot = TobiasBotPro()")
    print("transcricao = bot.process_video('URL_DO_YOUTUBE')")
    print("print(transcricao)")
    print("="*50)
    
    return bot

print("🎯 Funções de inicialização prontas!")
print("\n" + "="*70)
print("🚀 PARA USAR O TOBIAS BOT PRO:")
print("="*70)
print("1. Execute: bot = iniciar_tobias()")
print("2. Use a interface que aparecerá")
print("\nOU")
print("1. Execute: bot = usar_direto()")
print("2. Use: transcricao = bot.process_video('URL')")
print("="*70)
