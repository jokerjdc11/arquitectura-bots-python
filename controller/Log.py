# ===========================================================================
# Importaciones de clases y librerias necesarias
# ===========================================================================
# Region - Importaciones de librerias y archivos
from datetime import datetime, date, time, timedelta
from os import makedirs, path, getcwd
from controller.utils.Helpers import Helpers
from controller.utils.Configurations import Configurations
# Endregion - Importaciones de librerias y archivos

# ===========================================================================
# VARIABLES GLOBALES - LOCAL - INSTANCIA DE OBJETOS
# ===========================================================================
# Region
# Obtención de la ruta actual del proyecto
relativePath = getcwd()

# Instancia de la clase Helper
help = Helpers()
configuration = Configurations()

# Nombre de los archivos de logs de ejecución
nombreArchivoProceso ="LogProcesos_"+(datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d') +".txt"
nombreArchivoError ="LogErrores_"+(datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d') +".txt"
# Endregion

class Log:
    """
        Log
        ===
            Clase encargada de generar los logs del proceso,
            se entiende por log aquellos archivos de registros
            que se van generando en la ejecución del proceso.
        `Usos:`
            - Escritura de inicio de proceso
            - Escritura de finalización de proceso
            - Escritura de variables dadas en el proceso
            - Escritura de errores dados en el proceso
    """
    def __init__(self):
        """
            Metodo para inicializar la clase, siendo este
            el constructor de la misma, ayuda a validar
            que se tengan las carpetas correspondientes a los logs
        """
        self.__nombreArchivoEror = nombreArchivoError
        self.__nombreArchivoProceso = nombreArchivoProceso
        self.__tiempoActual = ""
        
        rutaCarpetaProcesos = configuration.getConfigValue("routes","UbicacionLogProceso")
        rutaCarpetaErrores = configuration.getConfigValue("routes","UbicacionLogError")
        
        if not(path.isdir(rutaCarpetaProcesos)):
            # Creación de la carpeta de logs de procesos, en caso de que no existe
            makedirs(rutaCarpetaProcesos)
        if not(path.isdir(rutaCarpetaErrores)):
            # Creación de la carpeta de logs de errores, en caso de que no existe
            makedirs(rutaCarpetaErrores)
            
    def gettiempoActual(self):
        return self.__tiempoActual
    
    def settiempoActual(self, tiempoActual):
        self.__tiempoActual = tiempoActual

    # Region - Metodos de escritura de logs
    
    def registroInicioProcesos(self):
        """
            Metodo que escribirá dentro del log de procesos, el 
            registro de la hora de inicio de ejecución del proceso.
            (Cambiar la cadena "NombreAutomatización" por el nombre del bot)
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        message = "============================================================================================================================\n"
        message+= "| INICIO DE APLICACION - NombreAutomatización | " + str(self.gettiempoActual()) + "|\n"
        message+= "============================================================================================================================\n"
        file = open(configuration.getConfigValue("routes","UbicacionLogProceso") + self.__nombreArchivoProceso, "a")
        file.write(message + "\n") 
        file.close()
    
    def registroFinalProcesos(self):
        """
            Metodo que escribirá dentro del log de procesos, el 
            registro de la hora en que se finalizo el proceso
            y su estado final: Exitoso o Fallido.
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= "| FINAL DE APLICACION | " + str(self.gettiempoActual()) + "\n"
        log+= "============================================================================================================================\n"
        file = open(configuration.getConfigValue("routes","UbicacionLogProceso") + self.__nombreArchivoProceso, "a")
        file.write(log + "\n") 
        file.close()
        
    def registrarLogProceso(self, nameProcess):
        """
            Metodo que escribirá dentro del log de procesos, el 
            nombre del proceso que se empezo a ejecutar.
            - `Args:`
                - nameProcess (str): Nombre del proceso en ejecución
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        Messagelog = "| Ejecutando la tarea --> ["+ nameProcess +"] --> Hora de ejecucion: " + str(self.gettiempoActual())
        file = open(configuration.getConfigValue("routes","UbicacionLogProceso") + self.__nombreArchivoProceso,"a")
        file.write(Messagelog + "\n") 
        file.close()
    
    # Metodo para registrar un nuevo subtitulo como seguimiento del proceso (CheckPoint)
    def registroSubtitulo(self, messageTitle):
        """
            Metodo que escribirá dentro del log de procesos, 
            un titulo referente a la ejecución del proceso
            - `Args:`
                - messageTitle (str): Titulo a registrar dentro del log
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= "| "+ messageTitle +" | " + str(self.gettiempoActual())  + "\n"
        log+= "============================================================================================================================\n"
        file = open(configuration.getConfigValue("routes","UbicacionLogProceso") + self.__nombreArchivoProceso, "a")
        file.write(log + "\n") 
        file.close()
        
    # Metodo para hacer una division en un log
    def registroSeparador(self):
        log = "============================================================================================================================"
        file = open(configuration.getConfigValue("routes","UbicacionLogProceso") + self.__nombreArchivoProceso, "a")
        file.write(log + "\n") 
        file.close()
    
    def registrarLogEror(self, error, procesoActual):
        """
            Metodo que escribirá dentro del log de errores, 
            el error que se genero y se dio manejo en el proceso,
            a la par que el nombre del proceso o metodo que genero
            el error
            - `Args:`
                - error (str): Error generado
                - procesoActual (str): Proceso o metodo del error
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= "| Se ha encontrado un error --> Hora detectada: " + str(self.gettiempoActual()) + "\n"
        log+= "| Ultimo estado (Tarea) --> " + procesoActual +  "\n"
        log+= "============================================================================================================================\n"
        log+= "| ERROR --> " + str(error) + "\n"
        file = open(configuration.getConfigValue("routes","UbicacionLogError") + self.__nombreArchivoEror, "a")
        file.write(log + "\n") 
        file.close()
        
    # Endregion - Metodos de escritura de logs
    