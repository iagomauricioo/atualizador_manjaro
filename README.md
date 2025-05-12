# Atualizador de Sistema para Manjaro (com Interface Gráfica)

Este é um pequeno script Python com interface gráfica (GUI) feito com `tkinter`, que pergunta ao usuário se deseja atualizar o sistema toda vez que ele liga o computador. Caso aceite, ele executa os comandos de atualização no terminal e oferece a opção de repetir a operação após o término.

---

## 🚀 Funcionalidades

- Interface simples perguntando: **"Quer atualizar o sistema?"**
- Executa os comandos:
  - `yay -Syyuu --noconfirm`
  - `sudo pacman -Syyuu --noconfirm`
- Mostra o terminal (`xterm`) com a saída completa do processo.
- Ao final, pergunta se o usuário deseja rodar novamente.

---

## 🛠️ Requisitos

Certifique-se de que os seguintes pacotes estão instalados:

```bash
sudo pacman -S tk xterm yay
```

## ▶️ Como executar
```python
python3 atualizador.py
```

## 🔄 Execução automática ao iniciar o sistema
Para que o script rode automaticamente sempre que o sistema for iniciado:

Crie a pasta de autostart (se não existir):

```bash
mkdir -p ~/.config/autostart
```
Crie o arquivo `~/.config/autostart/atualizador.desktop` com o seguinte conteúdo:

```bash
[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 /home/iago/atualizador/atualizador.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Atualizador de Sistema
Comment=Atualiza o Manjaro automaticamente ao iniciar
```
Lembre-se de ajustar o caminho do script (/home/iago/...) conforme necessário.

Torne o arquivo `.desktop` executável:

```bash
chmod +x ~/.config/autostart/atualizador.desktop
```