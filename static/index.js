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

let tempDOM = document.getElementById("temp")
let feelsLikeDOM = document.getElementById("feelsLike")

async function updateWeatherInformation() {
  let weatherInformationResponse = await fetch("weatherInformation.json")
  let weatherInformation = await weatherInformationResponse.json()
  let temp = weatherInformation.obs.temp.dry_bulb_1min_cel;
  let feelsLike = weatherInformation.obs.temp.apparent_1min_cel;
  console.log(weatherInformation)
  tempDOM.innerHTML = temp + "&deg;"
  feelsLikeDOM.innerHTML = "Feels Like " + feelsLike + "&deg;"
}

updateWeatherInformation()
setInterval(updateWeatherInformation, maxCacheTime * 1000)
