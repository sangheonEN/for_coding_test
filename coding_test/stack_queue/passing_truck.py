from collections import deque


def solution(bridge_length, weight, truck_weights):
    passing_truck = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)

    time = 0
    sum_weight = 0

    while len(passing_truck):
        time += 1
        # constrain
        # 1. weight <= truck_weights[i] pass
        # 2. bridge_length len(truck_stay)

        passing_truck.popleft()
        if passing_truck:
            sum_weight -= passing_truck[0]

        if truck_weights:
            if sum_weight <= weight:
                passing_truck.append(truck_weights.popleft())
                if truck_weights:
                    sum_weight += truck_weights[0]

            else:
                passing_truck.append(0)

    return time


print(solution(2, 10, [7,4,5,6]))
