import heapq
class TimeMap:

    def __init__(self):
        self.mem = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mem:
            heapq.heappush(self.mem[key], (timestamp, value))
            heapq._heapify_max(self.mem[key])
        else:
            self.mem[key] = [(timestamp, value)]
            #q = heapq._heapify_max()
            heapq._heapify_max(self.mem[key])
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mem:
            item = None
            lst = []
            while self.mem[key]:
                temp = heapq._heappop_max(self.mem[key])
                if temp[0] <= timestamp:
                    item = temp
                    lst.append(temp)
                    break
                lst.append(temp)
                #heapq.heappush(self.mem[key],item)
                
            self.mem[key] = lst
            heapq._heapify_max(self.mem[key])
            return item[1] if item else ''
        return ''