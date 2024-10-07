class credit_card_validator:
    
    def __init__(self):
        self.list_modified_num = None
        self.even_doubled_nums = []
        self.even_doubled_nums_two_digits = []
        self.index_even_doubled_nums = 0
        self.sum_even_doubled_nums_two_digits = []

    def validation(self):
        self.num = input("Enter a credit card #: ")
        no_spaces = self.num.replace(" ", "") 
        modified_num = no_spaces.replace("-", "")     
        self.list_modified_num = list(modified_num)
       
    def sum_odd_digits(self):
        total_odd = 0
        index_odd = 0
        for i in self.list_modified_num:
            if index_odd % 2 != 0:    
                total_odd += int(i)
            index_odd += 1
        print(total_odd)
        
    def double_even_digits(self):
        total_even = 0
        index_even = 0
        sum_even_digits = 0
        sum_digits = []
        for i in self.list_modified_num:
            if index_even % 2 == 0:
                total_even = int(i)*2
                self.even_doubled_nums.append(total_even)
            index_even += 1
        print(self.even_doubled_nums)
        
    def sum_even_two_digits(self):
        for i in self.even_doubled_nums:
            if i > 9:
                self.even_doubled_nums_two_digits.append(i)
                self.index_even_doubled_nums += 1
            else:
                self.index_even_doubled_nums += 1
        print(self.even_doubled_nums_two_digits)      
        for number in self.even_doubled_nums_two_digits:
            digit_sum = 0
            for digit in str(number):
                digit_sum += int(digit)
            self.sum_even_doubled_nums_two_digits.append(digit_sum)
        print(self.sum_even_doubled_nums_two_digits)
                  
def main():
    cr = credit_card_validator()
    cr.validation()
    cr.sum_odd_digits()
    cr.double_even_digits()
    cr.sum_even_two_digits()

if __name__ == "__main__":
    main()