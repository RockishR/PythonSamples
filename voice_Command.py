class VoiceCommand:
    def __init__(self,li):
        self.l = li
        self.curr = 0

    def first_channel(self):
        self.curr = 0
        return self.l[self.curr]
    def last_channel(self):
        self.curr = len(self.l)-1
        return self.l[self.curr]
    def turn_channel(self,ch):
        self.curr = ch-1
        print("###***   :: ",self.l[self.curr],ch,self.curr )
        return self.l[self.curr]
    def next_channel(self):
        if self.curr == len(self.l)-1:
            self.curr = 0
        else:
            self.curr += 1
        return self.l[self.curr]
    def previous_channel(self):
        print('------------',self.curr)
        if self.curr == 0:
            self.curr = len(self.l)-1
        else:
            self.curr -= 1
        print('------------',self.curr)
        return self.l[self.curr]
    def current_channel(self):
        return self.l[self.curr]
    def is_exist(self,obj):
        if isinstance(obj,int):
            if obj in range(1,len(self.l)):
                return 'Yes'
            else:
                return 'No'
        else:
            if obj in self.l:
                return 'Yes'
            else:
                return 'No'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    print("###### curr:: ",controller.last_channel())
    print("###### curr:: ",controller.previous_channel())
    print("###### curr:: ",controller.current_channel())

    # assert controller.first_channel() == "BBC"
    # assert controller.last_channel() == "TV1000"
    # assert controller.turn_channel(1) == "BBC"
    # print("###### curr:: ",controller.current_channel())
    # assert controller.next_channel() == "Discovery"
    # assert controller.previous_channel() == "BBC"
    # assert controller.current_channel() == "BBC"
    # assert controller.is_exist(4) == "No"
    # assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")