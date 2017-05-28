set -a
source .env
python main.py 2>&1 | tee logs.log
