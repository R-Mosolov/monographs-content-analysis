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

    defoe = create_full_path('dataset/fiction/foreign/Defoe/')

    texts_arr = defoe

    for text in texts_arr:
        all_texts += open(text, 'r').read()

    return all_texts
