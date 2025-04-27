# FURIA-Bot

&#x20;&#x20;

> [Versão em Português](./README.pt.md)

---

## About the Project

**FURIA-Bot** is a lightweight web application developed for a technical challenge, designed to simulate an interactive experience for fans of FURIA's **CS2** team.

Built with **Python (Flask)**, **HTML/CSS**, and **JavaScript**, the bot retrieves live information from **Wikipedia's API**, formats it cleanly, and delivers it through a chat interface inspired by FURIA’s official visual identity: minimalistic, black-and-white, modern.

This project emphasizes **efficiency, clean code, real-time data**, and a **fan-centric user experience**.

---

## Key Features

- **Current Roster**: Displays active players and coaches, including their roles and real names (with tooltips).
- **Tournament History**: Lists FURIA’s notable championship placements with direct links for more information.
- **Social Media Links**: Provides quick access to FURIA’s official website and main social channels.
- **Trivia Mode**: Fun facts and curiosities about FURIA, presented randomly to enhance fan engagement.
- **Cheering Simulator**: Fans can trigger randomized chants and celebration messages, recreating the energy of live tournaments.
- **Live Match Feed**: Users can activate a simulated real-time feed of match updates, creating a dynamic and immersive experience.
- **Conversational UX**: Natural typing delay, welcome messages, and structured responses create a lively interaction.
- **Custom Styling**: FURIA’s black-and-white branding fully respected, with centered logo, subtle animations, and smooth user interface.

---

## Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **External APIs**: Wikipedia MediaWiki API
- **Hosting Suggestions**: Compatible with Render, Railway, Vercel, etc.

---

## Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/lucasmartins-92/furia-bot.git
   cd furia-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   flask run
   ```

4. Open your browser at:

   ```
   http://127.0.0.1:5000
   ```

---

## Project Structure

```plaintext
furia-bot/
│
├── app.py
├── intents.py
├── social_media_links.py
├── trivia.py
├── chants.py
├── statuses.py
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

## Sources and Data References

- [Wikipedia - FURIA Esports](https://pt.wikipedia.org/wiki/Furia_Esports)
- [HLTV - FURIA Team Profile](https://www.hltv.org/team/8297/furia)
- [Liquipedia - FURIA](https://liquipedia.net/counterstrike/FURIA)

Trivia facts are based on publicly verifiable information from reliable sources.

---

## Challenge Requirements

- Create a functional chatbot for FURIA fans
- Deliver a prototype with real data integration and dynamic interaction
- Think like a fan: deliver roster, history, social media, trivia, and live experience
- Style according to FURIA’s brand
- Clear, modular, professional code

---

## Author

Developed with passion for esports, fans, and quality software engineering.

Lucas Martins de Andrade\
[LinkedIn](https://www.linkedin.com/in/lucas-martins-de-andrade-64043724/)\
[GitHub](https://github.com/lucasmartins-92)
