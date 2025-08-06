# BruteForce-deLoginHttp

> **Status:** Projeto em desenvolvimento 

Um script em Python para realizar ataques de força bruta em formulários de login HTTP. Utiliza uma wordlist para testar múltiplas combinações de senha em um alvo específico.

## Funcionalidades
- Lê uma lista de senhas a partir de um arquivo (wordlist).
- Realiza requisições POST automatizadas para testar credenciais.
- Identifica e exibe a senha correta ao encontrar um login válido.
- Mensagens de erro claras para argumentos inválidos ou arquivos não encontrados.

## Tecnologias Utilizadas
- Python 3
- Biblioteca [requests](https://pypi.org/project/requests/) (para requisições HTTP)

## Instalação

Clone o repositório:
```bash
git clone https://github.com/CarlosInCodeLand/BruteForce-deLoginHttp
cd BruteForce-deLoginHttp
```

Instale as dependências:
```bash
pip install requests
```

## Como Usar

Execute o script com os argumentos necessários:

```bash
python3 bruforht.py -a <url_alvo> -u <usuario> -w <wordlist>
```

### Argumentos
- `-h` : Help
- `-a` : URL do alvo (endpoint do login)
- `-u` : Nome de usuário
- `-w` : Caminho para o arquivo de wordlist

### Exemplo de uso
```bash
python3 bruforht.py -a http://localhost/login -u admin -w senhas.txt
```

Para exibir o manual de uso:
```bash
python3 bruforht.py -h
```

## Observações
- Certifique-se de que a wordlist e a URL do alvo estejam corretas.
- O script identifica sucesso se encontrar "logout" na resposta ou se o status HTTP for 302.

## ⚠️ Aviso Legal
Este script é para fins educacionais e de testes em ambientes controlados. **Não utilize em sistemas sem a devida autorização. O uso indevido é de sua total responsabilidade.**

