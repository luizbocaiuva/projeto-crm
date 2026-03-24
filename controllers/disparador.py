from playwright.sync_api import sync_playwright
import time
import random
import os

URL_BASE = 'https://web.whatsapp.com'

class DisparadorController:
    def __init__(self, vendedora):
        self.vendedora = vendedora
        self.primeiro_acesso = not os.path.exists(self.vendedora.session_path)

    def iniciar_disparo(self, lista_clientes):
        with sync_playwright() as play:

            is_headless = not self.primeiro_acesso

            print(f'Modo Headless: {is_headless} | Sessão: {self.vendedora.nome}')


            browser = play.chromium.launch_persistent_context(
                user_data_dir=self.vendedora.session_path, headless=is_headless,
                no_viewport=False, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page = browser.new_page()
            page.goto(URL_BASE)

            if self.primeiro_acesso:
                print(f'AGUARDANDO LOGIN: Escaneie o QR Code para {self.vendedora.nome}...')
                try:
                    page.wait_for_selector('canvas[aria-label="Scan this QR code to link a device!"]', state='detached',  timeout=120000)
                    
                    page.wait_for_function('''() => document.querySelector('div[contenteditable=\"true\"]') || document.querySelector('header')''', timeout=60000)
                    print('Login realizado com sucesso! Aguardando sincronização!')
                    time.sleep(10)
                except Exception as e:
                    print(f'Tempo esgotado para o QR Code ou erro no seletor: {e}')
                    page.screenshot(path=f'erro_login_{self.vendedora.id}.png')
                    browser.close()
                    return

            for cliente in lista_clientes:
                self._enviar_mensagem(page, cliente)
                time.sleep(random.randint(10, 30))

                    

            browser.close()

    def _enviar_mensagem(self, page, cliente):
        try:
            url = f'{URL_BASE}/send?phone={cliente.telefone}&text={cliente.mensagem}'
            page.goto(url, wait_until='networkidle', timeout=60000)
            try:
                page.wait_for_selector('#main', timeout=40000)

                caixa_texto = page.wait_for_selector(f'div[role="textbox"]', timeout=25000)
                time.sleep(random.uniform(5, 10))

                btn_enviar = page.query_selector('span[data-icon="send"]') or page.query_selector('button[aria-label="Enviar"]')

                if btn_enviar:
                    btn_enviar.click()
                else:
                    print('Botão não localizado, tentando enviar com a tecla ENTER...')
                    caixa_texto.focus()
                    page.keyboard.press('Enter')

                print(f'✓ Mensagem enviada para {cliente.nome} por {self.vendedora.nome}')
                cliente.status_envio = 'Enviado'
            except Exception as e:
                aviso_erro = page.query_selector('div:has-text("O número de telefone é inválido")')
                if aviso_erro:
                    print(f'⚠ O número {cliente.telefone} é inválido para o WhatsApp.')
                    cliente.status_envio = 'Número Inválido!'
                    page.click('button:has-text("OK")')
                else:
                    raise e

            intervalo = random.randint(30, 60)
            time.sleep(intervalo)
        except Exception as e:
            print(f'✗ Erro ao enviar mensagem para o cliente {cliente.nome}: {e}')
            cliente.status_envio = 'Erro'