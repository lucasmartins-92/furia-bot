import requests, re


def get_roster_and_coaches_from_wikipedia():
    url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "format": "json",
        "page": "Furia_Esports",
        "prop": "wikitext",
        "section": 5,
        "formatversion": 2,
    }

    headers = {
        "User-Agent": "FURIAChatBot/1.0 (https://github.com/lucasmartins-92/furia-bot; lucas.mart19+furiabot@gmail.com)"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()
    text = data["parse"]["wikitext"]

    lines = text.split("|")
    players = []
    coaches = []

    for line in lines:
        if line.startswith("jogador") or line.startswith("treinador"):
            parts = [re.sub(r"{{.*?}}", "", p).strip() for p in line.split("{{!!}}")]
            if len(parts) == 4:
                entry = {
                    "nickname": re.sub(
                        r"\[\[|\]\]", "", parts[0].split("=")[-1].strip()
                    ),
                    "real_name": parts[1],
                    "nationality": parts[2],
                    "role": re.sub(r"\{\{|\}\}", "", parts[3]),
                }
                if line.startswith("jogador"):
                    players.append(entry)
                else:
                    coaches.append(entry)
                print(players)

    return {"players": players, "coaches": coaches}


def clean_wikilink(text):
    # Remove style and bgcolor cleanly
    text = re.sub(r'style="[^"]*"', "", text)
    text = re.sub(r"bgcolor=[^\|]*\|", "", text)

    # Remove wiki links [[Page|Display]] and [[Display]]
    text = re.sub(r"\[\[(?:[^\|\]]*\|)?([^\]]+)\]\]", r"\1", text)

    # Remove empty attributes and weird spacing
    text = text.replace("&nbsp;", " ")
    text = text.replace("|", "")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_tournament_history_from_wikipedia():
    url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "format": "json",
        "page": "Furia_Esports",
        "prop": "wikitext",
        "section": 4,
        "formatversion": 2,
    }

    headers = {
        "User-Agent": "FURIAChatBot/1.0 (https://github.com/lucasmartins-92/furia-bot; lucas.mart19+furiabot@gmail.com)"
    }

    response = requests.get(url, params=params, headers=headers)
    text = response.json()["parse"]["wikitext"]

    row_blocks = text.split("|-")
    history = []

    for block in row_blocks:
        lines = block.strip().splitlines()
        lines = [line.strip() for line in lines if line.strip().startswith("|")]

        if len(lines) >= 5:
            cols = [clean_wikilink(line[1:].strip()) for line in lines]

            history.append(
                {
                    "position": cols[0],
                    "championship": cols[1],
                    "result": cols[2],
                    "opponent": cols[3],
                    "prize": cols[4],
                }
            )

    return {"history": history}
