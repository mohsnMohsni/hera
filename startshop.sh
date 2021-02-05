sudo apt install python3 -y
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requierments.txt
python3 manage.py migrate
python3 manage.py compilemessages
