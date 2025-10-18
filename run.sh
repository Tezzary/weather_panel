
pkill -f "python3 -m http.server 8001"
pkill -f "python3 main.py"

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

. venv/bin/activate
pip3 install -r requirements.txt

python3 -m http.server 8001 --directory static/ & # > /dev/null 2>&1
python3 main.py > log.txt &


