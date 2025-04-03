document.addEventListener("DOMContentLoaded", function () {
  const showFormBtn = document.getElementById("show-form-btn");
  const form = document.getElementById("upload-form");
  const input = document.getElementById("doc-upload");
  const uploadBox = document.getElementById("upload-box");
  const uploadText = document.getElementById("upload-text");

  // Prikaz forme kada se klikne "Dodaj"
  if (showFormBtn && form) {
    showFormBtn.addEventListener("click", function () {
      form.style.display = "flex";
      form.style.flexDirection = "column";
      form.style.gap = "20px";
      showFormBtn.style.display = "none";
    });
  }

  // Prikaz imena datoteke kada je odabrana
  if (input && uploadText) {
    input.addEventListener("change", function () {
      if (input.files.length > 0) {
        const file = input.files[0];
        uploadText.textContent = file.name;
        uploadText.style.fontSize = "14px";
        uploadText.style.color = "#333";
      } else {
        resetUploadText();
      }
    });
  }

  // Drag & drop funkcionalnost
  if (uploadBox) {
    uploadBox.addEventListener("dragover", function (e) {
      e.preventDefault();
      uploadBox.classList.add("drag-over");
    });

    uploadBox.addEventListener("dragleave", function () {
      uploadBox.classList.remove("drag-over");
    });

    uploadBox.addEventListener("drop", function (e) {
      e.preventDefault();
      uploadBox.classList.remove("drag-over");

      const files = e.dataTransfer.files;
      if (files.length > 0) {
        const file = files[0];
        if (validateWordFile(file)) {
          input.files = files;
          uploadText.textContent = file.name;
          uploadText.style.fontSize = "14px";
          uploadText.style.color = "#333";
        } else {
          uploadText.textContent = "Samo .doc/.docx!";
          uploadText.style.color = "red";
        }
      }
    });
  }

  function resetUploadText() {
    uploadText.textContent = "+";
    uploadText.style.fontSize = "48px";
    uploadText.style.color = "#888";
  }

  function validateWordFile(file) {
    const allowedTypes = [
      "application/msword",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ];
    return allowedTypes.includes(file.type);
  }
});
