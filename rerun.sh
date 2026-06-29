# echo "* * * * * * MIGRATION * * * * * *"
# echo
# python3 mylibrary/manage.py makemigrations
# python3 mylibrary/manage.py migrate
# echo

echo "* * * * * * TRADUCTION * * * * * *"
echo
cd ~/Bureau/stage26/mylibrary/shelf
django-admin makemessages -l=fr_FR -l=en_US
cd ~/Bureau/stage26/mylibrary/
./manage.py compilemessages

echo "* * * * * * Re-RUN * * * * * *"
echo
cd ~/Bureau/stage26/mylibrary/
fuser 8000/tcp 2>/dev/null > tmp.txt
kill -9 $(cat tmp.txt)
rm tmp.txt
python3 ./manage.py runserver
