import sys
import os
from typing import Optional

import psutil
import requests


class ProcessInfo:
    def __init__(self):
        self.pid = os.getpid()
        self.nome_app = os.path.basename(sys.executable)  # Obtém o nome do executável .exe
        self.diretorio_app = sys.executable  # Obtém o diretório do executável
        self.public_ip = self.get_public_ip()

    def pid_exists(self, pid: str):
        """Verifica se um PID existe na lista de processos."""
        for proc in psutil.process_iter(['pid']):
            if proc.pid == pid:
                return True
        return False

    def get_pid(self):
        return self.pid

    def get_diretorio_app(self):
        return self.diretorio_app

    def get_nome_app(self):
        return self.nome_app

    def get_public_ip(self) -> Optional[str]:
        try:
            response = requests.get('https://api.ipify.org?format=json')
            data = response.json()
            ip = data['ip']
            return ip
        except Exception:
            return

    def encerrar_processo_atual(self):
        try:
            os.kill(self.pid, 9)
        except Exception as e:
            print(f"Falha ao encerrar o processo: {e}")

    def is_process_on(self) -> bool:
        cont = 0
        for proc in psutil.process_iter(attrs=['pid', 'name', 'exe']):
            try:
                if proc.name() == self.nome_app and os.path.abspath(proc.exe()) == self.diretorio_app:
                    cont += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                pass

        if cont > 2:
            return True

        return False
