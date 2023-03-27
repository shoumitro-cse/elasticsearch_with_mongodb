#https://sunscrapers.com/blog/how-to-use-elasticsearch-with-django/#What_is_Elasticsearch
# https://django-elasticsearch-dsl.readthedocs.io/en/latest/es_index.html

Data Dump from django app
# https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata
python manage.py dumpdata cars.Car > cars.json
python manage.py dumpdata cars.Manufacturer > manufacturers.json
python manage.py loaddata cars/fixtures/manufacturers.json
python manage.py loaddata cars/fixtures/cars.json

# user: shoumitro
# pw: Sr12345678

# Must enter this cmd
/home/shoumitro/Documents/html_ex/my_elasticsearch_example/elasticsearch-7.12.0/bin/elasticsearch
#or
cd /home/shoumitro/Documents/html_ex/my_elasticsearch_example/elasticsearch-7.12.0/bin
./elasticsearch


/home/shoumitro/.pyenv/versions/3.6.12/bin/python -m venv env
source ./env/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py makemigrations
python manage.py loaddata cars/fixtures/manufacturers.json
python manage.py loaddata cars/fixtures/cars.json
python manage.py runserver 127.0.0.1:8000

    
# This line is used to create es index
python manage.py search_index --rebuild

#Django Elasticsearch DSL DRF – examples of usage:

# display all cars.
http://localhost:8000/cars/ 

# display cars which contain the letter ‘a’ in their name.
http://localhost:8000/cars/?name__wildcard=*a* 

# search and display cars, which contain the word ‘is’ in the description.
http://localhost:8000/cars/?search=description|is 
http://localhost:8000/cars/?search=description|established

# filter and get only the cars which have ‘id’ greater or equal than 7.
http://localhost:8000/cars/?id__gte=7  

# filter, get only the cars with ids 7 and 8.
http://localhost:8000/cars/?id__in=7__8 


# This attribute not exist
# http://localhost:8000/cars/suggest/?name_suggest__completion=cor ==> get suggestions for the word ‘cor’.
