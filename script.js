document.getElementById("salaryForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = isNaN(value) ? value : parseFloat(value);
  });

  const resultBox = document.getElementById("result");
  resultBox.classList.add("hidden");

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();

    if (res.ok) {
      resultBox.textContent = `💰 Predicted Salary: $${result.salary.toFixed(2)}`;
      resultBox.className = "result-box success";
    } else {
      resultBox.textContent = `⚠️ Error: ${result.detail}`;
      resultBox.className = "result-box error";
    }
  } catch (err) {
    resultBox.textContent = `❌ Network error: ${err.message}`;
    resultBox.className = "result-box error";
  }

  resultBox.classList.remove("hidden");
});
