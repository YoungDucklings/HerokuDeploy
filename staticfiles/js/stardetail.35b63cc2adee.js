const likeButton = document.querySelector('#like-button')
const likeCount = document.querySelector('#like-count')
const likeAlert = document.querySelector('#like-alert')
const starName = document.querySelector('#star-name').innerText
likeButton.addEventListener('click', e => {
  const starId = e.target.dataset.id
  axios.get(`/stars/${starId}/like/`)
    .then(res => {
      if (res.data.liked) {
        // unlike button
        e.target.removeAttribute("style")
        e.target.setAttribute("style", "font-size: 100px;")
        likeAlert.innerText = "You like this star"
      } else {
        // like button
        e.target.setAttribute(
          "style", "color: transparent; -webkit-text-stroke-width: 1px; -webkit-text-stroke-color: red; font-size: 100px;");
        likeAlert.innerText = "Pick this star"
      }
      if (res.data.count == 1) {
        likeCount.innerText = `${res.data.count} person likes "${starName}" already!`
      } else if (res.data.count != 0) {
        likeCount.innerText = `${res.data.count} people like "${starName}" already!`
      } else {
        likeCount.innerText = `Become the first liker of this star!`
      }
    })
})