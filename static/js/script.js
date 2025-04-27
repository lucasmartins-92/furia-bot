const chatBox = document.getElementById('chat-box');
const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');

let liveFeedActive = false;
let liveFeedInterval = null;
let waitingForLiveStopConfirmation = false;

const yesAnswers = ["sim", "quero", "bora", "manda", "vai", "por favor"];
const noAnswers = ["não", "nao", "pare", "parar", "cancela", "voltar"];

const liveUpdates = [
    "FURIA faz 5-2 contra a NAVI!",
    "Clutch espetacular do KSCERATO!",
    "FURIA leva o primeiro half, 8-7!",
    "yuurih brilha com 3 eliminações seguidas!",
    "Timeout tático da Team Liquid!",
    "FURIA fecha o mapa 16-12, vitória!",
    "Partida pausada por problemas técnicos.",
    "FURIA volta forte e vence o pistol round!",
    "É ponto atrás de ponto! 14-10 pra FURIA.",
    "Molodoy com highlight impressionante!"
];

function getRandomLiveUpdate() { // Simula atualizações ao vivo
    return liveUpdates[Math.floor(Math.random() * liveUpdates.length)];
}


window.onload = () => {
    appendMessage("FURIA-Bot", "Fala, fã da FURIA! O que você quer saber sobre a nossa equipe de CS2? Posso te contar sobre nosso time, campeonatos, rede sociais, e até curiosidades! 🐾");
};

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = input.value.trim();
    appendMessage("You", message);
    input.value = "";

    if (waitingForLiveStopConfirmation) {
        if (yesAnswers.includes(message.toLowerCase())) {
            appendMessage('FURIA-Bot', "Atualizações ao vivo encerradas. Bora continuar o papo!");
            waitingForLiveStopConfirmation = false;
            return;
        } else if (noAnswers.includes(message.toLowerCase())) {
            appendMessage('FURIA-Bot', "Beleza, seguimos na cobertura! 🎯");

            liveFeedActive = true;
            liveFeedInterval = setInterval(() => {
                appendMessage('FURIA-Bot', getRandomLiveUpdate());
            }, 5000);

            waitingForLiveStopConfirmation = false;
            return;
        }
    }

    if (liveFeedActive) {
        clearInterval(liveFeedInterval);
        liveFeedActive = false;
        appendMessage('FURIA-Bot', "Quer encerrar as atualizações ao vivo? (Responda 'sim' ou 'não')");
        waitingForLiveStopConfirmation = true;
        return;
    }

    if (message.toLowerCase() === "sim" && lastBotMessage.includes("atualizações em tempo real")) {
        liveFeedActive = true;
        appendMessage('FURIA-Bot', "Beleza! Atualizações ao vivo iniciadas. Se quiser interromper, basta mandar qualquer mensagem.");

        liveFeedInterval = setInterval(() => {
            appendMessage('FURIA-Bot', getRandomLiveUpdate());
        }, 5000);
        return;
    }

    const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await res.json();
    appendMessage("FURIA-Bot", data.reply, 500);
});

let lastBotMessage = "";

function appendMessage(sender, text, delay = 0) {
    const div = document.createElement('div');
    const isBot = sender === "FURIA-Bot";
    const icon = isBot ? `<img src="/static/img/panther-icon.png" class="icon">` : "";

    if (isBot && delay > 0) {
        const typingDiv = document.createElement('div');
        typingDiv.id = "typing";
        typingDiv.innerHTML = `${icon} <strong>${sender}:</strong> <em>Digitando</em>`;
        chatBox.appendChild(typingDiv);
        chatBox.scrollTop = chatBox.scrollHeight;

        setTimeout(() => {
            typingDiv.remove();
            div.innerHTML = `${icon} <strong>${sender}:</strong> ${text.replace(/\n/g, "<br>")}`;
            chatBox.appendChild(div);
            chatBox.scrollTop = chatBox.scrollHeight;

            if (isBot) lastBotMessage = text;
        }, delay);
    } else {
        div.innerHTML = `${icon} <strong>${sender}:</strong> ${text.replace(/\n/g, "<br>")}`;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;

        if (isBot) lastBotMessage = text;
    }
}