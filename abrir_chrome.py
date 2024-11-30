from playwright.sync_api import sync_playwright
7
# Caminho para o executável do Google Chrome
chrome_path = ""

with sync_playwright() as p:
    # Para escolher um Perfil, utlize --profile-directory="nome d perfil"
    context = p.chromium.launch_persistent_context(
        # user_data_dir : pasta onde fica os dados de usuário do Google Chrome
        # No Windows é: C:\\Users\\Seu usuário\\AppData\\Local\\Google\\Chrome\\User Data
        # Importante utilizar duas barras, para que o Python entenda como uma string completa.
        # Outra maneira seria utilizar apenas uma barra e colocar um r antes da string:
        # user_data_dir = r"C:\Users\Seu usuário\AppData\Local\Google\Chrome\User Data"
            user_data_dir= "",
            executable_path=chrome_path,
            channel="chrome",
            slow_mo=1000,
            headless=False,
            args=["--start-maximized", "--profile-directory=Profile 6"],
            no_viewport=True
        )
    page = context.pages[0]
    # Acessar o site do corresponde BB
    page.goto("https://correspondente.bb.com.br/cbo-portal-acesso/#/login")
    # Espera o usuário realizar o login:
    input()
    page.wait_for_timeout(5000)
    print(page.title())
    context.close()
