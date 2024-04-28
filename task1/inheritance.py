class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def make_call(self):
        print("Making a call...")

    def receive_call(self):
        print("Receiving a call...")

    def take_a_picture(self):
        print("Taking a picture...")

class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, model):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_face_id(self):
        print("Using Face ID...")

class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, model):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_fingerprint_scanner(self):
        print("Using fingerprint scanner...")

# Create some objects of Apple class with different properties
iphone_12 = Apple("Touch Screen", "5G", True, "12MP", "12MP", "4GB", "64GB", "iPhone 12")
iphone_11 = Apple("Touch Screen", "4G", False, "12MP", "12MP", "4GB", "64GB", "iPhone 11")

# Create some objects of Samsung class with different properties
s21 = Samsung("Touch Screen", "5G", True, "10MP", "64MP", "8GB", "128GB", "Galaxy S21")
s20 = Samsung("Touch Screen", "4G", False, "10MP", "64MP", "8GB", "128GB", "Galaxy S20")

# Use the objects
iphone_12.make_call()
iphone_11.receive_call()
iphone_12.take_a_picture()
s21.use_fingerprint_scanner()
iphone_11.use_face_id()