tension = 230  # V
max_power = 25 * tension  # W
number_of_bulbs = 5  # db
tension_of_bulbs = 30  # W
tension_of_aircon = 1500  # W
tension_of_washing_m = 1200  # W
tension_of_iron = 2000  # W

all_tension = number_of_bulbs * tension_of_bulbs + tension_of_aircon + tension_of_washing_m
power_w_iron = all_tension + tension_of_iron
print("Összes feszültség", all_tension, "W")
print("Teljesítmény", max_power, "W")
print("Lekapcsol-e a megszakító:", power_w_iron > max_power )




