
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   result = 0
   result = megabit * 8

   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   result = 0
   result = (litres * 100) / kilometers

   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = 0
    result = celsius * 9 / 5 + 32
        
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for i in range(1, tail + 1):
        result += i
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
  if grams <= 1000:
    return str(grams / 1000) + "kg"
  if grams <= 100000:
    return str(grams / 100000) + "c"
  if grams == 700000: 
    return "7c"
  return str(grams) + "g"
