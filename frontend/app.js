// LOAD DASHBOARD DATA
async function loadData() {
  const res = await fetch("/run");
  const data = await res.json();

  // PORTFOLIO DISPLAY
  let portfolioHTML = "";
  for (let key in data.portfolio) {
    portfolioHTML += `<div class="card">💼 ${key}: ${data.portfolio[key]} shares</div>`;
  }
  document.getElementById("portfolio").innerHTML = portfolioHTML;

  // ALLOCATION DISPLAY
  let allocationHTML = "";
  if (data.allocation) {
    for (let key in data.allocation) {
      allocationHTML += `<div class="card">📊 ${key}: ${(data.allocation[key]*100).toFixed(1)}%</div>`;
    }
  }
  document.getElementById("allocation").innerHTML = allocationHTML;

  // SIGNALS DISPLAY
  let signalsHTML = "";
  if (data.signals) {
    data.signals.forEach(sig => {
      signalsHTML += `<div class="card">
        📈 ${sig.ticker} → ${sig.signal} (score ${sig.score})
      </div>`;
    });
  }
  document.getElementById("signals").innerHTML = signalsHTML;
}

// FILE UPLOAD FUNCTION
async function uploadFile() {
  const file = document.getElementById("fileInput").files[0];

  if (!file) {
    alert("Please select a file first");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  await fetch("/upload", {
    method: "POST",
    body: formData
  });

  alert("Portfolio uploaded successfully!");
  loadData();
}

// AUTO REFRESH EVERY 10 SECONDS
setInterval(loadData, 10000);

// INITIAL LOAD
loadData();
  });

  alert("Portfolio uploaded successfully!");
  loadData();
}

// AUTO REFRESH EVERY 10 SECONDS
setInterval(loadData, 10000);

// INITIAL LOAD
loadData();
