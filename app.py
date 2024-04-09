from scraper import Scraper 
import flet as ft

# Dev branch

def main(page: ft.Page):

    def handle_click(e):
        if txt_keyword == "":
            txt_keyword.error_text = "Please enter a keyword"
            page.update()
        else:
            scraper = Scraper()
            scraper.scrap(url=f'https://www.google.com/maps/search/{txt_keyword.value}')

    # Global Config
    page.title = "Google Maps Web Scrapper"
    page.window_maximized = False
    page.window_maximizable = False
    page.window_resizable = False

    page.add(ft.Container(
        content=ft.Column([
            ft.Text(
            value="Google Maps Web Scrapper", 
            color="white", 
            size=30,
            weight=ft.FontWeight.BOLD
        ),
            ft.Text(
            value="By Rocchetta Luciano",
            color="white",
            size=20,
            )
        ]),
        image_src='../source/wallpaper.jpg',
        image_fit=ft.ImageFit.COVER,
        width=page.width,
        expand=True,
    ))

    txt_keyword = ft.TextField(label="Enter the Keyword!")

    page.add(ft.Row([
        txt_keyword,
        ft.FilledButton(
            text="Scrap", 
            on_click=handle_click, 
            icon="search"
            )
        ]))

    page.update()
    pass

if "__main__" == __name__:
    ft.app(target=main)

