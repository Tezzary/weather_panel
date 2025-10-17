import datetime
import requests
import time
from PIL import Image

def getNewestTime():
    newTime = 0
    for minutes in range(1,30):
        currentUtcTime = datetime.datetime.now(datetime.timezone.utc)
        newTime = currentUtcTime - datetime.timedelta(minutes=minutes)
        formattedTime = newTime.strftime("%Y%m%d%H%M")
        response = requests.get(f"http://www.bom.gov.au/radar/IDR023.T.{formattedTime}.png", headers = {'User-agent': 'Mozilla/5.0'})
        with open(f"/tmp/tmp.png", "wb") as f:
            f.write(response.content)
            f.close()

        try:
            im = Image.open(f"/tmp/tmp.png")
            im.verify()
            im.close() 
            break
        except:
            pass

        #path = "C:\\Programming\\VSCode\\Projects\\weathersite\\weathersitebackend\\djangobackend\\rainfall\\tempimages"
        #path = os.path.join(path, f"{formattedTime}.png")
        #os.remove(path)
    return newTime


def updateImageDatabase(time, amountOfTimes):
    #try:
        #Image.open("rainfall\\backgroundimages\\background.png")
        #backgroundImg = Image.alpha_composite(Image.open("rainfall\\backgroundimages\\background.png"), Image.open("rainfall\\backgroundimages\\topography.png")) 
        #print("pass")
    #except:
        #print("fail")
    backgroundImg = Image.open("background_images/background.png").convert("RGBA")
    topographyImg = Image.open("background_images/topography.png").convert("RGBA")
    rangeImg = Image.open("background_images/range.png").convert("RGBA")
    locationsImg = Image.open("background_images/locations.png").convert("RGBA")

    background = Image.alpha_composite(backgroundImg, topographyImg)
    foreground = Image.alpha_composite(rangeImg, locationsImg)
    
    for i in range(0, amountOfTimes):
        newTime = time - datetime.timedelta(minutes=i*5)
        formattedTime = newTime.strftime("%Y%m%d%H%M")

        response = requests.get(f"http://www.bom.gov.au/radar/IDR023.T.{formattedTime}.png", headers = {'User-agent': 'Mozilla/5.0'})

        file = open(f"images/{i}.png", "wb")
        file.write(response.content)
        file.close()
        
        rainfallImg = Image.open(f"images/{i}.png").convert("RGBA")
        temp = Image.alpha_composite(background, rainfallImg)
        finalImg = Image.alpha_composite(temp, foreground).convert("P")
        finalImg.save(f"images/{i}.png")


def update_images_every(seconds):
    while True:
        try:
            updateImageDatabase(getNewestTime(), 8)
            print("updated images")
            time.sleep(seconds)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    update_images_every(60)
