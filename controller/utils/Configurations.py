# ===========================================================================
# Importaciones de clases y librerias necesarias
# ===========================================================================
# region Importando librerias o clases necesarias
from configparser import ConfigParser
# endregion Importando librerias o clases necesarias

class Configurations:
    # Constructor de clase
    def __init__(self):
        self.__config = ConfigParser()
        self.__file = "config.ini"

    # region Metodos
    # Obtiene una ruta del archivo config concatenado con el path del proyecto
    def getConfigValue(self,sections,key):
        """
            Metodo que trae el valor de una seccion y valor enviado
            - `Args:`
                - sections (str): Nombre de la seccion
                - key (str): Nombre de la clave necesaria
        """
        self.__config.read(self.__file)
        valor = self.__config.get(sections,key)
        return valor
    # endregion    