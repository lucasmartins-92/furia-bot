# FURIA-Bot

[![Built with Flask](https://img.shields.io/badge/Built%20with-Flask-blue)](https://flask.palletsprojects.com/)
[![Powered by Wikipedia](https://img.shields.io/badge/Data-Powered%20by%20Wikipedia-lightgrey)](https://www.wikipedia.org/)
[![Status](https://img.shields.io/badge/Status-Prototype-success)]()

> [English Version](./README.md)

---

## Sobre o Projeto

O **FURIA-Bot** é uma aplicação web criada para um desafio técnico, projetada para simular uma experiência interativa com fãs do time de **CS2** da FURIA.

Desenvolvido com **Python (Flask)**, **HTML/CSS** e **JavaScript**, o bot coleta informações em tempo real da **API da Wikipedia**, formata os dados de forma elegante e entrega as respostas através de uma interface conversacional inspirada na identidade visual oficial da FURIA: minimalista, preta e branca, moderna.

O projeto foca em **eficiência**, **código limpo**, **dados em tempo real** e uma **experiência de usuário centrada no fã**.

---

## Principais Funcionalidades

- **Elenco Atual**: Exibe jogadores e técnicos ativos, com funções e nomes reais (com tooltip ao passar o mouse).
- **Histórico de Campeonatos**: Lista as principais conquistas da FURIA, com link direto para mais informações.
- **Redes Sociais**: Acesso rápido ao site oficial e às principais redes da FURIA.
- **Modo Curiosidades**: Fatos divertidos e curiosidades sobre a FURIA apresentados aleatoriamente.
- **Experiência Conversacional**: Respostas com delay realista, mensagem de boas-vindas e interação fluida.
- **Design Customizado**: Layout respeitando a identidade visual oficial da FURIA.

---

## Tecnologias Utilizadas

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **APIs Externas**: API MediaWiki (Wikipedia)
- **Sugestões de Deploy**: Compatível com Render, Railway, Vercel, entre outros.

---

## Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucasmartins-92/furia-bot.git
   cd furia-bot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode a aplicação:
   ```bash
   flask run
   ```

4. Acesse pelo navegador:
   ```
   http://127.0.0.1:5000
   ```

---

## Estrutura do Projeto

```plaintext
furia-bot/
│
├── app.py
├── intents.py
├── social_media_links.py
├── trivia.py
├── requirements.txt
├── data
│   └── wikipedia_scraper.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       ├── logo-furia.svg
│       └── panther-icon.png
├── README.md
└── README.pt.md
```

---

## Fontes e Referências de Dados

- [Wikipedia - FURIA Esports](https://pt.wikipedia.org/wiki/Furia_Esports)
- [HLTV - FURIA Team Profile](https://www.hltv.org/team/8297/furia)
- [Liquipedia - FURIA](https://liquipedia.net/counterstrike/FURIA)

As curiosidades foram baseadas em informações públicas e verificáveis de fontes confiáveis.

---

## Requisitos do Desafio

- Criar um chatbot funcional para fãs da FURIA
- Entregar um protótipo com integração de dados reais
- Pensar como fã: entregar elenco, histórico, redes sociais e curiosidades
- Respeitar o visual da marca FURIA
- Código limpo, modular e profissional

---

## Autor

Desenvolvido com paixão por esports, pelos fãs e por engenharia de software de qualidade.

Lucas Martins de Andrade\
[LinkedIn](https://www.linkedin.com/in/lucas-martins-de-andrade-64043724/)\
[GitHub](https://github.com/lucasmartins-92)
