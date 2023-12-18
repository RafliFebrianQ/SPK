# UAS spk_web

## Install venv

    virtualenv venv

## Install requirements

    pip install -r requirements.txt

## Run the app
to run the web app simply  use

    python main.py

## Usage
Install postman 
https://www.postman.com/downloads/

get ponsel list
<img src='img/get_salmon.png' alt='salmon list'/>

get recommendations saw
<img src='img/get_saw.png' alt='recommendations saw'/>

get recommendations wp
<img src='img/get_wp.png' alt='recommendations wp'/>

### TUGAS UAS
Implementasikan model yang sudah anda buat ke dalam web api dengan http method `POST`

INPUT:
{'harga': 4, 'umur': 3, 'berat': 4, 'lemak': 6, 'omega_3': 3}

OUTPUT (diurutkan / sort dari yang terbesar ke yang terkecil):

post recommendations saw
<img src='img/post_saw.png' alt='recommendations saw'/>

post recommendations wp
<img src='img/post_wp.png' alt='recommendations wp'/>
