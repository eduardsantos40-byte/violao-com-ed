from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.image import MDImage
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.webview import MDWebView
from kivy.core.audio import SoundLoader
import os

# Dados das perguntas
PERGUNTAS = [
    {
        "pergunta": "É normal sentir dor ao tocar?",
        "resposta": "No caso do iniciante, sim! ...",
        "audio": "resposta1.mp3"
    },
    {
        "pergunta": "Quanto tempo leva para começar a tocar bem?",
        "resposta": "Depende principalmente de dedicação ...",
        "audio": "resposta2.mp3"
    }
]

class MainScreen(MDScreen):
    pass

class AcordesScreen(MDScreen):
    # ... (código existente) ...

class PergunteEdScreen(MDScreen):
    # ... (código existente) ...

# Nova tela: Teoria Musical
class TeoriaMusicalScreen(MDScreen):
    def on_enter(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Cabeçalho
        cabecalho = MDLabel(
            text="Curso Teoria Musical - Com Edward Oliveira Monteiro",
            font_style="H4",
            halign="center",
            size_hint_y=0.2
        )
        layout.add_widget(cabecalho)
        
        # Mensagem de em breve
        aviso = MDLabel(
            text="Conteúdo em desenvolvimento\n\nEm breve: Lições completas de teoria musical!",
            halign="center",
            valign="middle",
            size_hint_y=0.6
        )
        layout.add_widget(aviso)
        
        # Botão de voltar
        voltar = MDRaisedButton(
            text="Voltar ao Menu",
            on_press=lambda x: self.manager.current = "main",
            size_hint_y=0.2
        )
        layout.add_widget(voltar)
        
        self.add_widget(layout)

# Nova tela: Cifras
class CifrasScreen(MDScreen):
    def on_enter(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)
        
        titulo = MDLabel(text="Cifras Simplificadas", font_style="H4")
        layout.add_widget(titulo)
        
        # Lista de cifras (exemplo)
        cifras = [
            "Garota de Ipanema - Tom Jobim",
            "Águas de Março - Elis Regina",
            "Wave - Antônio Carlos Jobim"
        ]
        
        for cifra in cifras:
            item = OneLineListItem(
                text=cifra,
                on_press=lambda x, c=cifra: self.mostrar_cifra(c)
            )
            layout.add_widget(item)
        
        # Botão para YouTube
        youtube_btn = MDRaisedButton(
            text="Abrir YouTube",
            on_press=self.abrir_youtube
        )
        layout.add_widget(youtube_btn)
        
        voltar = MDRaisedButton(
            text="Voltar",
            on_press=lambda x: self.manager.current = "main"
        )
        layout.add_widget(voltar)
        
        self.add_widget(layout)
    
    def mostrar_cifra(self, cifra):
        # Mostra detalhes da cifra
        dialog = MDDialog(
            title=cifra,
            text="Cifra detalhada aparecerá aqui...",
            size_hint=(0.8, 0.5),
            buttons=[
                MDRaisedButton(text="Fechar", on_press=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()
    
    def abrir_youtube(self, instance):
        # Abre o YouTube (implementaremos depois)
        self.manager.get_screen("youtube_player").url = "https://www.youtube.com/"
        self.manager.current = "youtube_player"

# Tela do YouTube
class YouTubePlayerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = "https://www.youtube.com/"
        
        layout = MDBoxLayout(orientation='vertical')
        
        self.webview = MDWebView()
        self.webview.url = self.url
        layout.add_widget(self.webview)
        
        voltar = MDRaisedButton(
            text="Voltar",
            on_press=lambda x: self.manager.current = "main"
        )
        layout.add_widget(voltar)
        
        self.add_widget(layout)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(AcordesScreen(name="acordes"))
        sm.add_widget(PergunteEdScreen(name="pergunte_ed"))
        sm.add_widget(TeoriaMusicalScreen(name="teoria_musical"))
        sm.add_widget(CifrasScreen(name="cifras"))
        sm.add_widget(YouTubePlayerScreen(name="youtube_player"))
        
        return sm

    def on_start(self):
        # Configuração do menu principal
        main_screen = self.root.get_screen("main")
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        titulo = MDLabel(text="Bem-vindo ao Violão com Ed!", font_style="H4")
        layout.add_widget(titulo)
        
        botoes = [
            "Acordes",
            "Teoria Musical",
            "Cifras",
            "Pergunte ao Ed"
        ]
        
        for btn_text in botoes:
            btn = MDRaisedButton(
                text=btn_text,
                on_press=self.navegar,
                size_hint=(None, None),
                width=300,
                height=60
            )
            layout.add_widget(btn)
        
        main_screen.add_widget(layout)
    
    def navegar(self, instance):
        texto = instance.text
        if texto == "Acordes":
            self.root.current = "acordes"
        elif texto == "Teoria Musical":
            self.root.current = "teoria_musical"
        elif texto == "Cifras":
            self.root.current = "cifras"
        elif texto == "Pergunte ao Ed":
            self.root.current = "pergunte_ed"

if __name__ == "__main__":
    MyApp().run()