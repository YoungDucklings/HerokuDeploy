const likeButton = document.querySelectorAll('#like-button')
let percentage = document.getElementById('percentage')
let selectNum = 0
const selected = new Set

// percentage.style.width

for (let i = 0; i < likeButton.length; i++) {
  likeButton[i].addEventListener('click', e => {
    const starId = e.target.dataset.id
    axios.get(`/stars/${starId}/like/`)
      .then(res => {
        if (res.data.liked) {
          // unlike button
          if (!(selected.has(starId))) {
            e.target.removeAttribute("style")
            selectNum++
            selected.add(starId)
            percentage.setAttribute("style", `width:${selectNum/20 * 100}%`)
          }
        } else {
          // like button
          e.target.setAttribute(
            "style", "color: transparent; -webkit-text-stroke-width: 1px; -webkit-text-stroke-color: red;");
          selectNum--
          selected.delete(starId)
          percentage.setAttribute("style", `width:${selectNum/20 * 100}%`)
        }
      })
  })
}

function mouseClick(n, movie_id) {
  if (!(selected.has(movie_id))) {
    selectNum++
    selected.add(movie_id)
    percentage.setAttribute("style", `width:${selectNum/20 * 100}%`)
  }
  for (let i = n; i > 0; i--) {
    document.getElementById(String(movie_id)+String(i)).setAttribute(
      "style", "color: gold; text-shadow: 3px 5px grey");
  }
  for (let i = n + 1; i < 6; i++) {
    document.getElementById(String(movie_id)+String(i)).removeAttribute(
      "style");
  }
  axios.get(`/movies/${movie_id}/${n}/rate/`)
}