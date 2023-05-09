from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from relogio import relogio

class MainApp(App):
    def build(self):
        self.title="Pomodoro"
        box_principal=BoxLayout(orientation= 'vertical')
        #box secundárias
        box_marcacao=BoxLayout()
        box_relogio=BoxLayout()
        box_botoes=BoxLayout()
        #botões
        botao_inicio=Button(text="Iniciar",size=(15,15),size_hint=(0.5,0.5),pos_hint={'y':0.1})
        botao_zerar=Button(text="Zerar",size=(15,15),size_hint=(0.5,0.5),pos_hint={'y':0.1})
        #Instância relogio
        relogio_1 = relogio()
        #labels
        legenda_estudos=Label(text="Estudo : "+str(relogio_1.get_horas_estudo()),font_size=15)
        legenda_descanso=Label(text="Descanso : "+str(relogio_1.get_horas_descanso()),font_size=15)
        legenda_relogio=Label(text=relogio_1.get_horas_extenso,size_hint=(1,1),padding=(1,1),font_size=90)
        #Adição dos widgtes
        box_botoes.add_widget(botao_inicio)
        box_botoes.add_widget(botao_zerar)
        box_relogio.add_widget(legenda_relogio)
        box_marcacao.add_widget(legenda_estudos)
        box_marcacao.add_widget(legenda_descanso)
        box_principal.add_widget(box_marcacao)
        box_principal.add_widget(box_relogio)
        box_principal.add_widget(box_botoes)
        #configurações de janela
        Window.size=(250,250)
        Window.resizable=False
        botao_inicio.bind(on_press=lambda instance: relogio_1.iniciar(legenda_relogio,legenda_descanso,legenda_estudos))
        botao_zerar.bind(on_press=lambda instance: relogio_1.zerar(legenda_relogio,legenda_descanso,legenda_estudos))
        return box_principal   

if __name__=="__main__":
    app=MainApp()
    app.run()
