async function loadData() {
  const res = await fetch("/run");
  const data = await res.json();

  // PORTFOLIO
  let p = "";
  for (let k in data.portfolio) {
    p += `<div class="card">💼 ${k}: ${data.portfolio[k]}</div>`;
  }
  document.getElementById("portfolio").innerHTML = p;

  // SIGNALS
  let s = "";
  data.signals.forEach(sig => {
    s += `<div class="card">📈 ${sig.ticker} → ${sig.signal}</div>`;
  });
  document.getElementById("signals").innerHTML = s;
}

// UPLOAD
async function uploadFile() {
  const file = document.getElementById("fileInput").files[0];

  const formData = new FormData();
  formData.append("file", file);

  await fetch("/upload", {
    method: "POST",
    body: formData
  });

  loadData();
}

setInterval(loadData, 10000);
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
