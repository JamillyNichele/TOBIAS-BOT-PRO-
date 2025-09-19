# 🤝 Contribuindo para o Tobias Bot Pro

Obrigado pelo interesse em contribuir! Este documento explica como você pode ajudar a melhorar o projeto.

## 🎯 Como Contribuir

### 🐛 Reportar Bugs

Encontrou um bug? Por favor:

1. **Verifique** se já não existe uma [issue](https://github.com/SEU_USERNAME/tobias-bot-pro/issues) sobre o problema
2. **Crie uma nova issue** com:
   - Título descritivo
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Informações do sistema (Python, OS, etc.)
   - Screenshots se aplicável

### 💡 Sugerir Melhorias

Tem uma ideia? Crie uma issue com:
- Descrição detalhada da funcionalidade
- Justificativa (por que seria útil)
- Exemplos de uso
- Possível implementação

### 🔧 Contribuir com Código

1. **Fork** o repositório
2. **Clone** seu fork: `git clone https://github.com/SEU_USERNAME/tobias-bot-pro.git`
3. **Crie uma branch**: `git checkout -b feature/minha-feature`
4. **Faça suas modificações**
5. **Teste** suas mudanças
6. **Commit**: `git commit -m "feat: adiciona nova funcionalidade"`
7. **Push**: `git push origin feature/minha-feature`
8. **Abra um Pull Request**

## 📋 Padrões de Desenvolvimento

### 🐍 Código Python

- **Estilo**: Siga PEP 8
- **Formatação**: Use `black` para formatação automática
- **Linting**: Use `flake8` para verificação
- **Type hints**: Use sempre que possível
- **Docstrings**: Documente todas as funções públicas

Exemplo:
```python
def minha_funcao(param: str) -> Optional[str]:
    """
    Descrição breve da função.
    
    Args:
        param: Descrição do parâmetro
        
    Returns:
        Descrição do retorno ou None se erro
    """
    # Implementação aqui
    pass
```

### 📝 Commits

Use conventional commits:

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` mudanças na documentação
- `style:` formatação, sem mudança de código
- `refactor:` refatoração sem mudança de funcionalidade
- `test:` adicionar ou modificar testes
- `chore:` mudanças de build, dependências, etc.

### 🧪 Testes

- Escreva testes para novas funcionalidades
- Execute `pytest` antes de enviar PR
- Mantenha cobertura de testes alta

## 🏗️ Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/SEU_USERNAME/tobias-bot-pro.git
cd tobias-bot-pro

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências de desenvolvimento
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Instalar em modo de desenvolvimento
pip install -e .
```

## 🎨 Áreas que Precisam de Ajuda

### 🔥 Prioridade Alta
- [ ] Melhorar tratamento de erros 403
- [ ] Otimizar uso de memória
- [ ] Adicionar mais testes
- [ ] Documentação da API

### 📈 Melhorias Futuras
- [ ] Suporte a outras plataformas (Spotify, SoundCloud)
- [ ] Interface web standalone
- [ ] API REST
- [ ] Processamento em lote
- [ ] Fine-tuning de modelos

### 🐛 Bugs Conhecidos
- [ ] Alguns vídeos muito longos podem dar timeout
- [ ] URLs com parâmetros extras às vezes falham
- [ ] Problemas intermitentes com pytube

## 💬 Comunicação

- **Issues**: Para bugs e sugestões
- **Discussions**: Para perguntas e ideias gerais
- **Email**: Jamillynichele@gmail.com para questões sensíveis

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [Licença MIT](LICENSE).

## 🙏 Reconhecimento

Todos os contribuidores serão listados no README. Obrigado por fazer o projeto melhor!

---

**Dúvidas?** Não hesite em perguntar! Estamos aqui para ajudar. 😊
