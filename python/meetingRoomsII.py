# given an array of meeting room intervals [start, end]

# find minimum no of conference rooms required

# input = [[0, 30], [5, 10], [15, 20]]


import heapq
input = [[0, 30], [5, 10], [15, 20]]

def meetingRooms(meetings):
  heap = []
  meetings.sort()
  heapq.heappush(heap, (meetings[0][1], meetings[0][0]))
  for i in range(1, len(meetings)):
    earliestEnd, earliestStart = heapq.heappop(heap)
    currentStart, currentEnd = meetings[i]
    if currentStart >= earliestEnd:
      earliestEnd = currentEnd
    else:
      heapq.heappush(heap, (currentEnd, currentStart))
    heapq.heappush(heap, (earliestEnd, earliestStart))
  return len(heap)


print(meetingRooms(input))  
