#https://www.youtube.com/watch?v=ahIpip2DQ70
#Given a list of points, vertex, and k, return the k closest points to the vertex
import math
import heapq

def manhattan(item1,item2):
    return math.pow(item1[0] - item2[0],2) + math.pow(item1[1] - item2[1],2)

def k_closest(array,vertex,k):
    heap = []
    if k < 1: return heap
    for item in array:
        heapq.heappush(heap,(manhattan(item,vertex),item))
    return [item[1] for item in heap[0:k]]



print(k_closest([(1,2),(2,3),(3,3),(4,4),(1,1)],(1,1),0))
