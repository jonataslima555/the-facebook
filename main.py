import sys
import os

# Adiciona o diretório `core` ao caminho de módulos do Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from core import creator  # Agora você pode importar sem erros

if __name__ == "__main__":
    creator.menu()
