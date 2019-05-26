class TwoSum():
    def __init__(self):
        self.num_dict = dict()

    def find(self, target: int):
        for num in self.num_dict:
            wanted_num = (target - num)
            if wanted_num == num and self.num_dict[wanted_num] < 2:
                continue
            if wanted_num in self.num_dict:
                return (num, wanted_num)
        return (-1, -1)
    
    def add(self, num):
        if num in self.num_dict:
            self.num_dict[num] += 1
        else:
            self.num_dict[num] = 1
        return self.num_dict