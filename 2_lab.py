import numpy as np

data = {
    "Акції": {
        "імовірності": [0.6, 0.4],
        "прибуток": [500, 300]
    },
    "Облігації": {
        "імовірності": [0.9, 0.1],
        "прибуток": [440, 120]
    }
}

def calculate_risk(probabilities, profits):

    expected_value = np.dot(probabilities, profits)

    variance = np.dot(probabilities, (np.array(profits) - expected_value) ** 2)

    coefficient_of_variation = np.sqrt(variance) / expected_value
    
    return expected_value, variance, coefficient_of_variation

results = {}
for option, values in data.items():
    expected_value, variance, coef_var = calculate_risk(values["імовірності"], values["прибуток"])
    results[option] = {
        "Сподіване значення": expected_value,
        "Варіація": variance,
        "Коефіцієнт варіації": coef_var
    }

for option, result in results.items():
    print(f"{option}:")
    print(f"  Сподіване значення: {result['Сподіване значення']:.2f} тис. дол.")
    print(f"  Варіація: {result['Варіація']:.2f}")
    print(f"  Коефіцієнт варіації: {result['Коефіцієнт варіації']:.2f}\n")

if results["Акції"]["Коефіцієнт варіації"] < results["Облігації"]["Коефіцієнт варіації"]:
    print("Менш ризиковане рішення: Вкладення в акції.")
else:
    print("Менш ризиковане рішення: Вкладення в облігації.")
