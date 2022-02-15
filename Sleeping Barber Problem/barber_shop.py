"""
Project #2: Sleeping Barber Problem

There is a barber shop which has one barber, one barber chair, and n chairs for waiting for customers if there are any to sit on the chair.
- If there is no customer, then the barber sleeps in his own chair.
- When a customer arrives, he has to wake up the barber.
- If there are many customers and the barber is cutting a customer's hair, then the remaining customers either wait if there are empty chairs in the waiting room or they leave if no chairs are empty.
The problem is to program the barber and the customers without getting into race conditions.
"""

from costumer import Costumer

def semaphore_wait(semaphore, the_queue, the_queue_length, p):
    if semaphore == 1:
            semaphore = 0
            return semaphore
    else:
        if len(the_queue) < the_queue_length:
            the_queue.append(p)
            print("Costumer {} is on Waiting Chairs!".format(p.name))
        else:
            print("There Is No Empty Chair, Costumer {} Left :(.".format(p.name))
    return semaphore

def semaphore_signal(semaphore, the_queue):
    if len(the_queue) == 0:
            semaphore = 1
            return semaphore
    else:
        p = the_queue[0]
        the_queue.remove(p)
        return p

def semaphore_sleep():
    print("The Barber Slept!")
    return 0

def semaphore_wakeup():
    print("The Barber is Awake!")
    return 1

with open('Sleeping Barber Problem/Text Files/input_costumers.txt') as input_file:
    raw_lines = input_file.readlines()

chairs_number = int(raw_lines[0][:-1])
raw_lines.remove(raw_lines[0])
costumers = []
for line in raw_lines:
    c_name, c_arrival_time, c_service_time = line[:-1].split(", ")
    costumers.append(Costumer(c_name, int(c_arrival_time), int(c_service_time)))

chair_semaphore = 0
turn_costumer = None
waiting_queue = []
time = 0
barber_on = False

print("Morning! The Barber Enters The Barber Shop")
chair_semaphore = semaphore_sleep()
barber_on = True

while len(costumers) or len(waiting_queue):
    if len(costumers):
        arrival_times = [c.arrival_time for c in costumers]
        if min(arrival_times) > time:
            chair_semaphore = semaphore_sleep()
            barber_on = True
            time = min(arrival_times)
        arrived_costumer = sorted([[costumer, costumer.arrival_time] for costumer in costumers if costumer.arrival_time <= time], key = lambda x: x[1])
        turn_costumers = [t_costumer[0] for t_costumer in arrived_costumer]
        if len(turn_costumers):
            turn_costumer = turn_costumers[0]
            costumers.remove(turn_costumer)
            turn_costumers.remove(turn_costumer)
        if barber_on:
            chair_semaphore = semaphore_wakeup()
            barber_on = False
        if chair_semaphore and not(barber_on):
            chair_semaphore = semaphore_wait(chair_semaphore, waiting_queue, chairs_number, turn_costumer)
            if len(waiting_queue):
                chair_semaphore = semaphore_wait(chair_semaphore, waiting_queue, chairs_number, turn_costumer)
                turn_costumer = semaphore_signal(chair_semaphore, waiting_queue)
            print("Time is {} and Costumer {} is On Chair.".format(time, turn_costumer.name))
            turn_costumer.waiting_time = time - turn_costumer.arrival_time
            time += turn_costumer.service_time
            print("--> Costumer {} is Leaving, Waiting Time: {}".format(turn_costumer.name, turn_costumer.waiting_time))  
        for t in turn_costumers:
            chair_semaphore = semaphore_wait(chair_semaphore, waiting_queue, chairs_number, t)
            costumers.remove(t)
        turn_costumers = turn_costumers.clear()
    else:
        turn_costumer = semaphore_signal(chair_semaphore, waiting_queue)
        if barber_on:
            chair_semaphore = semaphore_wakeup()
            barber_on = False
        if chair_semaphore and not(barber_on):
            chair_semaphore = semaphore_wait(chair_semaphore, waiting_queue, chairs_number, turn_costumer)
            print("Time is {} and Costumer {} is On Chair.".format(time, turn_costumer.name))
            turn_costumer.waiting_time = time - turn_costumer.arrival_time
            time += turn_costumer.service_time
            print("--> Costumer {} is Leaving, Waiting Time: {}".format(turn_costumer.name, turn_costumer.waiting_time))

chair_semaphore = semaphore_sleep()
barber_on = False