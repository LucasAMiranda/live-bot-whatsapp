import webbrowser
from time import sleep
import pyautogui
import pyperclip

# Função para localizar e clicar na caixa de mensagem automaticamente
def preencher_e_enviar_mensagem(mensagem):
    print("Procurando pela caixa de texto do WhatsApp Web...")
    for i in range(20):  # tenta por até 20 segundos
        try:
            caixa = pyautogui.locateCenterOnScreen('caixa_texto.png', confidence=0.6)
            if caixa:
                print(f'Caixa localizada na posição: {caixa}')
                pyautogui.click(caixa)  # clicar na caixa
                break
        except pyautogui.ImageNotFoundException:
            pass
        sleep(0.5)
    else:
        print("❌ Não consegui encontrar a caixa de texto.")
        return False
    
    # Copiar a mensagem para a área de transferência
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')  # Colar na caixa
    sleep(0.5)
    pyautogui.press('enter')  # Enviar
    print("✅ Mensagem enviada com sucesso.")
    return True

# Número de destino
numero_destino = "558298300281"

# Mensagem a ser enviada
mensagem = "Olá! Esta é uma mensagem automática enviada pelo script direta da Live Da LSCHOOL INFOTECH! ;) 🐍"

# Abrir WhatsApp Web
webbrowser.open('https://web.whatsapp.com/')
print("🔄 Por favor, escaneie o QR Code se necessário e aguarde o carregamento do WhatsApp Web...")
sleep(30)  # tempo para o WhatsApp carregar

# Instrução para clicar manualmente na barra de busca
print("👆 Posicione o cursor na barra de busca, clique nela e pressione Enter aqui no terminal.")
input("Pressione Enter para continuar após clicar na barra de busca...")

# Localizar a barra de busca na tela
print("🔍 Procurando pela barra de busca...")
for i in range(20):
    try:
        busca = pyautogui.locateCenterOnScreen('barra_busca.png', confidence=0.6)
        if busca:
            print(f"✅ Barra de busca encontrada na posição {busca}")
            pyautogui.click(busca)
            break
    except pyautogui.ImageNotFoundException:
        pass
    sleep(0.5)
else:
    print("❌ Não encontrei a barra de busca. Verifique a imagem e a tela.")
    exit()

# Digitar o número do contato
pyperclip.copy(numero_destino)
pyautogui.hotkey('ctrl', 'v')
sleep(1)
pyautogui.press('enter')
sleep(5)  # aguardar abrir o chat

# Enviar a mensagem
if preencher_e_enviar_mensagem(mensagem):
    print("🎉 Script finalizado com sucesso!")
else:
    print("⚠️ Falha ao enviar a mensagem.")
