class Popular_products:
    def __init__(self, image, name, summa)
        self.image = image
        self.name = name
        self.summa = summa

    def get_object_info(self):
        return f"{self.name} - {self.summa} - {self.image}"


obj1 = Popular_products('Гарри Поттер, Дж. К, Роулинг Полное собрание, комплект из 8 книг', 399_000, "https://uzum.uz/ru/product/garri-potter-dzh-135606")
obj2 = Popular_products('Гарри Поттер, Дж. К, Роулинг Полное собрание, комплект из 8 книг', 399_000, "https://uzum.uz/ru/product/garri-potter-dzh-135606")
obj3 = Popular_products('Гарри Поттер, Дж. К, Роулинг Полное собрание, комплект из 8 книг', 399_000, "https://uzum.uz/ru/product/garri-potter-dzh-135606")
database = [obj1, obj2, obj3]
def popular_products():
    return database[:5]
