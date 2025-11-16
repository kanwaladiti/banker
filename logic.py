def calculate_need(maximum, allocation):
    return [[maximum[i][j] - allocation[i][j] for j in range(len(maximum[0]))]
            for i in range(len(maximum))]

def is_safe_state(allocation, need, available):
    process_count = len(allocation)
    resource_count = len(available)
    work = available[:]
    finish = [False] * process_count
    safe_sequence = []

    while len(safe_sequence) < process_count:
        allocated = False
        for i in range(process_count):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(resource_count)):
                for j in range(resource_count):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                allocated = True
                break
        if not allocated:
            return False, []

    return True, safe_sequence
