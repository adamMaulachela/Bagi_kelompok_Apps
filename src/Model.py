import pandas as pd
import util as utils
from collections import defaultdict


# load file config
config = utils.load_config()


def load_dataset(return_file=True):

    # load pickel file
    dataset = utils.pickle_load(config["dataset_df"])

    if return_file:
        return dataset


def bagi_kelompok(data, min_group=5, max_group=10, max_prodi=3):
    """
    Membagi mahasiswa menjadi kelompok PLP berdasarkan kriteria

    Args:
        data (pd.DataFrame): Data mahasiswa dengan kolom 'Nama','NIM','Prodi'
        min_group (int, optional): Jumlah min mahasiswa per kelompok.
        Defaults to 5.
        max_group (int, optional): Jumlah max mahasiswa per kelompok.
        Defaults to 10.
        max_prodi (int, optional): Jumlah maks mhs dari prodi dengan
        mahasiswa terbanyak. Defaults to 3.

    Return:
        dict: kelompok yang telah terbagi
    """

    # hitung jumlah mahasiswa per prodi
    prodi_counts = data["Prodi"].value_counts()
    # prodi dengan mahasiswa terbanyak
    pop_prodi = prodi_counts.idxmax()

    # kumpulkan mahsiswa berdasarkan prodi
    prodi_groups = defaultdict(list)
    for _, row in data.iterrows():
        prodi_groups[row["Prodi"]].append(row)

    # Buat kelompok
    groups = []
    temp_group = []

    while any(prodi_groups.values()):
        for prodi, members in prodi_groups.items():
            if prodi == pop_prodi and len(temp_group) < max_group:
                to_add = min(max_prodi, len(members), max_group - len(temp_group))
            else:
                to_add = min(1, len(members), max_group - len(temp_group))

            temp_group.extend(members[:to_add])
            prodi_groups[prodi] = members[to_add:]

        if len(temp_group) >= min_group:
            groups.append(temp_group)
            temp_group = []

    if temp_group:
        groups.append(temp_group)

    for group, members in enumerate(groups):
        print(f"Kelompok {group+1}:")
        for member in members:
            print(
                f"  - Nama: {member['Nama']}, NIM: {member['NIM']}, Prodi: {member['Prodi']}"
            )

    output_path_file = config["kelompok"]
    results = []
    for group_name, members in enumerate(groups):
        for member in members:
            results.append(
                {
                    "Kelompok": group_name + 1,
                    "nama": member["Nama"],
                    "nim": member["NIM"],
                    "prodi": member["Prodi"],
                }
            )

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path_file, index=False)
    print(f"Hasil pembagian kelompok dalam file: {output_path_file}")
