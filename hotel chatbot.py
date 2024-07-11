import json
import requests
from chatterbot import ChatBot
# from chatterbot.conversation import statement
from chatterbot.trainers import ChatterBotCorpusTrainer


def get_hotel_booking_data():
    hotel_data = {
        "hotel_name": input("Enter the hotel name: "),
        "check_in_date": input("Enter the check-in date (YYYY-MM-DD): "),
        "check_out_date": input("Enter the check-out date (YYYY-MM-DD): "),
        "guests": int(input("Enter the number of guests: "))
    }
    return hotel_data

def make_api_call_with_json_body(json):
    # API endpoint URL
    api_url = "http://localhost:18888/engineapi/blocDataRequest"  # Replace with the actual API URL

    # JSON data to send in the request body
    data = json

    # Optional: If your API requires an API key or authentication token
    api_key = "YOUR_API_KEY"  # Replace with your API key

    headers = {

        # Optional: If the API accepts JSON format
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Check for errors

        result = response.json()  # Parse JSON response into Python dictionary
        print(result)

    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")

chatBot = ChatBot("ChatBot")
trainer = ChatterBotCorpusTrainer(chatBot)
trainer.train("chatterbot.corpus.english.ai")

print("Hi, I am ChatBot")
while True:
    query = input('>>> ')
    if query.__contains__("room booking"):
        print("please give me the following details")
        json = get_hotel_booking_data()
        print(json)
        make_api_call_with_json_body(json)

        # apicall
    elif chatBot.get_response(query).confidence > 0.5:
        print(chatBot.get_response(query))
    else:
        print("sorry I can't understand")