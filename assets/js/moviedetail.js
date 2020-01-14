function mouseClick(n) {
  for (let i = n; i > 0; i--) {
    document.getElementById(i).setAttribute(
      "style", "color: gold; text-shadow: 3px 5px grey");
  }
  for (let i = n + 1; i < 6; i++) {
    document.getElementById(i).removeAttribute(
      "style");
  }
  movie_id = document.querySelector('#score-box').dataset.id
  axios.get(`/movies/${movie_id}/${n}/rate/`)
}

function linktoLogin() {
  axios.get('/accounts/login/')
}

  function castInfo(n) {
    document.getElementById(`cast${n}`).removeAttribute("style");
  }

  function hideCastInfo(n) {
    document.getElementById(`cast${n}`).setAttribute("style", "display:none");
  }

  function buttonClick(e, tabName) {
    let tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    e.currentTarget.className += " active";
  }