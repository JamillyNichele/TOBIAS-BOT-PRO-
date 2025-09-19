# =============================================================================
# TOBIAS BOT PRO - NOTEBOOK PARA GOOGLE COLAB
# Salve este arquivo como: Tobias_Bot_Pro_Complete.ipynb
# =============================================================================

# INSTRUÇÕES:
# 1. Abra o Google Colab (colab.research.google.com)
# 2. File > New notebook
# 3. Delete todas as células
# 4. Copie e cole cada seção abaixo em células separadas
# 5. File > Save to GitHub
# 6. Salve como: Tobias_Bot_Pro_Complete.ipynb

# =============================================================================
# CÉLULA 1: MARKDOWN - HEADER
# =============================================================================
"""
Copie este MARKDOWN em uma célula de texto:

# 🤖 TOBIAS BOT PRO

**Sistema Avançado de Transcrição de Vídeos do YouTube usando IA**

[![GitHub](https://img.shields.io/badge/GitHub-Projeto-blue)](https://github.com/Jamilly_Nicehele/tobias-bot-pro)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Jamilly_Nichele/tobias-bot-pro/blob/main/LICENSE)

---

## 🎯 **O que este notebook faz:**

✅ **Transcreve automaticamente vídeos do YouTube**  
✅ **Interface moderna e intuitiva**  
✅ **Suporte a GPU para processamento rápido**  
✅ **Sistema robusto com múltiplas estratégias**  
✅ **Totalmente gratuito e open source**

## 📋 **Como usar:**

1. **Execute as células em ordem** (Ctrl+F9 para executar todas)
2. **Aguarde a instalação** (primeira execução)
3. **Use a interface gráfica** que aparecerá
4. **Cole a URL do YouTube** e clique em "Processar"

---
"""

# =============================================================================
# CÉLULA 2: PYTHON - VERIFICAÇÃO DO AMBIENTE
# =============================================================================

# 🔍 VERIFICAÇÃO DO AMBIENTE
print("🔍 VERIFICANDO AMBIENTE DO GOOGLE COLAB")
print("=" * 50)

import sys
print(f"🐍 Python: {sys.version}")

# Verificar se está no Colab
try:
    import google.colab
    print("✅ Google Colab detectado")
    IN_COLAB = True
except ImportError:
    print("⚠️ Não está no Google Colab")
    IN_COLAB = False

# Verificar GPU
import torch
if torch.cuda.is_available():
    gpu_name = torch.cuda.get_device_name(0)
    gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
    print(f"🚀 GPU: {gpu_name}")
    print(f"💾 VRAM: {gpu_memory:.1f} GB")
    print("⚡ Status: ACELERAÇÃO GPU ATIVADA")
else:
    print("🔧 GPU: Não detectada")
    print("💡 Dica: Runtime > Change runtime type > GPU")

print("=" * 50)

# =============================================================================
# CÉLULA 3: PYTHON - INSTALAÇÃO DE DEPENDÊNCIAS
# =============================================================================

# 📦 INSTALAÇÃO DE DEPENDÊNCIAS
import subprocess
import sys

