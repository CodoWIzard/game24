const gameContainer = document.getElementById("game");
const sceneTitle = document.getElementById("scene-title");
const sceneText = document.getElementById("scene-text");
const choicesContainer = document.getElementById("choices");
const saveButton = document.getElementById("save");
const loadButton = document.getElementById("load");

function loadScene(sceneId) {
  fetch(`/scene?scene_id=${sceneId}`)
    .then((response) => response.json())
    .then((scene) => {
      sceneTitle.textContent = `Scene: ${sceneId}`;
      sceneText.textContent = scene.text;
      choicesContainer.innerHTML = "";
      Object.entries(scene.choices).forEach(([choiceText, nextScene]) => {
        const button = document.createElement("button");
        button.textContent = choiceText;
        button.className = "px-4 py-2 bg-gray-700 hover:bg-gray-800";
        button.onclick = () => makeChoice(nextScene);
        choicesContainer.appendChild(button);
      });
    });
}

function makeChoice(nextScene) {
  fetch("/choice", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ choice: nextScene }),
  })
    .then((response) => response.json())
    .then(() => loadScene(nextScene));
}

saveButton.addEventListener("click", () => {
  fetch("/save", { method: "POST" })
    .then((response) => response.json())
    .then((data) => alert(data.message));
});

loadButton.addEventListener("click", () => {
  fetch("/load")
    .then((response) => response.json())
    .then(() => loadScene("start"));
});

document.addEventListener("DOMContentLoaded", () => loadScene("start"));
