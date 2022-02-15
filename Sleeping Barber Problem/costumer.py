class Costumer():
    def __init__(self, name, arrival_t, service_t):
        self.name = name
        self.arrival_time = arrival_t
        self.service_time = service_t
        self.waiting_time = 0