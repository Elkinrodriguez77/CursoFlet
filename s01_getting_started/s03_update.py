import flet as ft
import time
from flet import Page, Text

def main (page: Page):
    texto = Text()
    page.add(texto)

    for i in range(10):
        texto.value = f'Step: {i}'
        page.update()

        time.sleep(2)

# Ejecución en el escritorio:

#ft.app(target=main)

# Ejecución en el nagevador:

ft.app(target=main, view=ft.WEB_BROWSER, port=6781)