def install_dependencies():
    """Instala todas as dependências necessárias"""
    print("🚀 TOBIAS BOT PRO - INSTALAÇÃO v2.0")
    print("=" * 50)
    print("⏱️ Tempo estimado: 2-3 minutos\n")
    
    # Pacotes essenciais
    packages = [
        'faster-whisper>=0.10.0',
        'yt-dlp>=2023.12.30', 
        'torch>=2.0.0',
        'transformers>=4.35.0',
        'accelerate>=0.24.0',
        'ipywidgets>=8.0.0',
        'tqdm>=4.65.0',
        'pytube>=15.0.0'
    ]
    
    print("📦 Instalando pacotes Python...")
    for package in packages:
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "-q", "--upgrade", package
            ])
            print(f"   ✅ {package.split('>=')[0]}")
        except Exception as e:
            print(f"   ❌ Erro: {package}")
    
    print("\n🎵 Configurando FFmpeg...")
    try:
        subprocess.run(["apt", "update", "-qq"], capture_output=True)
        subprocess.run(["apt", "install", "-y", "ffmpeg"], capture_output=True)
        print("   ✅ FFmpeg instalado")
    except:
        print("   ⚠️ Problema com FFmpeg")
    
    if IN_COLAB:
        print("\n🎨 Habilitando widgets...")
        try:
            from google.colab import output
            output.enable_custom_widget_manager()
            print("   ✅ Widgets habilitados")
        except:
            print("   ⚠️ Problema com widgets")
    
    print("\n" + "=" * 50)
    print("✅ INSTALAÇÃO CONCLUÍDA!")
    print("=" * 50)

# Executar instalação
install_dependencies()

# =============================================================================
# CÉLULA 4: PYTHON - IMPORTAÇÕES
# =============================================================================

# 📚 IMPORTAÇÕES E CONFIGURAÇÕES
print("📚 Carregando bibliotecas...")

import os
import re
import torch
import logging
from typing import Optional, List

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Importações específicas
try:
    from faster_whisper import WhisperModel
    import yt_dlp
    import ipywidgets as widgets
    from IPython.display import display, HTML
    from tqdm.auto import tqdm
    
    print("✅ Bibliotecas carregadas!")
    print(f"🔥 Dispositivo: {'GPU' if torch.cuda.is_available() else 'CPU'}")
    
except ImportError as e:
    print(f"❌ Erro ao importar: {e}")
    print("💡 Execute a célula de instalação novamente")

# =============================================================================
# CÉLULA 5: PYTHON - CLASSE PRINCIPAL
# =============================================================================

