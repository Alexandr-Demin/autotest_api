import httpx

login_payload = {
    "email": "user_test@example.com",
    "password": "123456"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Response status code:", login_response.status_code)
print("Response body:", login_response_data)

authentication_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}


authentication_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=authentication_headers)
authentication_response_data = authentication_response.json()

print("Response status code:", authentication_response.status_code)
print("Response body:", authentication_response_data)