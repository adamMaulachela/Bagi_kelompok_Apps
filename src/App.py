import os
import Data_pep
import Model
import util as utils
import streamlit as st

if __name__ == "__main__":

    # load config file
    config = utils.load_config()

    # UPLOAD FOLDER
    UPLOAD_FOLDER = "/Users/adam/Documents/Projects/Bagi_kelompok_Apps/data/raw"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # judul aplikasi
    st.title("Aplikasi Roulette Groups LP3M UNDIKMA")

    # Deskripsi
    st.write("Aplikasi ini digunakan untuk melakukan pembagian kelompok PLP")

    # upload file
    uploaded_file = st.file_uploader("Pilih File Excel(.xlsx)", type=["xlsx"])

    if uploaded_file is not None:

        # simpan file ke dalam folder 'data/raw'
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"File berhasil diupload dan tersimpan di '{file_path}'")

        # konfigurasi parameter untuk method xlsx_to_csv
        input_file = config["dataraw_path"]
        output_folder = (
            "/Users/adam/Documents/Projects/Bagi_kelompok_Apps/data/processed"
        )

        # menjalankan method xlsx_to_csv
        dataset = Data_pep.xlsx_to_csv(input_file, output_folder)

        # ubah data csv menjadi dataframe dan simpan sebagai pickle file
        data_df = Data_pep.read_data()

        # load data pickle file
        data = Model.load_dataset()

        # menjalankan method bagi_kelompok dan save_to_csv
        kelompok = Model.bagi_kelompok(data)

        # membaca hasil kelompok
        csv_file_path = config["kelompok"]
        with open(csv_file_path, "rb") as f:
            csv_data = f.read()

        # tombol download file CSV
        st.download_button(
            label="Hasil Kelompok CSV",
            data=csv_data,
            file_name=os.path.basename(csv_file_path),
            mime="text/csv",
        )
