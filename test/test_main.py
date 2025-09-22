from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}
    
def test_add():
    ticket={
            "id": 1,
            "flight_name": "US Bangla",
            "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    
    }
    response = client.post("/ticket", json=ticket)
    assert response.status_code == 200
    assert response.json() == ticket
    
def test_get():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert isinstance(response.json(), list)    

def test_update():
    update= {
        "id": 1,
        "flight_name": "US Bangla Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:30",
        "destination": "Dhaka Updated"
    }
    response = client.put("/ticket/1", json=update)
    assert response.status_code == 200
    assert response.json() == update
def test_delete():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "US Bangla Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:30",
        "destination": "Dhaka Updated"
    }        
    