echo "* * * * * * MIGRATION * * * * * *"
echo
python3 mylibrary/manage.py makemigrations shelf
python3 mylibrary/manage.py migrate
echo
echo "* * * * * * Re-RUN * * * * * *"
echo
fuser 8000/tcp 2>/dev/null > tmp.txt
kill -9 $(cat tmp.txt)
rm tmp.txt
python3 mylibrary/manage.py runserver
