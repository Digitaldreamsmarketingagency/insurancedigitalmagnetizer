
var minimalUserResponseInMiliseconds = 100;
  var before = new Date().getTime();
  debugger;
  var after = new Date().getTime();
  if (after - before > minimalUserResponseInMiliseconds) { // user had to resume the script manually via opened dev tools 
    document.getElementById('test').innerHTML = 'on';
  }
  
const body = document.getElementsByTagName('body');
window.addEventListener("keydown", (event) => {
  if(event.ctrlKey && (event.key === "S" || event.key === "s")) {
     event.preventDefault();
     body[0].innerHTML = "sorry, you can't do this 💔"
  }

  if(event.ctrlKey && (event.key === "C")) {
    event.preventDefault();
    body[0].innerHTML = "sorry, you can't do this 💔"
  }
  if(event.ctrlKey && (event.key === "E" || event.key === "e")) {
     event.preventDefault();
     body[0].innerHTML = "sorry, you can't do this 💔"
  }
  if(event.ctrlKey && (event.key === "I" || event.key === "i")) {
     event.preventDefault();
     body[0].innerHTML = "sorry, you can't do this 💔";
  }
  if(event.ctrlKey && (event.key === "K" || event.key === "k")) {
     event.preventDefault();
     body[0].innerHTML = "sorry, you can't do this 💔";
  }
  if(event.ctrlKey && (event.key === "U" || event.key === "u")) {
     event.preventDefault();
     body[0].innerHTML = "sorry, you can't do this 💔";
  }
});
// stop right click
document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
});