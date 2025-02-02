import Data_pep
import Model
import util as utils

if __name__ == "__main__":

    # load config file
    config = utils.load_config()

    # konfigurasi parameter untuk method xlsx_to_csv
    input_file = config["dataraw_path"]
    output_folder = "data/processed"

    # menjalankan method xlsx_to_csv
    dataset = Data_pep.xlsx_to_csv(input_file, output_folder)

    # ubah data csv menjadi dataframe dan simpan sebagai pickle file
    data_df = Data_pep.read_data()

    # load data pickle file
    data = Model.load_dataset()

    # menjalankan method bagi_kelompok dan save_to_csv
    kelompok = Model.bagi_kelompok(data)
