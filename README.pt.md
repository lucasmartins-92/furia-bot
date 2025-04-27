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

- **Elenco Atual**: Mostra os jogadores e treinadores ativos, incluindo funções e nomes reais (com tooltips).
- **Histórico de Campeonatos**: Lista as principais colocações da FURIA em campeonatos, com links diretos para mais informações.
- **Redes Sociais**: Links rápidos para o site oficial e redes sociais da FURIA.
- **Modo Curiosidades**: Fatos e curiosidades sobre a FURIA, apresentados aleatoriamente para engajar o fã.
- **Simulador de Torcida**: Permite que fãs disparem gritos de torcida aleatórios, simulando a energia de um evento ao vivo.
- **Modo Live Feed**: Permite ativar um fluxo simulado de atualizações em tempo real durante as partidas, criando uma experiência mais dinâmica e imersiva.
- **Experiência Conversacional**: Respostas com delay de digitação, mensagens de boas-vindas e estrutura de conversa que simulam interações reais.
- **Estilização Personalizada**: Identidade visual da FURIA respeitada, com logo centralizado, animações sutis e interface fluida.

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
   git clone https://github.com/seuusuario/furia-bot.git
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
- Entregar um protótipo com integração de dados reais e interação dinâmica
- Pensar como fã: disponibilizar elenco, histórico, redes sociais, curiosidades e experiência ao vivo
- Respeitar a identidade visual da FURIA
- Código claro, modular e profissional

---

## Autor

Desenvolvido com paixão por esports, pelos fãs e por engenharia de software de qualidade.

Lucas Martins de Andrade\
[LinkedIn](https://www.linkedin.com/in/lucas-martins-de-andrade-64043724/)\
[GitHub](https://github.com/lucasmartins-92)
