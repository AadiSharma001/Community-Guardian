import requests

BASE = "http://127.0.0.1:8000"

def create():
    desc = input("Enter description: ")
    loc = input("Location: ")
    sev = input("Severity (low/medium/high): ")

    res = requests.post(f"{BASE}/incidents", json={
        "description": desc,
        "location": loc,
        "severity": sev
    })

    print(res.json())

def view():
    res = requests.get(f"{BASE}/incidents")
    for i in res.json():
        print(f"\n🔴 {i['type']} - {i['location']}")
        print("Summary:", i.get("summary"))
        print("Actions:", i.get("actions"))

def filter_incidents():
    loc = input("Filter by location: ")
    res = requests.get(f"{BASE}/incidents?location={loc}")
    print(res.json())

def update():
    id_ = int(input("Incident ID: "))
    status = input("New status: ")

    res = requests.put(f"{BASE}/incidents/{id_}?status={status}")
    print(res.json())

while True:
    print("\n1. Create\n2. View\n3. Filter\n4. Update\n5. Exit")
    choice = input("> ")

    if choice == "1":
        create()
    elif choice == "2":
        view()
    elif choice == "3":
        filter_incidents()
    elif choice == "4":
        update()
    else:
        break