import os

chehov_path = '../dataset/fiction/russian/Chehov/'
chehov = [chehov_path + 'Chehov_A._Chelovek_V_Futlyare_Sbornik.dataset',
          chehov_path + 'Chehov_A._Polnoesobranie._Sobranie_Yumoristicheskih.dataset',
          chehov_path + 'Chehov_A._Spisokshkolnoy._Vishnevyiyi_Sad.dataset']


def create_full_path(path_link):
    test_paths = os.listdir(path_link)
    test_arr = []

    for path in test_paths:
        if path != '.DS_Store':
            test_arr.append(path_link + path)

    return test_arr


# handler(chehov_path)

print(chehov)
print(create_full_path('../dataset/fiction/russian/Chehov/'))
