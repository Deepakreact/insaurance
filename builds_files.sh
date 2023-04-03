echo " BUILD START"

python 3.9 -m pip install -r requirements.txt


python 3.9 manage.py collectstatics --noinput --clear

echo " BUILD END"