class WashingQueue:
    def __init__(self, station_capacity):
        self.station = [None] * station_capacity
        self.front = -1
        self.rear = -1
        self.station_capacity = station_capacity

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.station_capacity == self.front

    def enqueue(self, car):
        if self.is_full():
            print("Car Stations are occupied")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.station_capacity
        self.station[self.rear] = car
        print(f"Car {car} sent for Washing")

    def dequeue(self):
        if self.is_empty():
            print("Waiting Hall is Empty")
            return -1
        dequeued_car = self.station[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.station_capacity
        return dequeued_car


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CallLog:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, car):
        new_node = Node(car)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue.")
            return -1
        dequeued_car = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_car

    def display(self):
        if self.is_empty():
            print("\nWaiting List is Empty.")
            return
        print("\nCars in the waiting list:")
        current = self.front
        while current:
            print(current.data)
            current = current.next


# Helper functions to check if a car is already in a queue or station
def car_in_washing(stations, car):
    index = stations.front
    while index != stations.rear:
        if stations.station[index] == car:
            return True
        index = (index + 1) % stations.station_capacity
    return stations.station[stations.rear] == car

def car_in_log(log, car):
    current = log.front
    while current:
        if current.data == car:
            return True
        current = current.next
    return False


# Main function
if __name__ == "__main__":
    size = int(input("Enter the number of stations: "))
    stations = WashingQueue(size)
    call_log = CallLog()

    while True:
        print("\n--------------------------------------------------------")
        print("1. New Car To The Station")
        print("2. Complete Wash And Invite Next Car")
        print("3. Next Car Data")
        print("4. Call Log Data")
        print("PRESS ANY OTHER KEY TO EXIT")

        try:
            decision = int(input("Choose Option To Perform: "))
        except ValueError:
            break

        if decision == 1:
            car = int(input("\nEnter Car Data (In Numbers): "))
            if car_in_washing(stations, car) or car_in_log(call_log, car):
                print(f"Car {car} is already in the station")
            else:
                if stations.is_full():
                    print(f"Car {car} added to waiting list")
                    call_log.enqueue(car)
                else:
                    stations.enqueue(car)

        elif decision == 2:
            if stations.is_empty():
                print("\nNo Cars in the station.")
                continue
            completed_car = stations.dequeue()
            print(f"\nCar {completed_car} Completed Washing")
            if call_log.is_empty():
                print("No Cars in the waiting list")
            else:
                stations.enqueue(call_log.dequeue())

        elif decision == 3:
            if call_log.is_empty():
                print("\nWaiting List is Empty.")
            else:
                print(f"\nCar {call_log.front.data} - Next in Line for Washing.")

        elif decision == 4:
            call_log.display()

        else:
            break
