class FirstComeFirstServed():
    def __init__(self, process_num, processes_list):
        self.processes_number = process_num
        self.processes = processes_list
        self.time = 0
        self.context_switch = 0

    def running_algorithm(self):
        arrival_times = sorted(list(set([process.arrival_time for process in self.processes])))

        for arrival_t in arrival_times:
            if self.time < arrival_t:
                self.time = arrival_t
            turn_processes = [process for process in self.processes if process.arrival_time == arrival_t]
            for turn_process in turn_processes:
                print("--> Running Process: {}".format(turn_process.name))
                self.time += turn_process.service_time
                turn_process.finish_time = self.time
                turn_process.calculate_turnaround_time()
                turn_process.calculate_wating_time()
                print("{} Turnaround Time: {}".format(turn_process.name, turn_process.turnaround_time))
                print("{} Waiting Time: {}".format(turn_process.name, turn_process.waiting_time))
                self.time += self.context_switch

        print("--> Finishing Time:",self.time)