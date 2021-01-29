class WareHouse:
    __cnum = 0

    def __init__(self, name, location, equipment_dictionary):
        WareHouse.__cnum += 1
        self.num = WareHouse.__cnum
        self.name = name
        self.location = location
        self.ed = equipment_dictionary
        self.rest_oe = {}

    def __str__(self):
        return f"WH: name and location: {self.name} {self.location}"

    def print_all_rest(self):
        print(self.name + '\n' + 30 * '-')
        for key, value in self.rest_oe.items():
            print(key, self.ed.get_equipment(key).name, self.ed.get_equipment(key).price, value)
        print(30 * '-')

    def input_product(self, oe, qnt):
        try:
            self.ed.get_equipment(oe.sku)
        except EquipmentDictionaryNotFound:
            self.ed.add_equipment(oe)

        if self.rest_oe.get(oe.sku) is not None:
            self.rest_oe[oe.sku] += qnt
        else:
            self.rest_oe[oe.sku] = qnt

    def inner_move_product(self, hw_in, sku, qnt):
        try:
            self.ed.get_equipment(sku)  # если неверный sku, будет исключение
        except EquipmentDictionaryNotFound as e:
            print('неверный sku')
            return -1

        if self.rest_oe.get(sku) is not None:
            if self.rest_oe.get(sku) < qnt:
                print('недостаточно в остатке')
                return -1
            else:
                self.rest_oe[sku] -= qnt
                hw_in.input_product(self.ed.get_equipment(sku), qnt)


class OfficeEquipment:
    def __init__(self, sku, name, vendor_code, price):
        self.sku = sku
        self.name = name
        self.vendor_code = vendor_code
        self.price = price

    def __str__(self):
        return f"OE: name and price: {self.name} {self.price}"


class EquipmentDictionaryNotFound(Exception):
    def __init__(self, txt):
        self.txt = txt


class EquipmentDictionary:
    def __init__(self):
        self.__dct = {}
        
    def add_equipment(self, oeq):
        self.__dct[oeq.sku] = oeq

    def get_equipment(self, sku):
        if self.__dct.get(sku) is None:
            raise EquipmentDictionaryNotFound(f' EquipmentDictionary:get_equipment **NOT FOUND** SKU: {sku}')
        else:
            return self.__dct.get(sku)

    def print_all_sku(self):
        for key, value in self.__dct.items():
            print(value)


class Printer(OfficeEquipment):
    def __init__(self, sku, name, vendor_code, price, type_of_seal, interface):
        super().__init__(sku, name, vendor_code, price)
        self.type_of_seal = type_of_seal
        self.interface = interface


class Scanner(OfficeEquipment):
    def __init__(self, sku, name, vendor_code, price, interface):
        super().__init__(sku, name, vendor_code, price)
        self.interface = interface


class Copier(OfficeEquipment):
    def __init__(self, sku, name, vendor_code, price, type_of_seal):
        super().__init__(sku, name, vendor_code, price)
        self.interface = type_of_seal


oed = EquipmentDictionary()
wh1 = WareHouse('Главный склад', 'ул. Ленина 13', oed)
wh2 = WareHouse('Склад магазин', 'ул. Победы 14', oed)
oe1 = Printer(123, 'Принтер Epson-1120', 'Epson', 3500, 'laser', 'usb')
oe2 = Printer(124, 'Принтер Canon-150', 'Сanon', 3800, 'ink', 'usb')
wh1.input_product(oe1, 5)
wh1.input_product(oe1, 4)
wh1.input_product(oe2, 2)
wh1.inner_move_product(wh2, 124, 1)
wh1.inner_move_product(wh2, 123, 2)

wh1.print_all_rest()
wh2.print_all_rest()
# oed.print_all_sku()
