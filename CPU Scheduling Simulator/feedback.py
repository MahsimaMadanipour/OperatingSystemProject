class Feedback():
    def __init__(self, process_num, processes_list, f_quantum_t, s_quantum_t, t_quantum_t):
        self.processes_number = process_num
        self.processes = processes_list
        self.f_quantum_time = f_quantum_t
        self.s_quantum_time = s_quantum_t
        self.t_quantum_time = t_quantum_t
        self.time = 0
        self.context_switch = 0

    def running_algorithm(self):
        service_times = [[process.name, process.service_time] for process in self.processes]

        first_queue = []
        second_queue = []
        third_queue = []

        while True:
            arrived_processes = [process for process in self.processes if process not in first_queue and process not in second_queue and process not in third_queue and process.arrival_time <= self.time and process.finish_time == 0]
            if len(arrived_processes):
                turn_process = arrived_processes[0]
                for a in arrived_processes:
                    if a.arrival_time < turn_process.arrival_time:
                        turn_process = a
                first_queue.append(turn_process)
                print("-> First Queue (Quantum = 1):")
                turn_process = first_queue[0]
                print("--> Running Process: {}".format(turn_process.name))
                if self.f_quantum_time < turn_process.service_time:
                    turn_process.service_time -= self.f_quantum_time
                    self.time += self.f_quantum_time + self.context_switch
                    second_queue.append(turn_process)
                else:
                    self.time += turn_process.service_time
                    turn_process.finish_time = self.time
                    for s in service_times:
                        if s[0] == turn_process.name:
                            turn_process.service_time = s[1]
                            break
                    turn_process.calculate_turnaround_time()
                    turn_process.calculate_wating_time()
                    print("{} Turnaround Time: {}".format(turn_process.name, turn_process.turnaround_time))
                    print("{} Waiting Time: {}".format(turn_process.name, turn_process.waiting_time))
                first_queue.remove(turn_process)
            elif len(second_queue) != 0 or len(third_queue) != 0:
                if len(second_queue):
                    print("-> Second Queue (Quantum = 4):")
                    turn_process = second_queue[0]
                    print("--> Running Process: {}".format(turn_process.name))
                    if self.s_quantum_time < turn_process.service_time:
                        turn_process.service_time -= self.s_quantum_time
                        self.time += self.s_quantum_time + self.context_switch
                        third_queue.append(turn_process)
                    else:
                        self.time += turn_process.service_time
                        turn_process.finish_time = self.time
                        for s in service_times:
                            if s[0] == turn_process.name:
                                turn_process.service_time = s[1]
                                break
                        turn_process.calculate_turnaround_time()
                        turn_process.calculate_wating_time()
                        print("{} Turnaround Time: {}".format(turn_process.name, turn_process.turnaround_time))
                        print("{} Waiting Time: {}".format(turn_process.name, turn_process.waiting_time))
                    second_queue.remove(turn_process)
                elif len(third_queue):
                    print("-> Third Queue (Quantum = 8):")
                    turn_process = third_queue[0]
                    print("--> Running Process: {}".format(turn_process.name))
                    if self.t_quantum_time < turn_process.service_time:
                        turn_process.service_time -= self.t_quantum_time
                        self.time += self.t_quantum_time + self.context_switch
                    else:
                        self.time += turn_process.service_time
                        turn_process.finish_time = self.time
                        for s in service_times:
                            if s[0] == turn_process.name:
                                turn_process.service_time = s[1]
                                break
                        turn_process.calculate_turnaround_time()
                        turn_process.calculate_wating_time()
                        print("{} Turnaround Time: {}".format(turn_process.name, turn_process.turnaround_time))
                        print("{} Waiting Time: {}".format(turn_process.name, turn_process.waiting_time))
                        third_queue.remove(turn_process)
            else:
                temp_processes = self.processes
                above_times = []
                for p in self.processes:
                    if self.time < p.arrival_time:
                        above_times.append(p.arrival_time)
                above_times = sorted(above_times)
                if len(above_times):
                    self.time = above_times[0]
                else:
                    break
        print("--> Finishing Time:",self.time)                                  