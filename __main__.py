import sys

from PyQt5.QtWidgets import QApplication
from src.vista.InterfazEPorra import App_EPorra
from src.logica.Logica_mock import Logica_mock
from src.logica.logica import Logica

from src.modelos.declarative_base import Session, Base, engine
from src.modelos.apostador import Apostador
from src.modelos.apuesta import Apuesta
from src.modelos.carrera import Carrera
from src.modelos.competidor import Competidor

if __name__ == '__main__':
    # Punto inicial de la aplicación
    #logica = Logica_mock()
    logica = Logica()

    

    app = App_EPorra(sys.argv, logica)
    sys.exit(app.exec_())