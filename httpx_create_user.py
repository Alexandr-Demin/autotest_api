import httpx
from tools.fakers import get_random_email

requet_body = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

creat_request = httpx.post("http://localhost:8000/api/v1/users", json=requet_body)

print(creat_request.status_code)
print(creat_request.json())