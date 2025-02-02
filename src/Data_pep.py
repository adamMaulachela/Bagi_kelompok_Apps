import pandas as pd
import util as utils
import os


# load file config
config = utils.load_config()


# fungsi untuk konversi XLXS menjadi CSV hanya pada sheet tertentu saja
def xlsx_to_csv(input_file, output_folder):
    # membuat folder jika belum ada
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
        print(f"Folder '{output_folder}' berhasil dibuat")

    # baca isi file excel
    xls = pd.ExcelFile(input_file)

    # loop melalui setiap sheet dan konversi menjadi CSV
    for sheet_name in xls.sheet_names:
        # Baca sheet ke dalam DataFrame
        df = pd.read_excel(xls, sheet_name)

        # tentukan nama file CSV output di dalam folder
        output_file = os.path.join(output_folder, f"{sheet_name}.csv")

        # konversi DataFrame ke CSV
        df.to_csv(output_file, index=False)
        print(f"File {output_file} berhasil dibuat")


# read dataset
def read_data(return_file=True):

    # read data
    dataset_path = config["dataset"]
    dataset = pd.read_csv(dataset_path)

    # Dump pickle
    utils.pickle_dump(dataset, config["dataset_df"])
    print(f"File {config['dataset_df']} berhasil dibuat")

    if return_file:
        return dataset
