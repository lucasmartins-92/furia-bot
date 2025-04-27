from flask import Flask, render_template, jsonify, request
from difflib import get_close_matches
from random import choice
from data.liquipedia_scraper import (
    get_roster_and_coaches_from_wikipedia,
    get_tournament_history_from_wikipedia,
)
from intents import INTENTS
from social_media_links import SOCIAL_LINKS
from trivia import TRIVIA_FACTS
from chants import CHEERING_PHRASES
from statuses import MATCH_STATUSES


app = Flask(__name__)


def match_input(user_input, intent_keywords, threshold=0.8):
    words = user_input.lower().split()
    for keyword in intent_keywords:
        matches = get_close_matches(keyword, words, n=1, cutoff=threshold)
        if matches:
            return True
    return False


def detect_intent(user_input):
    for intent, keywords in INTENTS.items():
        if match_input(user_input, keywords):
            return intent
    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/team")
def team_info():
    return jsonify({"roster": get_roster_and_coaches_from_wikipedia()["players"]})


@app.route("/api/coach")
def coach_info():
    return jsonify({"coaches": get_roster_and_coaches_from_wikipedia()["coaches"]})


@app.route("/api/history")
def tournament_history():
    return jsonify(get_tournament_history_from_wikipedia())


@app.route("/api/facts")
def get_fact():
    fact = choice(TRIVIA_FACTS)
    return jsonify({"fact": fact})


@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    intent = detect_intent(user_input)
    print(f"DEBUG: User input: '{user_input}' -> Detected intent: '{intent}'")

    if intent == "coach":
        coaches = get_roster_and_coaches_from_wikipedia()["coaches"]
        if not coaches:
            return jsonify(
                {"reply": "Não encontrei informação sobre os treinadores... 😔"}
            )

        lines = [format_roster_entry(c) for c in coaches]
        reply = "Nossos treinadores são:\n" + "\n".join(lines)
        return jsonify({"reply": reply})

    elif intent == "roster":
        players = get_roster_and_coaches_from_wikipedia()["players"]
        if not players:
            return jsonify({"reply": "Não encontrei informação sobre nosso time... 😔"})

        lines = [format_roster_entry(p) for p in players]
        reply = "Esse é o nosso time atual de CS2:\n" + "\n".join(lines)
        return jsonify({"reply": reply})

    elif intent == "history":
        history = get_tournament_history_from_wikipedia()["history"]
        if not history:
            return jsonify(
                {"reply": "Não encontrei informações sobre os campeonatos... 😔"}
            )

        lines = []
        for h in history:
            lines.append(f"{h['position']} - vs {h['opponent']} ({h['championship']})")

        reply = "Algumas conquistas da FURIA em CS2:\n" + "\n".join(lines)
        reply += "\n\nPara mais informações: <a href='https://pt.wikipedia.org/wiki/Furia_Esports#Conquistas_not%C3%A1veis' target='_blank'>Wikipedia</a>"

        return jsonify({"reply": reply})

    elif intent == "social":
        links = [
            f"<a href='{url}' target='_blank'>{name}</a>"
            for name, url in SOCIAL_LINKS.items()
        ]
        reply = "Siga a FURIA:\n" + "<br>".join(links)
        return jsonify({"reply": reply})

    elif intent == "facts":
        fact = choice(TRIVIA_FACTS)
        return jsonify({"reply": f"{fact}"})

    elif intent == "cheering":
        chant = choice(CHEERING_PHRASES)
        return jsonify({"reply": chant})

    elif intent == "match_status":
        status = choice(MATCH_STATUSES)
        return jsonify(
            {
                "reply": f"{status} Quer receber atualizações em tempo real? (Responda 'sim' ou 'não')"
            }
        )

    else:
        return jsonify({"reply": "Desculpa, ainda estou aprendendo... 😅"})


def format_roster_entry(entry):
    nickname = entry["nickname"]
    real_name = entry["real_name"]
    role = entry["role"]

    return f"<b title='{real_name}'>{nickname}</b> — {role}"


if __name__ == "__main__":
    app.run(debug=True)
