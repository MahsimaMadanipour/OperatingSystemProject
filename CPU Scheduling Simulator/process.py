class Process():
    def __init__(self, name, arrival_t, service_t):
        self.name = name
        self.arrival_time = arrival_t
        self.service_time = service_t
        self.finish_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def calculate_turnaround_time(self):
        self.turnaround_time = self.finish_time - self.arrival_time

    def calculate_wating_time(self):
        self.waiting_time = self.turnaround_time - self.service_time