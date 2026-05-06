async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select a PDF file first");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch("/upload", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    console.log("UPLOAD RESPONSE:", data);

    alert("Portfolio uploaded successfully!");

    loadData(); // refresh dashboard

  } catch (err) {
    console.error("UPLOAD ERROR:", err);
    alert("Upload failed. Check console/logs.");
  }
