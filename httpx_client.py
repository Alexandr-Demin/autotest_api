import httpx

login_payload = {
    "email": "user_test@example.com",
    "password": "123456"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)


client = httpx.Client(
    base_url="http://localhost:8000/api/v1",
    timeout=100,
    headers= {"Authorization":f"Bearer {login_response_data['token']['accessToken']}"}
    
    )

response = client.get("/users/me")
response_data = response.json()

print('Get user me data:', response_data)