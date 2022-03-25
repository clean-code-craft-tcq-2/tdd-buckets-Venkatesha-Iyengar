def check_not_same_numbers(num1,num2): 
    return bool((num1-num2))

def check_not_continuous_numbers(num1,num2):
    return bool((num2-num1)-1)

class Group_Number_Range:
    def __init__(self):
        self.continuous_range_not_started = True
        self.continuous_range_counter = 1
        self.range_first_value = 0
        self.range_last_value = 0
        self.result = dict()

    def iterate_numbers(self,number_list):
        number_list.sort()
        self.continuous_range_not_started = True
        self.result = dict()
        for i in range(len(number_list)-1):
            check_not_same = check_not_same_numbers(number_list[i],number_list[i+1])
            check_not_continuous = check_not_continuous_numbers(number_list[i],number_list[i+1])
            result_continuous_or_same = not (check_not_same & check_not_continuous)
            self.infer_result(result_continuous_or_same, number_list[i], number_list[i+1])
        self.last_range_details()
        return self.result

    def infer_result(self, result, num1, num2):
        if (result):
            self.continuous_range_inference(num1, num2)
            return
        self.new_range_inference(num1, num2)
        return
    
    def continuous_range_inference(self, num1,num2):
        if (self.continuous_range_not_started):
            self.continuous_range_not_started = False
            self.range_first_value = num1
            self.continuous_range_counter+=1
            self.range_last_value = num2
            return
        self.continuous_range_counter+=1
        self.range_last_value = num2
        return

    def new_range_inference(self, num1,num2):
        self.last_range_details()
        self.continuous_range_not_started = True
        

    def last_range_details(self):
        if self.continuous_range_counter>1:
            self.result[f'{self.range_first_value}-{self.range_last_value}'] = self.continuous_range_counter
            self.print_last_range_details(f'{self.range_first_value}-{self.range_last_value}, {self.continuous_range_counter}')
        self.continuous_range_counter = 1
        self.range_first_value = 0
        self.range_last_value = 0

    def print_last_range_details(self, print_statement):
        print(print_statement)
        return True


