"""
Setup configuration for Tobias Bot Pro
Sistema Avançado de Transcrição de Vídeos do YouTube
"""

from setuptools import setup, find_packages
import pathlib

# Diretório atual
HERE = pathlib.Path(__file__).parent

# README para descrição longa
README = (HERE / "README.md").read_text(encoding="utf-8")

# Requirements
REQUIREMENTS = (HERE / "requirements.txt").read_text(encoding="utf-8").splitlines()

setup(
    name="tobias-bot-pro",
    version="2.0.0",
    author="[SEU NOME]",
    author_email="[SEU EMAIL]",
    description="Sistema Avançado de Transcrição de Vídeos do YouTube usando IA",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/[SEU_USERNAME]/tobias-bot-pro",
    project_urls={
        "Bug Reports": "https://github.com/[SEU_USERNAME]/tobias-bot-pro/issues",
        "Source": "https://github.com/[SEU_USERNAME]/tobias-bot-pro",
        "Colab Demo": "https://colab.research.google.com/github/[SEU_USERNAME]/tobias-bot-pro/blob/main/Tobias_Bot_Pro_Complete.ipynb"
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "tobias-bot=tobias_bot:main",
        ],
    },
    keywords=[
        "youtube", "transcription", "whisper", "ai", "speech-to-text",
        "audio", "video", "machine-learning", "automation"
    ],
    zip_safe=False,
)
