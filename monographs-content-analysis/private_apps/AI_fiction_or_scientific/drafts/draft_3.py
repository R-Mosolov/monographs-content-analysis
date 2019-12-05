def create_all_paths(book_type, book_class):
    all_paths = ''
    authors_last_names = ['defoe', 'dikkens', 'vern']

    for author_last_name in authors_last_names:
        all_paths += create_full_path('dataset/' + book_type + '/' + book_class + '/' + author_last_name + '/')

    return all_paths


print(create_all_paths('fiction', 'foreign'))