ssh raspberrypi "

if [ ! -d weather_panel ]; then
  git clone https://github.com/Tezzary/weather_panel
  cd weather_panel
  chmod +x run.sh
fi

cd ~/weather_panel
killall firefox
./run.sh

"
