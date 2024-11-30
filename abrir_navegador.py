from playwright.sync_api import sync_playwright, Playwright
import os

def run(playwright:Playwright):
    # URL do Google. Pode colocar outra
    url = r"https://www.google.com"
    browser = playwright.chromium.launch(
            # Pode colocar: msedge, chrome, chromium
            channel="chrome",
            slow_mo=100,
            headless=False,
            args=["--start-maximized"] # Iniciar com a tela maximizada
        )
    # Seleciona uma única pagina
    page = browser.new_page(
        no_viewport=True # garante que a tela do navegador abrirá maximizada
        )
    # Acessa a página e espera 2 segundos para carregar
    page.goto(url)
    page.wait_for_timeout(5000)
    # Imprime o título da página
    print(page.title())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)