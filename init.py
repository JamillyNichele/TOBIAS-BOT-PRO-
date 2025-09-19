"""
Tobias Bot Pro - Sistema Avançado de Transcrição de Vídeos do YouTube

Este pacote fornece ferramentas para transcrição automática de vídeos
do YouTube usando IA de última geração.

Classes principais:
    TobiasBotPro: Classe principal para transcrição
    
Funções utilitárias:
    test_url: Testa URLs do YouTube
    fix_youtube_403: Corrige problemas de bloqueio
"""

from .tobias_bot import TobiasBotPro, test_url, fix_youtube_403

__version__ = "2.0.0"
__author__ = "Jamilly Nichele"
__email__ = "Jamillynichele@gmail.com"

__all__ = [
    "TobiasBotPro",
    "test_url", 
    "fix_youtube_403"
]
