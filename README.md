# HerSafeSpace API



HerSafeSpace is a RESTful API built with Django and Django REST Framework that provides women a safe, anonymous space to track moods, self-care activities, and share or explore experiences.



### Features



Token-based user authentication



Mood tracking (create \& view moods)



Self-care activities (create \& view activities)



Anonymous posts \& comments (share and read anonymously)



Users can only edit their own entries



### API Endpoints



Authentication: POST /api/token/



Moods: GET /api/moods/, POST /api/moods/



Self-Care: GET /api/selfcare/, POST /api/selfcare/



Anonymous Posts: GET /api/posts/, POST /api/posts/, GET /api/posts/{id}/



Comments: GET /api/posts/{id}/comments/, POST /api/posts/{id}/comments/



### Setup



###### Clone the repo:



git clone [https://github.com/hajar-elhaj/HerSafeSpace-API.git](https://github.com/hajar-elhaj/HerSafeSpace-API.git)



###### Install dependencies and run migrations:



pip install -r requirements.txt

python manage.py migrate



###### Start server:



python manage.py runserver



###### Testing



Use Postman or curl with your token to test endpoints, e.g.:



curl -H "Authorization: Token <your\_token>" http://127.0.0.1:8000/api/moods/

