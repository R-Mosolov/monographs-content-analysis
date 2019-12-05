import os


def run():
    def create_full_path(path_link):
        directory_paths = os.listdir(path_link)
        paths_arr = []

        for path in directory_paths:
            if path != '.DS_Store':
                paths_arr.append(path_link + path)

        return paths_arr

    all_texts = ''
    universal_path = '../../../texts-datasets/AI_fiction_or_scientific/dataset/'

    defoe = create_full_path(universal_path + 'fiction/russian/Defoe/')
    dikkens = create_full_path(universal_path + 'fiction/foreign/Dikkens/')
    vern = create_full_path(universal_path + 'fiction/foreign/Vern/')

    bulgakov = create_full_path(universal_path + 'fiction/russian/Bulgakov/')
    chehov = create_full_path(universal_path + 'fiction/russian/Chehov/')
    dostoevskiy = create_full_path(universal_path + 'fiction/russian/Dostoevskiy/')
    gogol = create_full_path(universal_path + 'fiction/russian/Gogol/')
    pushkin = create_full_path(universal_path + 'fiction/russian/Pushkin/')
    tolstoy = create_full_path(universal_path + 'fiction/russian/Tolstoy/')
    turgenev = create_full_path(universal_path + 'fiction/russian/Turgenev/')

    texts_arr = (defoe + dikkens + vern) + (bulgakov + chehov + dostoevskiy + gogol + pushkin + tolstoy + turgenev)

    for text in texts_arr:
        all_texts += open(text, 'r').read()

    return all_texts
