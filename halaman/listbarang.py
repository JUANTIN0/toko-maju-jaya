from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty


class ListBarangScreen(Screen):
    list_barang_grid = ObjectProperty(None)  # Referensi ke GridLayout di dalam ScrollView

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.barang_list = []  # List untuk menyimpan data barang

    def add_barang(self, nama, harga, gambar):
        """Menambahkan barang baru ke daftar dan ke UI."""
        # Simpan barang ke daftar
        self.barang_list.append({'nama': nama, 'harga': harga, 'gambar': gambar})

        # Buat widget untuk barang
        barang_box = BoxLayout(size_hint_y=None, height=120, padding=10, spacing=10)

        # Gambar Barang
        barang_box.add_widget(Image(source=gambar, size_hint_x=None, width=100))

        # Informasi Barang
        info_box = BoxLayout(orientation="vertical", padding=(5, 5))
        info_box.add_widget(Label(text=nama, font_size=16, halign="left", valign="middle", size_hint_y=None, height=40))
        info_box.add_widget(Label(text=f"Rp {harga}", font_size=14, halign="left", valign="middle", color=(0, 166/255, 81/255, 1)))
        barang_box.add_widget(info_box)

        # Tombol Aksi
        action_box = BoxLayout(orientation="vertical", size_hint_x=None, width=100, spacing=5)
        action_box.add_widget(Button(text="Edit", size_hint_y=None, height=40, on_press=lambda x: self.edit_barang(nama)))
        action_box.add_widget(Button(text="Hapus", size_hint_y=None, height=40, on_press=lambda x: self.remove_barang(barang_box, nama)))
        barang_box.add_widget(action_box)

        # Tambahkan ke GridLayout
        self.list_barang_grid.add_widget(barang_box)

    def edit_barang(self, nama):
        """Fungsi untuk mengedit barang (placeholder)."""
        print(f"Edit barang: {nama}")

    def remove_barang(self, barang_widget, nama):
        """Fungsi untuk menghapus barang dari daftar dan UI."""
        print(f"Hapus barang: {nama}")
        # Hapus barang dari daftar
        self.barang_list = [b for b in self.barang_list if b['nama'] != nama]
        # Hapus widget dari UI
        self.list_barang_grid.remove_widget(barang_widget)
