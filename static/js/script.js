const chatBox = document.getElementById('chat-box');
const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');


window.addEventListener('DOMContentLoaded', () => {
    appendMessage("FURIA-Bot", "Fala, fã da FURIA! O que você quer saber sobre a nossa equipe de CS2? Posso te contar sobre nosso time, campeonatos, rede sociais, e até curiosidades! 🐾");
});

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = input.value;
    appendMessage("You", message);
    input.value = "";

    const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await res.json();
    appendMessage("FURIA-Bot", data.reply, 500);
});

function appendMessage(sender, text, delay = 0) {
    const div = document.createElement('div');
    const isBot = sender === "FURIA-Bot";
    const icon = isBot ? `<img src="/static/img/panther-icon.png" class="icon">` : "";

    // Mostrar "digitando" durante o delay
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
        }, delay);
    } else {
        div.innerHTML = `${icon} <strong>${sender}:</strong> ${text.replace(/\n/g, "<br>")}`;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
