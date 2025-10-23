import os
import shutil
from pathlib import Path
import time

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / 'novo-diretorio')

arquivo = open(ROOT_PATH / "novo_texto.txt", "w")
arquivo.write("Conteúdo do novo arquivo de texto.")
arquivo.close()

time.sleep(2)

os.rename(ROOT_PATH / "novo_texto.txt", ROOT_PATH / "aran.txt")

time.sleep(2)

#shutil.copy(ROOT_PATH / "aran.txt", ROOT_PATH / "aran_copia.txt")


#os.remove(ROOT_PATH / "aran.txt")

os.mkdir(ROOT_PATH / 'novo-diretorio')

time.sleep(3)

shutil.move(ROOT_PATH / "aran.txt", ROOT_PATH / "novo-diretorio/aran.txt")