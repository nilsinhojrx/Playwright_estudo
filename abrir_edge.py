from playwright.sync_api import sync_playwright

# Caminho para o executável do Microsoft Edge
edge_path = ""

with sync_playwright() as p:
    # Para escolher um Perfil, utlize --profile-directory="nome d perfil"
    context = p.chromium.launch_persistent_context(
        # user_data_dir : pasta onde fica os dados de usuário do Google Chrome
        # No Windows é: C:\\Users\\nilso\\AppData\\Local\\Microsoft\\Edge\\User Data
            user_data_dir= "",
            executable_path=edge_path,
            channel="msedge",
            slow_mo=1000,
            headless=False,
            args=["--start-maximized", "--profile-directory=Default"],
            no_viewport=True
        )
    page = context.pages[0]
    # Acessar o site do Google
    page.goto("https://www.google.com")
    # Espera 5 segundos
    page.wait_for_timeout(5000)
    # Imprime o título da página:
    print(page.title())
    context.close()