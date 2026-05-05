async function loadData() {
  const res = await fetch("/run");
  const data = await res.json();

  const container = document.getElementById("signals");
  container.innerHTML = "";

  data.signals.forEach(s => {
    let className = "card";

    if (s.signal === "BUY") className += " buy";
    if (s.signal === "SELL") className += " sell";
    if (s.signal === "HOLD") className += " hold";

    container.innerHTML += `
      <div class="${className}">
        <h2>${s.ticker}</h2>
        <p>Signal: ${s.signal}</p>
        <p>Score: ${s.score}</p>
      </div>
    `;
  });
}

setInterval(loadData, 10000);
loadData();
