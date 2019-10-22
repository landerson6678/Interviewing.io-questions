#Given list of meetings, return the maximum amount of meetings that you can attend while filling up the most hours
#https://www.youtube.com/watch?v=Q5_2BCej9hg&t=2525s


#Extra: I added the ability to print out muliple calendars if there different options that take up the same time and space
import heapq

def meeting_optimization(meetings,hours):
    map = [(hours,meetings)]
    best = [map[0]]
    while len(map):
        current = heapq.heappop(map)
        if current[0] == 0:
            if len(current[1]) < len(best[0][1]):
                best = [current]
            elif current[1] not in [x[1] for x in best]:
                best.append(current)
        for meeting in current[1]:
            if meeting[1] <= current[0]:
                heapq.heappush(map,(current[0] - meeting[1],[x for x in current[1] if x != meeting]))
    return [[x for x in meetings if x not in y[1]] for y in best]

meetings = [('Call',3),('Lunch',1),('Happy Hour',1.5),('Test',5),('Dinner',3)]
print(meeting_optimization(meetings,9),'\n')
print(meeting_optimization(meetings,8))
