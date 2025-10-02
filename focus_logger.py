import time
import logging
import win32gui

# Configurações do log
logging.basicConfig(
    filename="distractions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def get_active_window_title():
    """Retorna o título da janela ativa"""
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def monitor_focus(main_app="Visual Studio Code"):
    """Monitora quando você perde o foco da janela principal"""
    last_window = ""
    while True:
        active_window = get_active_window_title()
        if active_window != last_window:
            if main_app not in active_window:
                logging.info(f"Perdeu o foco → {active_window}")
            last_window = active_window
        time.sleep(2)
