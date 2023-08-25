# problem statements
class IncrementCalculator:
    def calculate_incremented_salary(self, salary, appraisal_rating):
        if 1 <= appraisal_rating <= 3:
            increment_percentage = 0.10
        elif 3 < appraisal_rating <= 3.5:
            increment_percentage = 0.25
        elif 3.5 < appraisal_rating <= 5:
            increment_percentage = 0.30
        else:
            increment_percentage = 0.0
        
        increment_amount = salary * increment_percentage
        return salary + increment_amount


if __name__ == "__main__":
    calculator = IncrementCalculator()
    
    employee_salary = float(input("Enter employee's current salary: "))
    appraisal_rating = float(input("Enter appraisal rating: "))

    incremented_salary = calculator.calculate_incremented_salary(employee_salary, appraisal_rating)
    print(f"Incremented Salary: ${incremented_salary:.2f}")
