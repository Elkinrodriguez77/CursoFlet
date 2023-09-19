import flet as ft
from flet import Page, Text

def main(page: Page):
    texto = Text(value='Hola Flet', color='blue')
    page.controls.append(texto)
    page.update()

# Lanzar app en modo escritorio

ft.app(target=main)