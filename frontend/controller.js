// ✅ Expose to Python at top-level (not inside event listeners)
eel.expose(hideLoader);
function hideLoader() {
  $("#Loader").attr("hidden", true);
  $("#FaceAuth").attr("hidden", false);
}

eel.expose(hideFaceAuth);
function hideFaceAuth() {
  console.log("✅ hideFaceAuth() triggered");
  $("#FaceAuth").attr("hidden", true);
  $("#FaceAuthSuccess").attr("hidden", false);
}


eel.expose(hideFaceAuthSuccess);
function hideFaceAuthSuccess() {
  $("#FaceAuthSuccess").attr("hidden", true);
  $("#HelloGreet").attr("hidden", false);
}

eel.expose(hideStart);
function hideStart() {
  $("#Start").attr("hidden", true);
  setTimeout(function () {
    $("#Oval").addClass("animate__animated animate__zoomIn");
  }, 1000);
  setTimeout(function () {
    $("#Oval").attr("hidden", false);
  }, 1000);
}

eel.expose(ShowHood);
function ShowHood() {
  $("#Oval").attr("hidden", false);
  $("#SiriWave").attr("hidden", true);
}

// this is for controller.js
function showJarvisMessage(message) {
    const msgBox = document.getElementById('jarvis-response');
    msgBox.innerText = message;

    // Optional: Add a fade animation or delay
    msgBox.style.opacity = 1;
    setTimeout(() => {
        msgBox.style.opacity = 0;
    }, 3000); // hides after 3s
}

eel.expose(showJarvisMessage);

// 🎤 Mic button event
document.getElementById("MicBtn").addEventListener("click", async () => {
  console.log("🎙 Mic button clicked");
  const messageBox = document.querySelector(".siri-message");

  if (messageBox) messageBox.textContent = "Listening...";
  // eel.DisplayMessage("Listening...");
  $("#Oval").attr("hidden", true);
  $("#SiriWave").attr("hidden", false);

  try {
    await eel.play_assistant_sound()();
    const result = await eel.takeAllCommands()();
    console.log("Voice Result:", result);

    if (result && result !== "Sorry, I didn't get that.") {
      if (typeof eel.senderText === "function") eel.senderText(result);
      if (typeof eel.DisplayMessage === "function") eel.DisplayMessage("You said", result);
      else if (messageBox) messageBox.textContent = `You said: ${result}`;
    } else {
      if (typeof eel.DisplayMessage === "function") {
        eel.DisplayMessage("Sorry, I didn't catch that.");
      }
    }

    setTimeout(() => {
      ShowHood();
    }, 2000);

  } catch (error) {
    console.error("🚨 Error calling takeAllCommands:", error);
    if (typeof eel.DisplayMessage === "function") {
      eel.DisplayMessage("Something went wrong.");
    } else if (messageBox) {
      messageBox.textContent = "Error processing voice input.";
    }

    setTimeout(() => {
      ShowHood();
    }, 2000);
  }
});
