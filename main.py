import speech_recognition as sr
import datetime
import wikipedia as wk
import pyttsx3 as pyt
import datetime as dt
import pywhatkit as ms

audio = sr.Recognizer()
mic = sr.Microphone()
maquina = pyt.init()

def executa_comando():
    comando = ""
    try:
        with mic as source:
            audio.adjust_for_ambient_noise(source)
            voz = audio.listen(source)
            print(voz)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if "kira" in comando:
                comando = comando.replace("kira", "")
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
        horas = dt.datetime.now().strftime("%H horas e %M minutos")
        maquina.say("Agora são " + horas)
        maquina.runAndWait()
    elif "procure por" in comando:
        procurar = comando.replace("procure por", "")
        wk.set_lang("pt")
        result = wk.summary(procurar, 2)
        maquina.say(result)
        maquina.runAndWait()
    elif "toque" in comando:
        if "cantor" in comando:
            print("Falou do cantor")
            toque = comando.replace("toque", "").strip()
            cantor_index = comando.index("cantor") + len("cantor")
            cantor = comando[cantor_index:].strip()
            maquina.say(f"Tocando {toque} do cantor {cantor} em segundo plano")
            maquina.runAndWait()
            ms.playonyt(f"{toque} {cantor}")
        else:
            print("Música comum")
            toque = comando.replace("toque", "").strip()
            maquina.say(f"Tocando {toque} em segundo plano")
            maquina.runAndWait()
            ms.playonyt(toque)
    elif "mande uma mensagem" in comando:
            contact = ""
            msg = comando.replace("mande uma mensagem", "")
            hour, mins = datetime.datetime.now().strftime("%H"), (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%M")
            maquina.say(result)
            maquina.runAndWait()
            ms.sendwhatmsg(contact, msg, hour, mins)



while True:
    comando_voz_usuario()