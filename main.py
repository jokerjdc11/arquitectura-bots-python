# ===========================================================================
# Importaciones de clases y librerias necesarias en este archivo main
# ===========================================================================
# region -  Importaciones de archivos o librerias
from controller.Log import Log
from controller.Impresor import Impresor
from content.YoutubeBot import YoutubeBot
# endregion - Importaciones de archivos o librerias

# ===========================================================================
# VARIABLES GLOBALES - LOCALES - INICIALIZACION DE OBJETOS
# ===========================================================================
# region - Instancia de clases de archivos importado
logger = Log()
consola = Impresor()
# endregion - Instancia de clases de archivos importado

# region Body Metodo principal main
def main():
    try: 
        # Metodos utilizados para almacenar logs iniciales e Imprimir resultados iniciales en pantalla
        consola.imprimirInicio("Bots en Python - Reproducir cancion en youtube")
        logger.registroInicioProcesos()

        # Metodos para imprimir o dejar logs en cualquier parte del proceso
        consola.imprimirProceso("Inicio de ejecucion del proceso")
        logger.registrarLogProceso("Inicio de ejecucion del proceso")
        
        # Ejecucion de bot
        YoutubeBot().iniciarBotYoutube()

        # Impresion y registro de log final      
        consola.imprimirFinal()
        logger.registroFinalProcesos()
    except Exception as e:
        logger.registrarLogEror(f"Except del main: {e}", "Ejecucion de Main")
        consola.imprimirError(f"Ocurrio un error en la ejecucion: {e}")
    
# endregion

# Metodo para ejecución del Script, invocando la función main()    
if __name__ == '__main__':
    main()