import requests
import json


headers = {'APP_KEY': 'B*Zeu>&HWg9`jx*j'}

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def attempt(rfid):
    response = requests.post("http://127.0.0.1:8000/api/raspberry/visitor", data=rfid, headers=headers)
    if (response.status_code == 404):
        res = jprint(response.json()['error'])
        return 0
    else:
        res = jprint(response.json())
        return 1


def getStudentData():
    student = []
    rfid = str(input("rfid: "))
    rfid = {'rfid': rfid}
    response = requests.post("http://127.0.0.1:8000/api/RaspberryPi/find/student", data=rfid, headers=headers)
    data = json.loads(response.text)
    if(response.status_code == 404):
        print('mahasiswa tidak ditemukan')
        student = 0
        return  student
    else:
        data = data['data']
        student.append(data)
        return student







