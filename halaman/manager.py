from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

class OrderItem(BoxLayout):
    order_name = StringProperty("")
    order_status = StringProperty("")

class ManagerScreen(Screen):
    def on_pre_enter(self, *args):
        # Contoh data pesanan
        orders = [
            {"order_name": "Order #001", "order_status": "In Progress"},
            {"order_name": "Order #002", "order_status": "Completed"},
            {"order_name": "Order #003", "order_status": "Pending"}
        ]
        # Isi data ke RecycleView
        self.ids.order_list.data = [
            {'order_name': order['order_name'], 'order_status': order['order_status']} for order in orders
        ]