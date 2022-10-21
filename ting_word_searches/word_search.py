def exists_word(word, instance):
    word_occurrences = []
    the_word = word.upper()
    for content in instance._data:
        for index, line in enumerate(content["linhas_do_arquivo"]):
            if the_word in line.upper():
                word_occurrences.append({"linha": index + 1})
    if word_occurrences:
        return [{
            "palavra": word,
            "arquivo": content["nome_do_arquivo"],
            "ocorrencias": word_occurrences,
        }]
    return word_occurrences


def search_by_word(word, instance):
    word_occurrences = []
    the_word = word.upper()
    for content in instance._data:
        for index, line in enumerate(content["linhas_do_arquivo"]):
            if the_word in line.upper():
                word_occurrences.append({"linha": index + 1, "conteudo": line})
    if word_occurrences:
        return [{
            "palavra": word,
            "arquivo": content["nome_do_arquivo"],
            "ocorrencias": word_occurrences,
        }]
    return word_occurrences
