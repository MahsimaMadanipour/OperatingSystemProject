class ShortestRemainingTime():
    def __init__(self, process_num, processes_list):
        self.processes_number = process_num
        self.processes = processes_list
        self.time = 0
        self.context_switch = 0
        
    def running_algorithm(self):
        service_times = [[process.name, process.service_time] for process in self.processes]

        last_process = " "
        while True:
            arrived_services = [process for process in self.processes if process.finish_time == 0 and process.arrival_time <= self.time]
            if len(arrived_services):
                shortest = arrived_services[0]
                for a in arrived_services:
                    if shortest.service_time > a.service_time:
                        shortest = a
                running_service = shortest
                if running_service.name != last_process:
                    print("--> Running Process: {}".format(running_service.name))
                self.time += 1
                running_service.service_time -= 1
                last_process = running_service.name
                if running_service.service_time == 0:
                    running_service.finish_time = self.time
                    for s in service_times:
                        if running_service.name == s[0]:
                            running_service.service_time = s[1]
                            break
                    running_service.calculate_turnaround_time()
                    running_service.calculate_wating_time()
                    print("{} Turnaround Time: {}".format(running_service.name, running_service.turnaround_time))
                    print("{} Waiting Time: {}".format(running_service.name, running_service.waiting_time))
                self.time += self.context_switch
            else:
                break

        print("--> Finishing Time:",self.time)