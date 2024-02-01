import openai
import speech_recognition as sr
import os

def reconhecer_fala():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("robob escutando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não entendi o áudio")
        return None
    except sr.RequestError:
        print("Erro de serviço; tente novamente")
        return None

def obter_resposta_openai(texto):
    openai.api_key = 'sua_chave'

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual inteligente chamado robibob"},
                {"role": "user", "content": texto}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Erro ao obter resposta da OpenAI: {e}")
        return None

def falar(texto):
    texto_unico = texto.replace('\n', ' ')
    os.system(f"say {texto_unico}")

def main():
    while True:  # Loop infinito
        texto = reconhecer_fala()
        if texto:
            resposta = obter_resposta_openai(texto)
            if resposta:
                print(f"robob: {resposta}")
                falar(resposta)

if __name__ == "__main__":
    main()
