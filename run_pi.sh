ssh raspberrypi "

if [ ! -d weather_panel ]; then
  git clone https://github.com/Tezzary/weather_panel
  cd weather_panel
  chmod +x run.sh
fi

cd ~/weather_panel

git pull

nohup ./run.sh &

killall firefox
export DISPLAY=:0
nohup firefox --kiosk --new-instance --private-window http://localhost:8001/ &
"
