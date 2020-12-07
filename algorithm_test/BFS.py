
# -*- codeing = utf-8 -*-
#@Time :2020/12/6 15:49
#@Author :张士澜
#@File :BFS.py
#@Software :PyCharm

from collections import deque

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'
def search(name):
    search_queue = deque()      #创建一个队列
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+" is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")