class ShortestProcessNext():
    def __init__(self, process_num, processes_list):
        self.processes_number = process_num
        self.processes = processes_list
        self.time = 0
        self.context_switch = 0

    def running_algorithm(self):

        while True:
            arrived_shortest_services = [process for process in self.processes if process.finish_time == 0 and process.arrival_time <= self.time]
            if len(arrived_shortest_services):
                shortest = arrived_shortest_services[0]
                for a in arrived_shortest_services:
                    if shortest.service_time > a.service_time:
                        shortest = a
                running_process = shortest
                print("--> Running Process: {}".format(running_process.name))
                self.time += running_process.service_time
                running_process.finish_time = self.time
                running_process.calculate_turnaround_time()
                running_process.calculate_wating_time()
                print("{} Turnaround Time: {}".format(running_process.name, running_process.turnaround_time))
                print("{} Waiting Time: {}".format(running_process.name, running_process.waiting_time))
                self.time += self.context_switch
            else:
                break

        print("--> Finishing Time:",self.time)
                