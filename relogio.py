from kivy.clock import Clock
from win10toast import ToastNotifier

class relogio():
    def __init__(self):
        self._minuto=0
        self.teste=0
        self._segundo=0
        self._horas_extenso="00:00"
        self._estudo_descanso=0
        self._horas_descanso=0
        self._horas_estudo=0
        self._validade=False

    @property
    def get_horas_extenso(self):
        return self._horas_extenso
    @property
    def get_horas_descanso(self):
        return self._horas_descanso
    @property
    def get_horas_estudo(self):
        return self._horas_estudo

    def alterar(self,label,dt):
        #alterar o cronometro
        if self._segundo<59:
            self._segundo=self._segundo+1
        elif self._segundo==59:
            self._segundo=0
            self._minuto=self._minuto+1
        if self._segundo<10 and self._minuto<10:
            self._horas_extenso="0"+str(self._minuto)+":0"+str(self._segundo)
        elif self._segundo>=10 and self._minuto<10:
            self._horas_extenso="0"+str(self._minuto)+":"+str(self._segundo)
        elif self._segundo<10 and self._minuto>=10:
            self._horas_extenso=str(self._minuto)+":0"+str(self._segundo)
        else:
            self._horas_extenso=str(self._minuto)+":"+str(self._segundo)
        label.text=self._horas_extenso
      
    def adicionar_estudo(self,label_estudos,label_horas):
        #adicionar no label de estudos quando bater meia hora
        self._horas_estudo=self._horas_estudo+1
        label_estudos.text="Estudo : " + str(self._horas_estudo)
        self._horas_extenso="00:00"
        label_horas.text=self._horas_extenso
        self._estudo_descanso=1
        self._minuto = 0
        self._segundo= 0
        self.notificacao_estudo = ToastNotifier().show_toast("Acabou o tempo", "Acabou o tempo de estudo, seu descanso começou", duration=5,threaded=True)
          
    def adicionar_descanso(self,label_descanso,label_horas):
        #adicionar no label de descanso quando bater 15 minutos
        self._horas_descanso=self._horas_descanso+1
        label_descanso.text="Descanso : " + str(self._horas_descanso)
        self._horas_extenso="00:00"
        label_horas.text=self._horas_extenso
        self._estudo_descanso=0
        self._minuto = 0
        self._segundo= 0
        self.notificacao_descanso = ToastNotifier().show_toast("Acabou o tempo", "Acabou o tempo de descanso, seu estudo começou", duration=5,threaded=True)
        
    def verificar(self,label_descanso,label_estudo,label_horas,dt):
        #verifica se bateu o tempo de estudo ou de descanso
        if self._estudo_descanso==0 and self._minuto==25:
            self.adicionar_estudo(label_estudo,label_horas)
        elif self._estudo_descanso==1 and self._minuto==5:
            self.adicionar_descanso(label_descanso,label_horas)

    def iniciar(self,label_horas,label_descanso,label_estudos):
        #iniciar o cronometro
        if self._validade==False:
            global evento_contagem
            global evento_verificacao
            evento_contagem=Clock.schedule_interval(lambda dt: self.alterar(label_horas,dt),1.0)
            evento_verificacao=Clock.schedule_interval(lambda dt: self.verificar(label_descanso,label_estudos,label_horas,dt),1.0)
            self._validade=True

    def zerar(self,label_horas,label_descanso,label_estudos):
        #zerar tudo
        if self._validade==True:
            evento_contagem.cancel()
            evento_verificacao.cancel()
            self._validade=False
        self._horas_extenso="00:00"
        label_horas.text=self._horas_extenso
        self._minuto=0
        self._segundo=0
        self._estudo_descanso=0
        self._horas_descanso=0
        self._horas_estudo=0
        label_descanso.text="Descanso : " + str(self._horas_descanso)
        label_estudos.text="Estudo : " + str(self._horas_estudo)