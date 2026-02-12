let keystrokes = 0;
let errorCount = 0;
let typingStart = null;
let lastActivity = Date.now();
const taskStart = Date.now();

// Keyboard tracking
document.addEventListener("keydown", e => {
  if (!typingStart) typingStart = Date.now();
  keystrokes++;
  if (e.key === "Backspace") errorCount++;
  lastActivity = Date.now();
});

// Mouse tracking
document.addEventListener("mousemove", () => {
  lastActivity = Date.now();
});

// Collect metrics SAFELY
function collectMetrics() {
  let typing_speed = 0;

  if (typingStart) {
    const minutes = (Date.now() - typingStart) / 60000;
    typing_speed = minutes > 0 ? Math.round(keystrokes / minutes) : 0;
  }

  return {
    typing_speed,
    time_on_task: Math.round((Date.now() - taskStart) / 1000),
    error_count: errorCount,
    inactivity: Math.round((Date.now() - lastActivity) / 1000)
  };
}

// Send to backend every 8 seconds
// SEND EVERY 8 SECONDS (NOT 4)
setInterval(() => {
  fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(collectMetrics())
  })
  .then(r => r.json())
  .then(d => window.updateUI(d));
}, 8000);


