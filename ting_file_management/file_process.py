import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for process in instance._data:
        if path_file in process["nome_do_arquivo"]:
            return
    content = txt_importer(path_file)
    formated_response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }
    instance.enqueue(formated_response)
    print(formated_response, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
