
kills = input("How many kills did you get?: ")
assists = input("How many assists did you get?: ")
deaths = input("How many times did you die?: ")

kd_ratio = (float(kills) + float(assists)) / float(deaths)

print("Your K/D ratio is: " + str(kd_ratio) + "!")