# 🤖 CLASSE PRINCIPAL TOBIAS BOT
class TobiasBotPro:
    """Sistema avançado de transcrição de vídeos do YouTube"""
    
    def __init__(self, model_size="base"):
        self.model_size = model_size
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.compute_type = "float16" if self.device == "cuda" else "int8"
        self.model = None
        
        print(f"🤖 Iniciando Tobias Bot Pro ({model_size})...")
        self._load_model()
    
    def _load_model(self):
        try:
            print("🧠 Carregando modelo Whisper...")
            self.model = WhisperModel(
                self.model_size,
                device=self.device,
                compute_type=self.compute_type
            )
            print("✅ Modelo carregado!")
            return True
        except Exception as e:
            print(f"❌ Erro: {e}")
            return False
    
    def validate_url(self, url):
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
            r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                video_id = match.group(1)
                return f"https://www.youtube.com/watch?v={video_id}"
        return None
    
    def download_video(self, url):
        clean_url = self.validate_url(url)
        if not clean_url:
            print("❌ URL inválida")
            return None
        
        print(f"🔗 Processando: {clean_url}")
        
        # Tentar yt-dlp
        audio_file = self._download_with_ydl(clean_url)
        if audio_file:
            return audio_file
        
        # Tentar pytube
        audio_file = self._download_with_pytube(clean_url)
        return audio_file
    
    def _download_with_ydl(self, url):
        configs = [
            {
                'format': 'bestaudio[ext=m4a]/bestaudio',
                'outtmpl': 'audio_%(id)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '128',
                }],
            },
            {
                'format': 'worst[ext=mp4]/worst',
                'outtmpl': 'audio_%(id)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '96',
                }],
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Android) AppleWebKit/537.36'
                },
                'extractor_args': {
                    'youtube': {'player_client': ['android']}
                },
            }
        ]
        
        for i, config in enumerate(configs, 1):
            try:
                print(f"📥 Tentativa {i}...")
                with yt_dlp.YoutubeDL(config) as ydl:
                    info = ydl.extract_info(url, download=True)
                    return self._find_audio_file(info['id'])
            except Exception as e:
                print(f"❌ Tentativa {i} falhou")
                continue
        return None
    
    def _download_with_pytube(self, url):
        try:
            from pytube import YouTube
            print("📥 Tentando pytube...")
            
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            
            if audio_stream:
                filename = f"audio_{yt.video_id}.mp4"
                audio_stream.download(filename=filename)
                
                wav_file = f"audio_{yt.video_id}.wav"
                if self._convert_to_wav(filename, wav_file):
                    os.remove(filename)
                    return wav_file
                return filename
        except Exception as e:
            print(f"❌ Pytube falhou: {e}")
        return None
    
    def _find_audio_file(self, video_id):
        extensions = ['.wav', '.m4a', '.mp3', '.webm', '.mp4']
        for ext in extensions:
            filename = f"audio_{video_id}{ext}"
            if os.path.exists(filename):
                if ext != '.wav':
                    wav_file = f"audio_{video_id}.wav"
                    if self._convert_to_wav(filename, wav_file):
                        os.remove(filename)
                        return wav_file
                return filename
        return None
    
    def _convert_to_wav(self, input_file, output_file):
        try:
            import subprocess
            subprocess.run([
                'ffmpeg', '-i', input_file, '-ar', '16000', 
                '-ac', '1', '-c:a', 'pcm_s16le', output_file, '-y'
            ], capture_output=True, check=True)
            return True
        except:
            return False
    
    def transcribe_audio(self, audio_file):
        if not self.model:
            print("❌ Modelo não carregado")
            return None
        
        try:
            print("🎯 Transcrevendo...")
            segments, info = self.model.transcribe(audio_file, language="pt")
            
            print(f"📊 Idioma: {info.language} (confiança: {info.language_probability:.2f})")
            
            full_text = ""
            segments_list = list(segments)
            
            for segment in tqdm(segments_list, desc="Processando"):
                full_text += segment.text + " "
            
            print(f"✅ Concluído! ({len(segments_list)} segmentos)")
            return full_text.strip()
            
        except Exception as e:
            print(f"❌ Erro: {e}")
            return None
    
    def process_video(self, url):
        print("🚀 PROCESSANDO VÍDEO")
        print("=" * 40)
        
        audio_file = self.download_video(url)
        if not audio_file:
            return None
        
        transcription = self.transcribe_audio(audio_file)
        
        try:
            os.remove(audio_file)
            print(f"🧹 Removido: {audio_file}")
        except:
            pass
        
        print("=" * 40)
        print("✅ CONCLUÍDO!")
        
        return transcription

print("🤖 Classe TobiasBotPro criada!")

# =============================================================================
# CÉLULA 6: PYTHON - INTERFACE GRÁFICA
# =============================================================================

