# process_data.py - Analyzes and categorizes threats
import json
import re
import pymongo

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client["darkweb_monitor"]
collection = db["threat_data"]

def analyze_data(raw_html):
    threats = []
    keywords = ["leak", "exploit", "malware", "0-day"]
    for keyword in keywords:
        if re.search(keyword, raw_html, re.IGNORECASE):
            threats.append(keyword)
    
    if threats:
        collection.insert_one({"threats": threats})
        print(f"Threats identified: {threats}")
    else:
        print("No significant threats detected.")

if __name__ == "__main__":
    sample_html = "<html><body>Latest exploit leaked...</body></html>"
    analyze_data(sample_html)
