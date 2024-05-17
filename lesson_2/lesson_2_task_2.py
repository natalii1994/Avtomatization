def is_year_leap(year):
   year = int(year)
   if year % 4 == 0:
      print("год", year, ":", True)
   else:
      print("год", year, ":", False)

print(is_year_leap(input("Введите год: ")))
