import re
import time
import requests
import json

log_file = '/var/log/openvpn/status.log'
webhook_url = 'https://discord.com/api/webhooks/'
output_file = 'vpn_logs.txt'

ex_profiles = ["profile1","profile2"] # Exclude profiles that you don't want showing in the login notification.


def extract_user_info(log_file):
    user_info = {}
    with open(log_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        match = re.search(r'(\w+),(\d+\.\d+\.\d+\.\d+:\d+),', line)
        if match:
            profile_name = match.group(1)
            ip_address = match.group(2)
            user_info[ip_address] = profile_name

    return user_info

def send_discord_embed(profile, ip_address):
    if profile in ex_profiles:  
        return  
    else:
        embed = {
            "title": "VPN LOGIN",
            "description": f"Profile: {profile}\nIP Address: {ip_address}"
        }

        payload = {
            "embeds": [embed]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 204:
            print("Discord embed sent successfully.")
        else:
            print("Failed to send Discord embed.")

def log_user_info(profile, ip_address):
    with open(output_file, 'a') as file:
        file.write(f"Profile: {profile}, IP Address: {ip_address}\n")

def is_new_user(user_info, ip_address):
    return ip_address not in user_info

prev_user_info = {}

while True:
    user_info = extract_user_info(log_file)

    for ip_address, profile in user_info.items():
        if is_new_user(prev_user_info, ip_address):
            print(f"Profile: {profile}, IP Address: {ip_address}")
            send_discord_embed(profile, ip_address)
            log_user_info(profile, ip_address)

    prev_user_info = user_info

    time.sleep(5) 
