echo "Installing a local python + packages if necessary"
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt &> .venv/pip_log.txt

echo "Running the algorithm"
.venv/bin/python run.py
