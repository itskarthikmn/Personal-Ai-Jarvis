/**animation of text file that is for "Ask me Anything" */
$(document).ready(function () {

  eel.init()(); // gives time for expose bindings to load
  $(".text").textillate({
    loop: true,
    speed: 1500,
    sync: true,
    in: {
      effect: "bouneIn",
    },
    out: {
      effect: "bounceOut",
    },
  });
  /**animation of text file that is for "Hello, I am Your Assistant" */
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });

  //siri wave annimation
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 940,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    height: 200,
    autostart: true,
    waveColor: "#ff0000",
    waveOffset: 0,
    rippleEffect: true,
    rippleColor: "#ffffff",
  });

  /** Mic button function that helps when mic button is clicked it will turn on siri wave*/
  $("#MicBtn").click(function () {
    eel.play_assistant_sound();
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.takeAllCommands()()
  });

  function doc_keyUp(e) {
    // check for ctrl +K

    if (e.key === "k" && e.ctrlKey) {
      eel.play_assistant_sound();
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.takeAllCommands()()
    }
  }
  document.addEventListener("keyup", doc_keyUp, false);

  function PlayAssistant(message) {
    if (message != "") {
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.takeAllCommands(message);
      $("#chatbox").val("");
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    } else {
      console.log("Empty message, nothing sent."); // Log if the message is empty
    }
  }

  function ShowHideButton(message) {
    if (message.length == 0) {
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    } else {
      $("#MicBtn").attr("hidden", true);
      $("#SendBtn").attr("hidden", false);
    }
  }
  $("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    console.log("Current chatbox input: ", message); // Log input value for debugging
    ShowHideButton(message);
  });

  $("#SendBtn").click(function () {
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });
  $("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
      let message = $("#chatbox").val();
      PlayAssistant(message);
    }
  });
  eel.expose(senderText);
  function senderText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-end mb-4">
          <div class = "width-size">
          <div class="sender_message">${message}</div>
      </div>`;

      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
  eel.expose(receiverText);
  function receiverText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-start mb-4">
          <div class = "width-size">
          <div class="receiver_message">${message}</div>
          </div>
      </div>`;

      // Scroll to the bottom of the chat box
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
});


