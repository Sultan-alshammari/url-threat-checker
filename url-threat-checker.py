import requests

API_KEY = 'YOUR_API_KEY'
URL_TO_CHECK = 'http://example.com'

def check_url_safety(url):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(api_url, json=payload)
    if response.json():
        return "مشبوه أو خطر"
    else:
        return "آمن"

result = check_url_safety(URL_TO_CHECK)
print(f"الرابط: {URL_TO_CHECK} هو {result}")