def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be greater than zero.")

    return weight / (height ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


if __name__ == "__main__":
    weight = 60
    height = 1.65

    bmi = calculate_bmi(weight, height)

    print(f"BMI: {bmi:.2f}")
    print(f"Category: {get_bmi_category(bmi)}")