import os
import glob

diretorio = "arquivos/"
extensao = ".txt"

prefixo = "Segunda_Forma"

arquivos = glob.glob(os.path.join(diretorio, '*{}'.format(extensao)))

for arquivo_old in arquivos:
    nome_arquivo = os.path.basename(arquivo_old)
    novo_nome = os.path.join(diretorio, prefixo + nome_arquivo )
    os.rename(arquivo_old, novo_nome)