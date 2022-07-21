1. git clone <github url>

2. cd to ReadingList Project

3. Create virtualenv using python3
    python3 -m venv env

4. source env/bin/activate

5. pip install -r requirements.txt

6. python manage.py makemigrations api

7. python manage.py migrate

8. python manage.py createsuperuser

9. python manage.py runserver

10. generate token using login API with username and password

##API TEST.##
 1. Login API: 
    curl --location --request POST 'http://127.0.0.1:8000/api/v1/login/' \
--header 'Authorization: Token 193a9e8656c1991b12d9f475a9f43fd7bc09e9ee' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"tejendra", "password":"tejsingh1992"}'

    Response: {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1ODUxMjgwNCwianRpIjoiNjBkMTllZDgyOTI3NDhmMWFlZWFiN2QzOTE2NDhjMWMiLCJ1c2VyX2lkIjoxfQ.G2z2HIezeTvaiI2qrLm2njtP6EtiOqd_Nu3xIbcZhNY",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4NDI2NzA0LCJqdGkiOiIxZWYzYzdlNDFkMDc0YjBjYjNkNzM3ZjNmOTQ1MGI2MiIsInVzZXJfaWQiOjF9.VM4OrlMYeYna4IfsIZQbGFbB9ZTTXIJEr7ZvsX_oo0E"
}

2. GET list of Books API.
    curl --location --request GET 'http://127.0.0.1:8000/api/v1/books/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4NDI2NzA0LCJqdGkiOiIxZWYzYzdlNDFkMDc0YjBjYjNkNzM3ZjNmOTQ1MGI2MiIsInVzZXJfaWQiOjF9.VM4OrlMYeYna4IfsIZQbGFbB9ZTTXIJEr7ZvsX_oo0E'

    Response: [
    {
        "id": 1,
        "name": "database",
        "as_read": false,
        "owner": 1
    },
    {
        "id": 3,
        "name": "database1",
        "as_read": true,
        "owner": 1
    },
    {
        "id": 4,
        "name": "dbms1",
        "as_read": true,
        "owner": 1
    }
]

Note:   1. Use pagination with limit and offset query parameter
        2. User filter with name and read_as query parameter

3. Add Books API:
    curl --location --request POST 'http://127.0.0.1:8000/api/v1/books/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4NDI0NjM0LCJqdGkiOiI1YmYyNTBlMWFmYjk0Y2I2YTY0YjVhMzYyNjg0OTczMSIsInVzZXJfaWQiOjF9.Z6isQlBGTDpfzPtwfowYeWsf3aHTY2qNs1hF7Z0EH9g' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"c language","owner":1}'

    Response: {
    "id": 5,
    "name": "c language",
    "as_read": false,
    "owner": 1
}

4. Update Book Record:
    curl --location --request PUT 'http://127.0.0.1:8000/api/v1/books/4/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4NDI0OTQ3LCJqdGkiOiJhYWQ1ODBmYjZlNDE0MmU0YTI5Yzk1MjA2ZjQxNzdlMSIsInVzZXJfaWQiOjF9.uNtWZrsvAcda91KP93ob-wa8_YxY6DlSVzq1r4W68FQ' \
--header 'Content-Type: application/json' \
--data-raw '{"as_read":true,"name":"database1", "owner":1}'

5. Delete Book Record:
    curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/books/5/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4NDI0OTQ3LCJqdGkiOiJhYWQ1ODBmYjZlNDE0MmU0YTI5Yzk1MjA2ZjQxNzdlMSIsInVzZXJfaWQiOjF9.uNtWZrsvAcda91KP93ob-wa8_YxY6DlSVzq1r4W68FQ'

6. Mark-as-Read API:
    curl --location --request POST 'http://127.0.0.1:8000/api/v1/mark-as-read' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4NDI2NzA0LCJqdGkiOiIxZWYzYzdlNDFkMDc0YjBjYjNkNzM3ZjNmOTQ1MGI2MiIsInVzZXJfaWQiOjF9.VM4OrlMYeYna4IfsIZQbGFbB9ZTTXIJEr7ZvsX_oo0E' \
--header 'Content-Type: application/json' \
--data-raw '{"book_id":3, "as_read":true}'

    Response: {
    "status": "success",
    "data": "Record update successfully"
}

7. User Create API:
    curl --location --request POST 'http://127.0.0.1:8000/api/v1/register/' \
    --header 'Content-Type: application/json' \
    --data-raw '{"username":"tejendra", "password":"12345","password2":"12345", "email":"tejendrakushwah2012@gmail.com", "first_name":"tejendra", "last_name":"kushwah" }'