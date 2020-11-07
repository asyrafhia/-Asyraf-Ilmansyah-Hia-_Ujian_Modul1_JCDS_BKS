#Pagination helper class

from math import ceil
class PaginationHelper:
    def __init__(self, list, page):
        self.book = list
        self.page = page
        self.page_count =  ceil(len(self.book)/self.page)
        self.item_count = len(self.book)
        self.book_list = []
        self.page_dict = {}
        #membuat list dalam list
        for i in range(self.page_count):
            temp = []
            if i == self.page_count - 1:
                if self.item_count % self.page > 0:
                    for j in range(self.item_count % self.page):
                        temp.append(self.book[j + i*self.page])
                else:
                    for l in range(self.page):
                        temp.append(self.book[l + i*self.page])      
            else:    
                for k in range(self.page):
                    temp.append(self.book[k + i*self.page])
            self.book_list.append(temp)
        

        for idx, val in enumerate(self.book_list):
            for idx1 in range(len(val)):
                self.page_dict[idx1 + (self.page * idx )] = idx

        #{key:value} = {index dari item: index dari page}    


    def page_item_count(self, num):
        try:    
            print(len(self.book_list[num]))
        except:
            print(-1)
            
    def page_index(self, num):
        if num > self.item_count or num < 0:
            print(-1)        
        else:
            print(self.page_dict[num])


helper = PaginationHelper('a b c d e f g h'.split(), 4)   
print(helper.page_count)
print(helper.item_count)  
helper.page_item_count(0)
helper.page_item_count(1)
helper.page_item_count(3)  
# helper.page_index(7)    
# helper.page_index(2)
# helper.page_index(20)               
# helper.page_index(-10)    