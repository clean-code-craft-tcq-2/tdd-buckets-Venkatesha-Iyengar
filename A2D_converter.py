class A2D_Conerter:
    def __init__(self, no_bits, flag_signed = False):
        self.number_of_bits = no_bits
        self.flag_is_signed = flag_signed
        self.max_possible_digital_value = self.get_maximum_value()

    def get_maximum_value(self):
        return pow(2,self.number_of_bits)-1

    def get_absolute_range(self, list_digital_values, max_current_in_amps):
        self.max_possible_current = max_current_in_amps
        
        list_valid_digital_values = self.get_valid_range(list_digital_values)
        print(list_valid_digital_values)
        list_absolute_current_values = [self.get_absolute_current_value(digital_value) for digital_value in list_valid_digital_values]
        return list_absolute_current_values

    def get_valid_range(self, list_digital_values):
        return [value for value in list_digital_values if abs(value)<self.max_possible_digital_value]

    def get_absolute_current_value(self, digital_value):
        if self.flag_is_signed:
            return (abs(round((self.max_possible_current/(self.max_possible_digital_value/2))*(digital_value-self.max_possible_digital_value/2))))
        return (abs(round((self.max_possible_current/self.max_possible_digital_value)*digital_value)))
        
