import struct as st

def abreWave (waveFile):
    #utilizamos gestor de contexto:
    with open(waveFile,'rb') as fwave:
        #pase lo que pase dentro de aquí, esto se cerrará
        format = '<4sI4s'
        buffer = fwave.read(st.calcsize(format))
        chunkID, chunkSize, fmtWave = st.unpack(format,buffer)
        if chunkID != b'RIFF' or fmtWave != b'WAVE':
            raise Exception ('Error en el fichero no tiene formato wav') # esto genera un traceback, aunque no te informa porqué
        format = '<4sI2H2I2H'
        buffer = fwave.read(st.calcsize(format))
        schunk1ID,schunk1Size,aformat,nchannels,srate,brate,blockAlign,bitsperSample = st.unpack(format,buffer)
        #todo cacho empieza con 4s:
        format = '<4sI'
        buffer = fwave.read(st.calcsize(format))
        schunk2ID,schunk2Size = st.unpack(format,buffer)
        numMuestras = schunk2Size // blockAlign
        format = f'<{numMuestras}h'
        buffer = fwave.read(st.calcsize(format))
        data = st.unpack(format, buffer)
    return data
    # return chunkID, chunkSize,fmtWave,schunk1ID,schunk1Size,aformat,nchannels,srate,brate,blockAlign,bitsperSample