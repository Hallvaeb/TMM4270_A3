

class IDGenerator():
    """
        Makes unique IDs for 
        Customer
        Gearbox
        Order
    """
    # [Name, address, phone, email, material, color, radius_list[]]
    # fil = form input list
    def create_customer_id(fil):
        email = fil[3]
        return email

    def create_gearbox_id(fil):
        radius_list = fil[-1]
        str_list = str(radius_list).replace(" ", "")
        return str_list

    def create_order_id(fil):
        gearbox_id = IDGenerator.create_gearbox_id(fil) 
        customer_id = IDGenerator.create_customer_id(fil)
        mat = IDGenerator.get_material_number(fil)
        col = IDGenerator.get_color_number(fil)
        order_id = gearbox_id + customer_id + mat + col
        return order_id
       

    def create_all_ids(fil):
        """
        """
        gearbox_id = IDGenerator.create_gearbox_id(fil) 
        customer_id = IDGenerator.create_customer_id(fil)
        order_id = IDGenerator.create_order_id(fil)
        return gearbox_id, customer_id, order_id

    def get_material_number(fil):
        material = fil[4]
        material_number = {
            "Brass": 1,
            "Steel": 2,
            "Diamond": 3,
            "Uncertain": 4
        }
        return material_number.get(material, 0)

    def get_color_number(fil):
        color = fil[5]
        color_number = {
            "None": 1,
            "Have it painted": 2,
            "Uncertain": 3
        }
        return color_number.get(color, 0)