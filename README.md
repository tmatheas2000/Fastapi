### Setup Virtualenv
python3 -m virtualenv env
cd env
source bin/activate
cd ..

### Install packages
pip3 install -r requirements.txt

### Run Application
uvicorn main:app --reload

### Generate SECRET_KEY
openssl rand -hex 32