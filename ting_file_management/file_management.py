import sys


def txt_importer(path_file):           
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as arquivo: 
            content = arquivo.read()
            return content.splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


# video de como imprimor stderr => https://www.youtube.com/watch?v=ewCghx53Dgg
# como separar \n => https://www.w3schools.com/python/ref_string_splitlines.asp
