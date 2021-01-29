class WareHouse:
    def __init__(self, num, name, location):
        self.num = num
        self.name = name
        self.location = location


class OfficeEquipment:
    def __init__(self, sku, name, vendor_code, price):
        self.sku = sku
        self.name = name
        self.vendor_code = vendor_code
        self.price = price


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
