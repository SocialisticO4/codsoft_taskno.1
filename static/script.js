function sendMessage() {
  const userInputElement = document.getElementById("user-input");
  const userInput = userInputElement.value;
  userInputElement.selectedIndex = 0;

  if (!userInput) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user">User: ${userInput}</div>`;

  fetch("/get_response", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      chatBox.innerHTML += `<div class="bot">Bot: ${data.response}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    });
}
