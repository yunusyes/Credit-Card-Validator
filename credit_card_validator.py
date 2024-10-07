class credit_card_validator:
    
    def __init__(self):
        self.list_modified_num = None

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
        even_doubled_nums = []
        even_doubled_nums_two_digits = []
        sum_digits = []
        index_even_doubled_nums = 0
        for i in self.list_modified_num:
            if index_even % 2 == 0:
                total_even = int(i)*2
                even_doubled_nums.append(total_even)
            index_even += 1
        print(even_doubled_nums)
        ##
        for i in even_doubled_nums:
            if i > 9:
                even_doubled_nums_two_digits.append(i)
                index_even_doubled_nums += 1
            else:
                index_even_doubled_nums += 1
        print(even_doubled_nums_two_digits)
        
    def sum_even_two_digits():
        pass
        
                  
def main():
    cr = credit_card_validator()
    cr.validation()
    cr.sum_odd_digits()
    cr.double_even_digits()

if __name__ == "__main__":
    main()