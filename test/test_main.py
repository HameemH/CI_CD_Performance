from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}
    
def test_add():
    response = client.post("/ticket", json=[{
        "id": 1,
        "flight_name": "US Bangla",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    },
    {
        "id": 2,
        "flight_name": "Biman Bangladesh",
        "flight_date": "2025-11-20",
        "flight_time": "10:00",
        "destination": "Chittagong"
    }])
    assert response.status_code == 200
    assert response.json() == "ticket added"
    
def test_get():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert isinstance(response.json(), list)    

def test_update():
    response = client.put("/ticket/1", json={
        "id": 1,
        "flight_name": "US Bangla Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:30",
        "destination": "Dhaka Updated"
    })
    assert response.status_code == 200
    assert response.json() == "ticket updated"  
def test_delete():
    response = client.delete("/ticket/2")
    assert response.status_code == 200
    assert response.json() == "ticket deleted"        
    