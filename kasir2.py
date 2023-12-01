import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

qt_creator_file = "kasir.ui"  # Import UI dari QtDesigner
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.edit_mode = False
        self.connection = self.connect()

        self.btncari.clicked.connect(self.cari_data)
        self.btntambah.clicked.connect(self.tambah_data)
        self.btnhapus.clicked.connect(self.hapus_data)
        self.btnclear.clicked.connect(self.bersihkan)
        self.btnedit.clicked.connect(self.edit_data)

        self.gridBarang.setHorizontalHeaderLabels(
            ['ID', 'Nama Barang', 'Harga Beli', 'Harga Jual', 'Dari Toko', 'Tanggal Masuk', 'QT Barang', 'Kode Barang']
        )

        self.select_data()

    def connect(self):
        return mc.connect(
            host="localhost",  # koneksi ke mysql menggunakan localhost
            user="root",
            password="",
            database="kasirdb"  # nama database
        )

    def select_data(self):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute("SELECT * FROM barang")
            result = mycursor.fetchall()

            self.gridBarang.setRowCount(len(result))

            for row_number, row_data in enumerate(result):
                self.gridBarang.setItem(
                    row_number, 0, QTableWidgetItem(str(row_data[0]))
                )
                for column_number in range(1, len(row_data)):
                    self.gridBarang.setItem(
                        row_number, column_number, QTableWidgetItem(str(row_data[column_number]))
                    )

        except mc.Error as e:
            self.handle_error("Terjadi kesalahan koneksi data", e)

    def cari_data(self):
        try:
            id_barang = self.txtid.text()
            mycursor = self.connection.cursor()
            query = "SELECT * FROM barang WHERE id = %s"
            mycursor.execute(query, (id_barang,))

            result = mycursor.fetchone()
            if result:
                self.populate_entry_fields(result)
                self.btnedit.setText("Update")
                self.edit_mode = True
                self.btnhapus.setEnabled(True)
                self.btnhapus.setStyleSheet("background-color : red")
            else:
                self.message_box("INFO", "Data tidak ditemukan")
                self.clear_entry_fields()

        except mc.Error as e:
            self.handle_error("Terjadi kesalahan koneksi data", e)

    def edit_data(self):
        try:
            nama_barang = self.txtnama.text()
            harga_beli = self.txthrgbeli.text()
            harga_jual = self.txtjual.text()
            dari_toko = self.txtasal.text()
            tanggal_masuk = self.txttanggal.text()
            qt_barang = self.txtqt.text()

            mycursor = self.connection.cursor()
            if not self.edit_mode:
                self.insert_data(mycursor, nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang)
            else:
                self.update_data(mycursor, nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang)

            self.edit_mode = False
            self.clear_entry_fields()
            self.select_data()

        except mc.Error as e:
            self.handle_error("Terjadi kesalahan koneksi data", e)

    def insert_data(self, cursor, nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang):
        val = (nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang, self.txtkode.text())
        sql = "INSERT INTO barang (nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang, kode_barang) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, val)
        self.connection.commit()
        if cursor.rowcount > 0:
            self.message_box("SUKSES", "Data Barang Tersimpan")
        else:
            self.message_box("GAGAL", "Data Barang Gagal Tersimpan")

    def update_data(self, cursor, nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang):
        sql = "UPDATE barang SET nama_barang = %s, harga_beli=%s, harga_jual=%s, dari_toko=%s, tanggal_masuk=%s, qt_barang=%s, kode_barang=%s WHERE id=%s"
        val = (nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang, self.txtkode.text(), self.txtid.text())
        cursor.execute(sql, val)
        self.connection.commit()
        if cursor.rowcount > 0:
            self.message_box("SUKSES", "Data Barang Diperbarui")
        else:
            self.message_box("GAGAL", "Data Barang Gagal Diperbarui")

    def hapus_data(self):
        try:
            id_barang = self.txtid.text()
            mycursor = self.connection.cursor()

            if self.edit_mode:
                sql = "DELETE FROM barang WHERE id=%s"
                mycursor.execute(sql, (id_barang,))
                self.connection.commit()
                if mycursor.rowcount > 0:
                    self.message_box("SUKSES", "Data Barang Dihapus")
                else:
                    self.message_box("GAGAL", "Data Barang Gagal Dihapus")

                self.clear_entry_fields()
                self.select_data()
            else:
                self.message_box("ERROR", "Sebelum menghapus data harus ditemukan terlebih dahulu")

            self.edit_mode = False

        except mc.Error as e:
            self.handle_error("Terjadi kesalahan koneksi data", e)

    def tambah_data(self):
        try:
            nama_barang = self.txtnama.text()
            harga_beli = self.txthrgbeli.text()
            harga_jual = self.txtjual.text()
            dari_toko = self.txtasal.text()
            tanggal_masuk = self.txttanggal.text()
            qt_barang = self.txtqt.text()
            kode_barang = self.txtkode.text()

            mycursor = self.connection.cursor()
            self.insert_data(mycursor, nama_barang, harga_beli, harga_jual, dari_toko, tanggal_masuk, qt_barang)

            self.clear_entry_fields()
            self.select_data()

        except mc.Error as e:
            self.handle_error("Terjadi kesalahan koneksi data", e)

    def bersihkan(self):
        self.clear_entry_fields()

    def clear_entry_fields(self):
        self.txtnama.setText("")
        self.txthrgbeli.setText("")
        self.txtjual.setText("")
        self.txtasal.setText("")
        self.txttanggal.setText("")
        self.txtqt.setText("")
        self.txtkode.setText("")
        self.txtnama.setFocus()

    def populate_entry_fields(self, result):
        self.txtnama.setText(result[1])
        self.txthrgbeli.setText(str(result[2]))
        self.txtjual.setText(str(result[3]))
        self.txtasal.setText(result[4])
        self.txttanggal.setText(str(result[5]))
        self.txtqt.setText(str(result[6]))
        self.txtkode.setText(str(result[7]))

    def message_box(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def handle_error(self, message, exception):
        error_message = f"{message}\nError details: {str(exception)}"
        self.message_box("ERROR", error_message)
        # Add the following line to print the error traceback
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
