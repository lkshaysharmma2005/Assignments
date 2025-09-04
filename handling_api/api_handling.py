import requests

def fetching_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]["data"]
        username = user_data[0]["login"]["username"]
        country = user_data[0]["location"]["country"]
        return username,country
    
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username,country = fetching_api()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
