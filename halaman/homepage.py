from kivy.uix.screenmanager import  Screen

class HomepageScreen(Screen):
    pass
        
        
"""# Top Search Bar
        self.add_widget(TextInput(hint_text='Search categories...', size_hint=(1, 0.1)))
        
        # Categories
        categories_layout = BoxLayout(size_hint=(1, 0.1))
        categories = ['Vegetables', 'Fruits', 'Spices', 'Holiday Sales']
        for category in categories:
            btn = Button(text=category)
            categories_layout.add_widget(btn)
        self.add_widget(categories_layout)
        
        # Today's Special Label
        self.add_widget(Label(text="Today's Special", size_hint=(1, 0.1)))
        
        # Products List
        products_layout = BoxLayout(size_hint=(1, 0.7), orientation='horizontal')
        
        products = [
            {"name": "Broccoli", "image": "broccoli.png", "price": "IDR 15.000/kg"},
            {"name": "Tomato", "image": "tomato.png", "price": "IDR 20.000/kg"},
            {"name": "Banana", "image": "banana.png", "price": "IDR 12.000/kg"},
            {"name": "Strawberry", "image": "strawberry.png", "price": "IDR 35.000/kg"}
        ]
        
        for product in products:
            product_box = BoxLayout(orientation='vertical')
            product_box.add_widget(Image(source=product["image"]))
            product_box.add_widget(Label(text=product["name"]))
            product_box.add_widget(Label(text=product["price"]))
            products_layout.add_widget(product_box)
        
        self.add_widget(products_layout)

if __name__ == '__main__':
    ProductApp().run()
"""