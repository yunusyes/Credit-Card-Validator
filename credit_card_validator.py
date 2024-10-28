class credit_card_validator:
    
    def __init__(self):
        self.list_modified_num = None
        self.sum_odd_digits = 0  
        self.even_doubled_nums = []
        self.even_doubled_nums_two_digits = []
        self.sum_even_doubled_nums_two_digits = []       
        self.sum_even_digits = 0
        self.sum = 0

    def validation(self):
        num = input("Enter a credit card #: ")
        no_spaces = num.replace(" ", "") 
        modified_num = no_spaces.replace("-", "")     
        self.list_modified_num = list(modified_num)
       
    def sum_of_odd_digits(self):
        index_odd = 0
        for i in self.list_modified_num:
            if index_odd % 2 != 0:    
                self.sum_odd_digits += int(i)
            index_odd += 1
        
    def double_even_digits(self):
        total_even = 0
        index_even = 0
        for i in self.list_modified_num:
            if index_even % 2 == 0:
                total_even = int(i)*2
                self.even_doubled_nums.append(total_even)
            index_even += 1
        
    def sum_of_even_two_digits(self):
        index_even_doubled_nums = 0
        for i in self.even_doubled_nums:
            if i > 9:
                self.even_doubled_nums_two_digits.append(i)
                index_even_doubled_nums += 1
            else:
                index_even_doubled_nums += 1    
        for number in self.even_doubled_nums_two_digits:
            digit_sum = 0
            for digit in str(number):
                digit_sum += int(digit)
            self.sum_even_doubled_nums_two_digits.append(digit_sum)
        
    def sum_of_even_digits(self):
        for i in self.sum_even_doubled_nums_two_digits:
            self.sum_even_digits += i
        for i in self.even_doubled_nums:
            if i < 9:
                self.sum_even_digits += i
    
    def sum_of_even_odd_nums(self):
        self.sum = self.sum_odd_digits + self.sum_even_digits
        
    def sum_validation_check(self):
        if self.sum % 10 == 0:
            print("VALID")
        elif self.sum % 10 != 0:
            print("INVALID")
                             
def main():
    cr = credit_card_validator()
    cr.validation()
    cr.sum_of_odd_digits()
    cr.double_even_digits()
    cr.sum_of_even_two_digits()
    cr.sum_of_even_digits()
    cr.sum_of_even_odd_nums()
    cr.sum_validation_check()

if __name__ == "__main__":
    main()