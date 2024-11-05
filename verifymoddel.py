import httpx
from datetime import date


api_key = ''
headers = {
    'Authorization': f'Bearer {api_key}'
}

def check_quota():
    try:
        url = "https://api.openai.com/v1/usage"
        
        params = {'date': str(date.today())}
        response = httpx.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
       
        if data.get('data'):
            print(f"Usage: {data['data'][0]['usage']}")
            print(f"Quota: {data['data'][0]['quota']}")
        else:
            print("No usage information available.")
    except httpx.HTTPStatusError as e:
        print(f"HTTP Error: {e.response.status_code}, {e.response.json()}")
    except httpx.RequestError as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    check_quota()
