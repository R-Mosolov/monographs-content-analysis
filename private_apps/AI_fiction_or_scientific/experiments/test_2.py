import os

chehov_path = '../txt/fiction_literature/russian/Chehov/'
chehov = [chehov_path + 'Chehov_A._Chelovek_V_Futlyare_Sbornik.txt',
          chehov_path + 'Chehov_A._Polnoesobranie._Sobranie_Yumoristicheskih.txt',
          chehov_path + 'Chehov_A._Spisokshkolnoy._Vishnevyiyi_Sad.txt']


def create_full_path(path_link):
    test_paths = os.listdir(path_link)
    test_arr = []

    for path in test_paths:
        if path != '.DS_Store':
            test_arr.append(path_link + path)

    return test_arr


# handler(chehov_path)

print(chehov)
print(create_full_path('../txt/fiction_literature/russian/Chehov/'))
