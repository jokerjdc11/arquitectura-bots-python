# region Importando librerias o clases necesarias
from time import sleep
from controller.Log import Log
from content.Selenium import Selenium
from controller.Impresor import Impresor
from selenium.webdriver.common.by import By
from controller.utils.KeyMouse import KeyMouse
from controller.utils.Configurations import Configurations
# endregion Importando librerias o clases necesarias

# ===========================================================================
# VARIABLES GLOBALES - LOCALES - INICIALIZACION DE OBJETOS
# ===========================================================================
# region - Instancia de clases de archivos importado
logger = Log()
mouse = KeyMouse()
consola = Impresor()
selenium = Selenium()
configuration = Configurations()
# endregion - Instancia de clases de archivos importado

class YoutubeBot:
    # Constructor de clase
    def __init__(self):
        """
        Metodo constructor de la clase, se crearan
        las variables o instancias propias de la clase
        donde podrán ser usadas dentro de la clase, o
        en cualquier lugar del aplicativo.
        """
        self.__driver = selenium.retornarDriver()
        self.__videosReproducir = []

    # region - Metodos de la clase

    # Inicializador de proceso para el bot de youtube
    def iniciarBotYoutube(self):
        """
        Metodo encargado de iniciaizar el proceso de la clase
        desde el llamado de funciones internas, hasta el manejo
        de logs de resultados de la ejecución.
        """
        self.__driver.maximize_window()
        sleep(2)
        consola.imprimirProceso("Inicio de proceso de YouTube")
        logger.registrarLogProceso("Inicio de proceso de YouTube")

        self.agregarAdblock()
        self.buscarCancion1()
        self.buscarCancion2()
        self.buscarCancion3()
        self.buscarListaLinks()
        self.__driver.quit()

        consola.imprimirProceso("Finalización de ejecución de Bot YouTube")
        logger.registrarLogProceso("Finalización de ejecución de Bot YouTube")
    
    
    def agregarAdblock(self):
        """
        Metodo para añadir al driver ejecutado, el complemento
        de adblock para ignorar las publicidades de las páginas
        """
        consola.imprimirProceso("Agregando complemento adBlock")
        logger.registrarLogProceso("Agregando complemento adBlock")
        self.__driver.get(configuration.getConfigValue("urls","adblock"))
        sleep(3)
        add = self.__driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[1]/section[1]/div/header/div[3]/div/div/a')
        sleep(2)
        add.click()
        sleep(2)
        mouse.moverMouse((1700,350))
        sleep(2)
        mouse.singleClick()
        sleep(5)

    def buscarCancion1(self):
        """
        Busqueda de link proporcionado (1)
        """
        consola.imprimirProceso("Ejecucion de primer cancion")
        logger.registrarLogProceso("Ejecucion de primer cancion")
        self.__driver.execute_script("window.open('');")
        self.__driver.switch_to.window(self.__driver.window_handles[1])
        self.__videosReproducir.append(configuration.getConfigValue("urls","urlYoutube1"))
        self.__driver.get(configuration.getConfigValue("urls","urlYoutube1"))
        sleep(3)
        try:
            btnPremium = self.__driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
            sleep(3)
            btnPremium.click()
        except Exception as ex:
            pass
        sleep(3)
        mouse.presionarHotKey("f")
        sleep(int(configuration.getConfigValue("time","videoTime")))
        mouse.presionarHotKey("f")

    def buscarCancion2(self):
        """
        Busqueda de link proporcionado (2)
        """
        consola.imprimirProceso("Ejecucion de segunda cancion")
        logger.registrarLogProceso("Ejecucion de segunda cancion")
        self.__videosReproducir.append(configuration.getConfigValue("urls","urlYoutube2"))
        self.__driver.get(configuration.getConfigValue("urls","urlYoutube2"))
        sleep(3)
        mouse.presionarHotKey("f")
        sleep(int(configuration.getConfigValue("time","videoTime")))
        mouse.presionarHotKey("f")
    
    def buscarCancion3(self):
        """
        Busqueda de link proporcionado (3)
        """
        consola.imprimirProceso("Ejecucion de tercera cancion")
        logger.registrarLogProceso("Ejecucion de tercera cancion")
        self.__videosReproducir.append(configuration.getConfigValue("urls","urlYoutube3"))
        self.__driver.get(configuration.getConfigValue("urls","urlYoutube3"))
        sleep(3)
        mouse.presionarHotKey("f")
        sleep(int(configuration.getConfigValue("time","videoTime")))
        mouse.presionarHotKey("f")

    def buscarListaLinks(self):
        """
        Metodo encargado de generar el ciclo de 
        busqueda de canciones para evitar la 
        repetición de código.

        Genera el mismo comportamiento por cada 
        canción que se reproduzca, de manera que
        se genera un estandar de reproducción.
        """
        for link in self.__videosReproducir:
            consola.imprimirProceso(f"Busqueda de Link: {link}")
            logger.registrarLogProceso("Inicio de tratado para link: {link}")
            self.__driver.execute_script("window.open('');")
            self.__driver.switch_to.window(self.__driver.window_handles[1])
            self.__driver.get(link)
            sleep(3)
            try:
                btnPremium = self.__driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
                sleep(3)
                btnPremium.click()
            except Exception as ex:
                pass
            sleep(1.5)
            mouse.presionarHotKey("f")
            sleep(int(configuration.getConfigValue("time","videoTime")))
            mouse.presionarHotKey("f")

    # endregion - Metodos de la clase 