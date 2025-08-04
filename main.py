import time
import requests
from termcolor import colored
from table import final_table
from telegram import send_massage


def main(check_list):
    """all of the steps was here"""
    loc = final_table()
    if not isinstance(loc, str) and not isinstance(loc, Exception):
        try:
            for name in loc.values:
                if not name[4] == "":
                    hash_massage = send_massage(name, check_list)
                    check_list.append(hash_massage)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(20)
    return check_list


def send_startup_message():
    """Send a message when bot starts"""
    base_url = "https://api.telegram.org/bot7452324631:AAHFMFgb5s2Ef5YRTRDNxFNcb4ik-ETz_Tc/sendMessage"
    parameters = {
        "chat_id": "@news_news127",
        "text": "Bot started 🤖"
    }
    try:
        requests.get(url=base_url, data=parameters)
        print(colored("Startup message sent to channel", "green"))
    except Exception as e:
        print(colored(f"Failed to send startup message: {e}", "red"))

if __name__ == "__main__":
    print(colored("the bot was started to work", "green"))
    check_list = []
    send_startup_message()
    while True:
        time.sleep(2)
        check_list = main(check_list)
        time.sleep(2)