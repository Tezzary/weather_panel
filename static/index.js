let weatherMapObject = document.getElementById("weatherMap")

const timeBetweenImages = 300
let imageCount = 8
let maxCacheTime = 60

let currentImage = 0

function loadNextImage() {

  let now = Date.now()
  let cache_buster = Math.floor(now / (maxCacheTime * 1000))

  weatherMapObject.src = "images/" + (imageCount - currentImage - 1) + ".png?t=" + cache_buster

  currentImage = (currentImage + 1) % imageCount
  console.log("Updated image")
}

setInterval(loadNextImage, timeBetweenImages)
