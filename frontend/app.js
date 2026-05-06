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
      p += `<div>💼 ${k}: ${data.portfolio[k]}</div>`;
    }
    document.getElementById("portfolio").innerHTML = p;

    let s = "";
    if (data.signals) {
      data.signals.forEach(sig => {
        s += `<div>📈 ${sig.ticker} → ${sig.signal}</div>`;
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
    return;
  }

  console.log("FILE:", file.name);

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch("/upload", {
      method: "POST",
      body: formData
    });

    console.log("STATUS:", res.status);

    const data = await res.json();
    console.log("RESPONSE:", data);

    alert("Upload complete");
    loadData();

  } catch (err) {
    console.error("UPLOAD ERROR:", err);
    alert("Upload failed");
  }
}

setInterval(loadData, 10000);
loadData();
