lead_volume = 18
copper_volume = 23  # cm^3
lead_density = 11.34  # g/cm^3
copper_density = 8.69  # g/cm^3
lead_mass = lead_volume * lead_density
copper_mass = copper_volume * copper_density
print("Az ólom nehezebb:", lead_mass > copper_mass)
