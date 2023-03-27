# enter docker container
docker-compose up --build
docker exec -it web_app bash

# create index
python manage.py search_index --create 
python manage.py search_index --rebuild

# create super user
python manage.py createsuperuser

# add data
python manage.py loaddata cars/fixtures/manufacturers.json
python manage.py loaddata cars/fixtures/cars.json