# 🎨 INTERFACE GRÁFICA MODERNA
def create_interface():
    """Cria interface moderna para o bot"""
    
    # Header HTML
    header_html = """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 25px; border-radius: 15px; 
                text-align: center; margin-bottom: 20px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
        <h1 style="font-size: 2.5em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🤖 TOBIAS BOT PRO
        </h1>
        <p style="font-size: 1.1em; margin-bottom: 20px;">
            Sistema Avançado de Transcrição com IA
        </p>
        <div style="margin-bottom: 15px;">
            <span style="background: rgba(255,255,255,0.2); padding: 8px 15px; 
                         border-radius: 20px; margin: 5px; font-size: 0.9em;">
                🎥 Download Inteligente
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 8px 15px; 
                         border-radius: 20px; margin: 5px; font-size: 0.9em;">
                🧠 IA Whisper
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 8px 15px; 
                         border-radius: 20px; margin: 5px; font-size: 0.9em;">
                ⚡ GPU Ready
            </span>
        </div>
        <p style="font-size: 0.9em; opacity: 0.9;">
            📋 <strong>Como usar:</strong> Cole a URL → Clique em Processar → Aguarde o resultado
        </p>
    </div>
    """
    
    display(HTML(header_html))
    
    # Inicializar bot
    print("🚀 Inicializando Tobias Bot Pro...")
    bot = TobiasBotPro()
    
    if not bot.model:
        print("❌ Erro na inicialização")
        return None
    
    # Widgets
    url_input = widgets.Text(
        placeholder='https://youtube.com/watch?v=... ou https://youtu.be/...',
        description='📺 URL:',
        layout=widgets.Layout(width='100%', height='45px'),
        style={'description_width': '80px'}
    )
    
    process_btn = widgets.Button(
        description='🚀 Processar Vídeo',
        button_style='success',
        layout=widgets.Layout(width='180px', height='45px')
    )
    
    clear_btn = widgets.Button(
        description='🧹 Limpar',
        button_style='info', 
        layout=widgets.Layout(width='120px', height='45px')
    )
    
    status_output = widgets.HTML(
        value='<p style="color: #666;">⏳ Aguardando URL do YouTube...</p>'
    )
    
    result_area = widgets.Textarea(
        placeholder='📝 A transcrição aparecerá aqui...\n\n💡 Funciona melhor com áudio claro em português',
        layout=widgets.Layout(width='100%', height='400px')
    )
    
    # Função de processamento
    def process_video(btn):
        if not url_input.value.strip():
            status_output.value = '<p style="color: red;">⚠️ Insira uma URL válida</p>'
            return
        
        result_area.value = ""
        status_output.value = '<p style="color: blue;">🔄 Processando... Aguarde...</p>'
        
        try:
            transcription = bot.process_video(url_input.value.strip())
            
            if transcription:
                result_area.value = transcription
                word_count = len(transcription.split())
                status_output.value = f'<p style="color: green;">✅ Concluído! ({word_count} palavras)</p>'
            else:
                result_area.value = "❌ Erro no processamento.\n\n💡 Tente:\n• Verificar se o vídeo está público\n• Usar vídeos menores\n• Tentar outro vídeo"
                status_output.value = '<p style="color: red;">❌ Falha no processamento</p>'
            
        except Exception as e:
            result_area.value = f"❌ Erro: {str(e)}\n\n💡 Tente executar todas as células novamente"
            status_output.value = '<p style="color: red;">❌ Erro inesperado</p>'
    
    def clear_all(btn):
        url_input.value = ""
        result_area.value = ""
        status_output.value = '<p style="color: #666;">⏳ Aguardando nova URL...</p>'
    
    # Conectar eventos
    process_btn.on_click(process_video)
    clear_btn.on_click(clear_all)
    
    # Layout
    interface = widgets.VBox([
        widgets.HBox([url_input]),
        widgets.HBox([process_btn, clear_btn]),
        status_output,
        widgets.HTML('<hr><h3>📝 Resultado da Transcrição</h3>'),
        result_area
    ])
    
    display(interface)
    
    # Info final
    info_html = """
    <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; 
                margin-top: 20px; border-left: 4px solid #007bff;">
        <h4 style="color: #007bff; margin-top: 0;">💡 Dicas de Uso</h4>
        <ul>
            <li><strong>URLs:</strong> youtube.com/watch?v=... ou youtu.be/...</li>
            <li><strong>Duração:</strong> Vídeos até 1 hora funcionam melhor</li>
            <li><strong>Áudio:</strong> Qualidade clara produz melhor resultado</li>
        </ul>
    </div>
    
    <div style="text-align: center; margin-top: 20px; padding: 15px; 
                background: #e7f3ff; border-radius: 8px;">
        <strong>🌟 Gostou?</strong> 
        <a href="https://github.com/SEU_USERNAME/tobias-bot-pro" target="_blank">
            ⭐ Deixe uma estrela no GitHub!
        </a>
    </div>
    """
    
    display(HTML(info_html))
    return bot

print("🎨 Interface criada!")

