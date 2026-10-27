def convert_celsius_to_farenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

farenheit = convert_celsius_to_farenheit(20.0)

print(f"20.0°C = {farenheit}°F")