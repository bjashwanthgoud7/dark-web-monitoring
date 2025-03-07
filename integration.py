# integration.py - Connects with SIEM (Splunk/ELK)
import requests
import json

def send_to_siem(data):
    siem_url = "http://siem-server:8088/services/collector"
    headers = {"Authorization": "Splunk <TOKEN>", "Content-Type": "application/json"}
    payload = json.dumps({"event": data})
    
    try:
        response = requests.post(siem_url, headers=headers, data=payload)
        if response.status_code == 200:
            print("Threat data successfully sent to SIEM.")
        else:
            print(f"Failed to send data. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to SIEM: {e}")

if __name__ == "__main__":
    sample_data = {"threat": "Exploit found", "severity": "High"}
    send_to_siem(sample_data)
