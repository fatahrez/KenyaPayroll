from django.shortcuts import render


# Create your views here.
class EmployeePayroll:
    basicSalary = 0
    gross_salary = 0
    taxable_income = 0
    nssf_deduction = 0
    nhif_deduction = 0
    payee = 0
    personal_relief = 0
    total_tax = 0
    net_salary = 0

    def __init__(self, basic_salary):
        self.basicSalary = basic_salary
        self.calculate_gross_salary()
        self.calculate_nssf()
        self.calculate_nhif()
        self.calculate_taxable_income()
        self.calculate_payee()
        self.calculate_tax_payable()
        self.calculate_net_salary()

    def calculate_gross_salary(self):
        gross_salary = self.basicSalary
        self.gross_salary = gross_salary

        return gross_salary

    def calculate_nssf(self):
        if 0 < self.gross_salary <= 6000:
            nssf = 0.06 * self.gross_salary
            self.nssf_deduction = nssf
            return nssf
        elif 6000 < self.gross_salary < 18000:
            remainder = self.gross_salary - 6000
            nssf = 6000 * 0.06 + remainder * 0.06
            self.nssf_deduction = nssf
            return nssf
        elif self.gross_salary > 18000:
            nssf = 6000 * 0.06 + 12000 * 0.06
            self.nssf_deduction = nssf
            return nssf

    def calculate_nhif(self):
        if 0 <= self.gross_salary <= 5999:  # 0 - 5999
            nhif = 150
            self.nhif_deduction = nhif
            return nhif
        elif 6000 <= self.gross_salary <= 7999:  # 6000 - 7999
            nhif = 300
            self.nhif_deduction = nhif
            return nhif
        elif 8000 <= self.gross_salary <= 11999:
            nhif = 400
            self.nhif_deduction = nhif
            return nhif
        elif 12000 <= self.gross_salary <= 14999:  # 12000 - 14999
            nhif = 500
            self.nhif_deduction = nhif
            return nhif
        elif 15000 <= self.gross_salary < 19999:  # 15000 - 19999
            nhif = 600
            self.nhif_deduction = nhif
            return nhif
        elif 20000 <= self.gross_salary <= 24999:
            nhif = 750
            self.nhif_deduction = nhif
            return nhif
        elif 25000 <= self.gross_salary <= 29999:
            nhif = 850
            self.nhif_deduction = nhif
            return nhif
        elif 30000 <= self.gross_salary <= 34999:
            nhif = 900
            self.nhif_deduction = nhif
            return nhif
        elif 35000 <= self.gross_salary <= 39999:
            nhif = 950
            self.nhif_deduction = nhif
            return nhif
        elif 40000 <= self.gross_salary <= 44999:
            nhif = 1000
            self.nhif_deduction = nhif
            return nhif
        elif 45000 <= self.gross_salary <= 49999:
            nhif = 1100
            self.nhif_deduction = nhif
            return nhif
        elif 50000 <= self.gross_salary <= 59999:
            nhif = 1200
            self.nhif_deduction = nhif
            return nhif
        elif 60000 <= self.gross_salary <= 69999:
            nhif = 1300
            self.nhif_deduction = nhif
            return nhif
        elif 70000 <= self.gross_salary <= 79999:
            nhif = 1400
            self.nhif_deduction = nhif
            return nhif
        elif 80000 <= self.gross_salary <= 89999:
            nhif = 1500
            self.nhif_deduction = nhif
            return nhif
        elif 90000 <= self.gross_salary <= 99999:
            nhif = 1600
            self.nhif_deduction = nhif
            return nhif
        elif self.gross_salary >= 100000:
            nhif = 1700
            self.nhif_deduction = nhif
            return nhif

    def calculate_taxable_income(self):
        nti = self.gross_salary - self.nssf_deduction
        self.taxable_income = nti
        return nti

    def calculate_payee(self):
        tier1 = 12298
        tier2 = 11587
        tier3 = 11587
        tier4 = 11587

        if self.taxable_income <= 12298:
            tax = self.taxable_income * 0.1
            self.payee = tax
            return tax
        elif 12299 <= self.taxable_income <= 23885:
            remainder = self.taxable_income - 12298
            tax = tier1 * 0.1 + 0.15 * remainder
            self.payee = tax
            return tax
        elif 23886 <= self.taxable_income <= 35472:
            remainder = self.taxable_income - tier1 - tier2
            tax = (tier1 * 0.1) + (tier2 * 0.15) + (0.2 * remainder)
            self.payee = tax
            return tax
        elif 35473 <= self.taxable_income <= 47059:
            remainder = self.taxable_income - tier1 - tier2 - tier3
            tax = (tier1 * 0.1) + (tier2 * 0.15) + (tier3 * 0.2) + (0.25 * remainder)
            self.payee = tax
            return tax
        elif self.taxable_income >= 47059:
            remainder = self.taxable_income - tier1 - tier2 - tier3 - tier4
            tax = (tier1 * 0.1) + (tier2 * 0.15) + (tier3 * 0.2) + (0.25 * tier4) + (0.3 * remainder)
            self.payee = tax
            return tax

    def calculate_net_salary(self):
        pass
