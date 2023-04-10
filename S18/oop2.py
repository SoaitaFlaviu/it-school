class Employee:
    
    def __init__(self, first_name, last_name, email, gross_salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gross_salary = gross_salary
        self.__ssm_signes = False

    def sign_ssm(self):
        self.__ssm_signed = True

    def sign_presence(self):
        pass

    def get_net_salary(self):
        return self.__gross_salary

    def pay(self):
        print(f"Amount to transfer": {self.get_net_salary()}"
              f"{self.__last_name}:{self.get_net_salary() RON"})

class FullTimeEmployee(Employee):
    pass

class Contractor(Employee):
    pass

class NoTaxEmployee(Employee):
    pass

class PartTimeEmployee(Employee):
    pass


employes = [FullTimeEmployee("Ionut", "Sergiu", "test@tes.com", 3000),
           Contractor("Ionut", "Zmeu", "test@tes.com", 6000),
           PartTimeEmployee("Alex", "Grigore", "test@tes.com", 5000),
           NoTaxEmployee("Ionut", "Sergiu", "test@tes.com", 4000) ]
