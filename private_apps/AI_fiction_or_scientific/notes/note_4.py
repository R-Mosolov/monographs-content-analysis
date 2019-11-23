all_texts = ''

# scientific_books = create_full_path('txt/scientific/')

defoe = create_full_path('txt/fiction/foreign/Defoe/')
dikkens = create_full_path('txt/fiction/foreign/Dikkens/')
vern = create_full_path('txt/fiction/foreign/Vern/')

bulgakov = create_full_path('txt/fiction/russian/Bulgakov/')
chehov = create_full_path('txt/fiction/russian/Chehov/')
dostoevskiy = create_full_path('txt/fiction/russian/Dostoevskiy/')
gogol = create_full_path('txt/fiction/russian/Gogol/')
pushkin = create_full_path('txt/fiction/russian/Pushkin/')
tolstoy = create_full_path('txt/fiction/russian/Tolstoy/')
turgenev = create_full_path('txt/fiction/russian/Turgenev/')

# texts_arr = scientific_books
texts_arr = (defoe + dikkens + vern) + (bulgakov + chehov + dostoevskiy + gogol + pushkin + tolstoy + turgenev)

for text in texts_arr:
    all_texts += open(text, 'r').read().lower()

print(all_texts)


# OR


scientific_books = create_full_path('txt/scientific/')
texts_arr = scientific_books