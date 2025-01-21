const gameContainer = document.getElementById("game");
const sceneTitle = document.getElementById("scene-title");
const sceneText = document.getElementById("scene-text");
const choicesContainer = document.getElementById("choices");
const saveButton = document.getElementById("save");
const loadButton = document.getElementById("load");
const startButton = document.getElementById("start");

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

// Handle Save Game button
saveButton.addEventListener("click", () => {
  fetch("/save", { method: "POST" })
    .then((response) => response.json())
    .then((data) => alert(data.message));
});

// Handle Load Game button
loadButton.addEventListener("click", () => {
  fetch("/load")
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        alert(data.error);
      } else {
        loadScene(data.player_state.current_scene);
      }
    });
});

// Initialize game with Start button
document.addEventListener("DOMContentLoaded", () => {
  gameContainer.style.display = "none"; // Hide game content on load
});

// Start the game when the Start button is clicked
startButton.addEventListener("click", () => {
  loadScene("start"); // Load the initial scene
  startButton.style.display = "none"; // Hide the Start button
  gameContainer.style.display = "block"; // Show the game content
});
