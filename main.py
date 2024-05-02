import speech_recognition as sr
import wikipedia as wk
import pyttsx3 as pyt
import datetime as dt
import pywhatkit as ms

audio = sr.Recognizer()
mic = sr.Microphone()
maquina = pyt.init()

def executa_comando():
    try:
        with mic as source:
            audio.adjust_for_ambient_noise(source)
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if "alfred" in comando:
                comando = comando.replace("alfred", "")
                maquina.say(comando)
                maquina.runAndWait()
    except sr.UnknownValueError:
        maquina.say("Não entendi o que você disse")
        maquina.runAndWait()
    except sr.RequestError as e:
        error = f"Não foi possível obter os resultados; {e}"
        maquina.say(error)
        maquina.runAndWait()

    return comando

def comando_voz_usuario():  
    comando = executa_comando()
    if "horas" in comando:
        horas = dt.datetime.now().strftime("%H%M")
        maquina.say("Agora são " + horas)
        maquina.runAndWait()
    elif "procure por" in comando:
        procurar = comando.replace("procure por", "")
        wk.set_lang("pt")
        result = wk.summary(procurar, 2)
        maquina.say(result)
        maquina.runAndWait()
    elif "toque" in comando:
        toque = comando.replace("toque", "")
        result = []



comando_voz_usuario()