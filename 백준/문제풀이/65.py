#####################
# 다리 만들기 
# 골드 1
# 백준 17472
# 23.9.26
#####################

import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

dr = [1,0,-1,0] #행 방향으로의 탐색
dc = [0,1,0,-1] #열 방향으로의 탐색

N,M = map(int,input().split())
myMap = [[[0] * (N)] for i in range(N)]
visited = [[[False] * (N)] for i in range(N)]

#지도 정보 저장 - input
for i in range(N):
    myMap[i] = list(map(int,input().split()))

sNum = 1 #1번부터 시작해서 하나씩 증가시키기
sumlist = []
mlist = []

def addNode(i,j,queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i,j]
    mlist.append(temp)
    q.append(temp)

def BFS(i,j):
    queue = deque()
    mlist.clear()
    start = [i,j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum




            


    