# =============================================================================
# CÉLULA 7: PYTHON - FUNÇÕES UTILITÁRIAS
# =============================================================================

# 🔧 FUNÇÕES UTILITÁRIAS
def test_url(url):
    """Testa URL rapidamente"""
    print(f"🧪 Testando: {url}")
    
    bot = TobiasBotPro()
    clean_url = bot.validate_url(url)
    
    if clean_url:
        print(f"✅ URL válida: {clean_url}")
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(clean_url, download=False)
                print(f"🎬 Título: {info.get('title', 'N/A')}")
                print(f"⏱️ Duração: {info.get('duration', 'N/A')}s")
                return True
        except:
            print("❌ Erro ao acessar")
    else:
        print("❌ URL inválida")
    
    return False

def fix_youtube_403():
    """Corrige erros 403"""
    print("🔧 Atualizando yt-dlp...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        print("✅ Atualizado com sucesso")
    except:
        print("❌ Erro na atualização")

print("🔧 Utilitários carregados!")

# =============================================================================
# CÉLULA 8: PYTHON - INICIALIZAÇÃO PRINCIPAL
# =============================================================================

# 🚀 INICIALIZAÇÃO PRINCIPAL
print("🎉 TOBIAS BOT PRO - INICIALIZAÇÃO FINAL")
print("=" * 50)

# Info do sistema
print(f"🐍 Python: {sys.version.split()[0]}")
print(f"🔥 PyTorch: {torch.__version__}")
print(f"🎯 Device: {'GPU' if torch.cuda.is_available() else 'CPU'}")

if torch.cuda.is_available():
    print(f"🚀 GPU: {torch.cuda.get_device_name(0)}")

print("\n🚀 Carregando interface...")
bot = create_interface()

if bot:
    print("\n✅ TUDO PRONTO!")
    print("👆 Use a interface acima")
    print("\n💡 COMANDOS EXTRAS:")
    print("• test_url('URL')     - Testa URL")
    print("• fix_youtube_403()   - Corrige erro 403")
    
    print(f"\n📊 STATUS:")
    print(f"   🤖 Modelo: {bot.model_size}")
    print(f"   💻 Device: {bot.device}")
    print(f"   🧠 Status: {'✅ Pronto' if bot.model else '❌ Erro'}")
else:
    print("❌ Erro na inicialização")

print("=" * 50)

# =============================================================================
# CÉLULA 9: MARKDOWN - FOOTER
# =============================================================================
"""
Copie este MARKDOWN em uma célula de texto:

---

# 🎉 **Parabéns! Tobias Bot Pro funcionando!**

## 🚀 **Próximos passos:**

1. **Use a interface acima** para transcrever vídeos
2. **Compartilhe este notebook** com amigos
3. **Contribua no GitHub** com melhorias
4. **Deixe uma ⭐** se gostou do projeto

## 💡 **Casos de uso:**

- 📚 **Estudantes**: Transcrever aulas gravadas  
- 🎙️ **Podcasters**: Converter episódios para texto
- 📰 **Jornalistas**: Transcrever entrevistas
- 🎬 **Criadores**: Gerar legendas automaticamente

## 🆘 **Precisa de ajuda?**

- 🐛 **Bug?** [Abra issue no GitHub](https://github.com/Jamilly_Nichele/tobias-bot-pro/issues)
- 💡 **Sugestão?** [Envie pull request](https://github.com/Jamilly_Nichele/tobias-bot-pro/pulls)  
- 💬 **Dúvidas?** [Entre em contato](https://linkedin.com/in/seu_perfil)

---

<div align="center">

**🤖 Tobias Bot Pro** | **v2.0.0** | **MIT License**

Desenvolvido com ❤️ para a comunidade

[![GitHub](https://img.shields.io/badge/GitHub-Projeto-blue)](https://github.com/Jamilly_Nichele/tobias-bot-pro)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://linkedin.com/in/seu_perfil)

</div>
"""
