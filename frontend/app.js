console.log("JS LOADED");

async function loadData() {
  console.log("LOADING DATA...");

  try {
    const res = await fetch("/run");
    console.log("RUN STATUS:", res.status);

    const data = await res.json();
    console.log("RUN DATA:", data);

    let p = "";
    for (let k in data.portfolio) {
      p += `<div class="card">💼 ${k}: ${data.portfolio[k]}</div>`;
    }
    document.getElementById("portfolio").innerHTML = p;

    let s = "";
    if (data.signals) {
      data.signals.forEach(sig => {
        s += `<div class="card">📈 ${sig.ticker} → ${sig.signal}</div>`;
      });
    }
    document.getElementById("signals").innerHTML = s;

  } catch (err) {
    console.error("LOAD ERROR:", err);
  }
}

async function uploadFile() {
  console.log("UPLOAD CLICKED");

  const file = document.getElementById("fileInput").files[0];

  if (!file) {
    alert("Select a file first");
    console.warn("NO FILE SELECTED");
    return;
  }

  console.log("FILE SELECTED:", file.name);

  const formData = new FormData();
  formData.append("file", file);

  try {
    console.log("SENDING REQUEST TO /upload...");

    const res = await fetch("/upload", {
      method: "POST",
      body: formData
    });

    console.log("UPLOAD STATUS:", res.status);

    const data = await res.json();
    console.log("UPLOAD RESPONSE:", data);

    alert("Upload complete");
    loadData();

  } catch (err) {
    console.error("UPLOAD FAILED:", err);
    alert("Upload failed — check console");
  }
}

setInterval(loadData, 10000);
loadData();
