import requests

# Lista de links para evitar o erro 404 (tenta main e master)
URL_LIST = [
    "https://raw.githubusercontent.com/lkzin9172/AIMBOTFF/main/aimbot_payload.json",
    "https://raw.githubusercontent.com/lkzin9172/AIMBOTFF/master/aimbot_payload.json"
]

def get_remote_config():
    """Função inteligente para buscar as configurações sem dar erro 404"""
    for url in URL_LIST:
        try:
            print(f"[*] Tentando conectar ao servidor: {url}")
            # timeout de 5 segundos para o programa não travar
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print("[+] SUCESSO! Configurações remotas carregadas.")
                return response.json()
            
            elif response.status_code == 404:
                print(f"[!] Link não encontrado (404): {url}. Tentando outro...")
                continue 
            
            else:
                print(f"[!] Erro de servidor: Status {response.status_code}")
                break

        except Exception as e:
            print(f"[!] Erro de conexão: {e}")
            break
            
    print("[!!!] FALHA CRÍTICA: Não foi possível conectar ao GitHub.")
    return None

# --- INÍCIO DO SEU SISTEMA ---

print("--- INICIANDO SISTEMA AIMBOT FF ---")
config = get_remote_config()

if config:
    # Aqui o seu programa começa a usar as configurações que vieram do GitHub
    print("\n[+] Configurações aplicadas com sucesso!")
    print(f"[*] Aimbot Ativo: {config['aimbot_active']}")
    print(f"[*] Target: {config['aim_target']}")
    print(f"[*] FOV: {config['aim_fov']}")
    print(f"[*] Precisão: {config['aim_precision']}")
    
    # O seu código do jogo continua aqui abaixo...
    # Exemplo:
    # if config['aimbot_active']:
    #    run_aimbot(config['aim_fov'])

else:
    print("\n[!] O programa não conseguiu carregar as configurações.")
    print("[!] Verifique sua internet e se o repositório é PÚBLICO.")
