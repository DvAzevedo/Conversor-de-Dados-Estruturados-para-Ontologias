import os
import subprocess
import sys

def create_venv():
    venv_name = 'venv_conversor'  # Nome do ambiente virtual
    if not os.path.exists(venv_name):
        print(f"Criando o ambiente virtual: {venv_name}")
        subprocess.run([sys.executable, '-m', 'venv', venv_name])
    else:
        print(f"O ambiente virtual '{venv_name}' já existe.")

def install_requirements():
    # Define o caminho para o executável pip
    venv_pip = os.path.join('venv_conversor', 'bin', 'pip')  # Caminho para pip no Linux/Mac
    if os.name == 'nt':  # Se estiver no Windows
        venv_pip = os.path.join('venv_conversor', 'Scripts', 'pip.exe')
    
    # Verifica se o executável pip existe
    if not os.path.exists(venv_pip):
        print(f"Erro: O executável '{venv_pip}' não foi encontrado. Verifique se o ambiente virtual foi criado corretamente.")
        return
    
    print("Instalando dependências...")
    subprocess.run([venv_pip, 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    create_venv()
    install_requirements()
