export PYTHONPATH=$PYTHONPATH:.
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --no-cache-dir -r requirements.txt

python3 src/main.py