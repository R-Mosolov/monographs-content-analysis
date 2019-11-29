import os


def centralization():
    def create_full_path(path_link):
        directory_paths = os.listdir(path_link)
        paths_arr = []

        for path in directory_paths:
            if path != '.DS_Store':
                paths_arr.append(path_link + path)

        return paths_arr

    all_texts = ''

    scientific_books = create_full_path('dataset/scientific/')

    texts_arr = scientific_books

    for text in texts_arr:
        all_texts += open(text, 'r').read()

    return all_texts
