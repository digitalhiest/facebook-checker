import argparse
import requests
from colorama import init, Fore

def display_logo():
    print(Fore.GREEN + "Facebook App Checker")

def display_usage():
    usage = """
    Usage:
    python script_name.py app_id app_secret
    """
    print(Fore.RED + usage)

def check_facebook_app(app_id, app_secret):
    url = "https://graph.facebook.com/oauth/access_token"
    params = {
        "client_id": app_id,
        "client_secret": app_secret,
        "grant_type": "client_credentials"
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(Fore.GREEN + "[+] Facebook App ID and Secret are valid.")
            access_token = response.json().get("access_token")
            check_ads_management(access_token)
            check_page_management(access_token)
            display_user_info(access_token)
        else:
            print(Fore.RED + "[-] Failed to obtain access token. Check your Facebook App ID and Secret.")
    except Exception as e:
        print(Fore.RED + f"[-] An error occurred: {e}")

def check_ads_management(access_token):
    try:
        ads_url = "https://graph.facebook.com/v12.0/act_{account_id}/campaigns".format(account_id="your_ad_account_id")
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(ads_url, headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + "[+] Ads Management is accessible.")
        else:
            print(Fore.RED + "[-] Ads Management is not accessible.")
    except Exception as e:
        print(Fore.RED + f"[-] An error occurred while checking Ads Management: {e}")

def check_page_management(access_token):
    try:
        pages_url = "https://graph.facebook.com/v12.0/me/accounts"
        params = {"access_token": access_token}
        response = requests.get(pages_url, params=params)
        if response.status_code == 200:
            print(Fore.GREEN + "[+] Page Management is accessible.")
        else:
            print(Fore.RED + "[-] Page Management is not accessible.")
    except Exception as e:
        print(Fore.RED + f"[-] An error occurred while checking Page Management: {e}")

def display_user_info(access_token):
    try:
        user_info_url = f"https://graph.facebook.com/me?fields=id,name,email&access_token={access_token}"
        response = requests.get(user_info_url)
        if response.status_code == 200:
            user_data = response.json()
            print("User Information:")
            print(f"ID: {user_data.get('id')}")
            print(f"Name: {user_data.get('name')}")
            print(f"Email: {user_data.get('email')}")
        else:
            print(Fore.RED + "[-] Failed to retrieve user information.")
    except Exception as e:
        print(Fore.RED + f"[-] An error occurred while fetching user information: {e}")

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama
    display_logo()

    parser = argparse.ArgumentParser(description="Facebook App Checker")
    parser.add_argument("app_id", help="Facebook App ID")
    parser.add_argument("app_secret", help="Facebook App Secret")
    args = parser.parse_args()

    if args.app_id and args.app_secret:
        check_facebook_app(args.app_id, args.app_secret)
    else:
        display_usage()
