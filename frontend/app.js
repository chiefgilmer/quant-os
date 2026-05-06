
console.log("JS LOADED");

document.addEventListener("DOMContentLoaded", () => {

  const uploadBtn = document.getElementById("uploadBtn");
  const refreshBtn = document.getElementById("refreshBtn");

  uploadBtn.addEventListener("click", uploadFile);
  refreshBtn.addEventListener("click", loadData);

  loadData();
});

async function loadData() {
  console.log("LOADING DATA");

  try {
    const res = await fetch("/run");
    const data = await res.json();

    let p = "";
    for (let k in data.portfolio) {
      p += `<div>💼 ${k}: ${data.portfolio[k]}</div>`;
    }
    document.getElementById("portfolio").innerHTML = p;

  } catch (err) {
    console.error("LOAD ERROR:", err);
  }
}

async function uploadFile() {
  console.log("UPLOAD BUTTON CLICKED");

  const file = document.getElementById("fileInput").files[0];

  if (!file) {
    alert("Please select a file first");
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
