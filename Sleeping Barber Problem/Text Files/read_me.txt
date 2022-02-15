Project #2: Sleeping Barber Problem

Project’s Objectives:
    There is a barber shop which has one barber, one barber chair, and n chairs for waiting for
    customers if there are any to sit on the chair.
        If there is no customer, then the barber sleeps in his own chair.
        When a customer arrives, he has to wake up the barber.
        If there are many customers and the barber is cutting a customer’s hair, then the remaining
          customers either wait if there are empty chairs in the waiting room or they leave if no chairs 
          are empty.
    The problem is to program the barber and the customers without getting into race conditions.

Project’s Description:
    When the barber shows up in the morning, he executes the procedure “barber”. Then the
    barber goes to sleep until the first customer comes up.
    When a customer arrives, he executes the procedure “customer”, if another customer enters
    thereafter, the second one will not be able to anything until the first one has left. The customer
    then checks the chairs in the waiting room if waiting customers are less than the number of
    chairs then he sits otherwise he leaves.
    If the barber chair is available then customer wakes up the barber if he is sleeping and sits on
    the chair. At this point, customer and barber are both awake and the barber is ready to give
    that person a haircut. When the haircut is over, the customer exits the procedure and if there
    are no customers in waiting room barber sleeps.

Design Hints:
    Use semaphores or monitors to solve this problem

Inputs:
    Number of waiting chairs
    Arrival time of each customer
    How long the haircut of each costumer takes

Outputs:
    Design a program that supports mutual exclusion and solves the problem of deadlock andstarvation
    Waiting time of each costumer