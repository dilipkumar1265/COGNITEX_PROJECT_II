let lastState = null;

window.updateUI = function(data) {
  if (JSON.stringify(data) === JSON.stringify(lastState)) return;
  lastState = data;

  document.getElementById("load").innerText = data.cognitive_load;
  document.getElementById("decision").innerText = data.decision;
  document.getElementById("execution").innerText = data.execution;
  document.getElementById("advice").innerText = data.advice;
  document.getElementById("reflection").innerText = data.reflection;
};
