import requests

def upload(data):
    lol = {
        'u': (None, 'username'),
        'p': (None, 'password hash'),
        'v': (None, '1'),
        'ss': ("ss", data, 'application/octet-stream')
    }

    headers = {
        "User-Agent": "osu!",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close"
    }

    response = requests.post('https://osu.ppy.sh/web/osu-screenshot.php', files=lol, headers=headers)
    return response.content.decode()

print("What do you want to send?")
type = input("1 - Text, 2 - File: ")

if type == "1":
    txt = input("Enter your message: ")
    link = upload(txt)

elif type == "2":
    path = input("Enter the path of the file: ")
    file = open(path, "rb")
    link = upload(file)

else:
    print("Please enter 1 or 2!")
    exit()

print(link)
