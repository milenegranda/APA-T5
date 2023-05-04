import struct as st

#Siguiendo la función trabajada en clase empezamos la tarea a realizar usando ésta:
def abreWave (fichero):
    #utilizamos gestor de contexto:
    with open(fichero,'rb') as fwave:
        #pase lo que pase dentro de aquí, esto se cerrará
        cabecera = '<4sI4s'
        buffer = fwave.read(st.calcsize(cabecera))
        #Asignamos variables que sacamos del buffer
        chunkID, chunkSize, formato = st.unpack(cabecera,buffer)
        if chunkID != b'RIFF' or formato != b'WAVE':
            raise Exception ('Error en el fichero no tiene formato wav') # esto genera un traceback, aunque no te informa porqué
        schunk1= '<4sI2H2I2H'
        buffer = fwave.read(st.calcsize(schunk1))
        schunk1ID,schunk1Size,aformat,nchannels,srate,brate,blockAlign,bitsperSample = st.unpack(schunk1,buffer)
        #todo cacho empieza con 4s:
        schunk2 = '<4sI'
        buffer = fwave.read(st.calcsize(schunk2))
        schunk2ID,schunk2Size = st.unpack(schunk2,buffer)
        numMuestras = schunk2Size // blockAlign
        datos = f'<{numMuestras}h'
        buffer = fwave.read(st.calcsize(format))
        Datos = st.unpack(datos, buffer)
        
        return chunkID, chunkSize,formato,schunk1ID,schunk1Size,aformat,nchannels,srate,brate,blockAlign,bitsperSample,Datos

#definimos la función que creará la cabecera de nuestro fichero:

def creaCabecera (sampleRate,numCanales, bitsperSample,)