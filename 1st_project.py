print("Welcome to the flood predictor!")
print("The flood chances depend on factors like terrain, drainage systems, and soil absorption!")
rainfall=int(input("Tell me the rainfall(in mm) in your area!"))
if rainfall<10:
    print("No risk[0%-5% Chances---No need to worry.]")
elif rainfall>=10 and rainfall<30:
    print("Low risk[5%-15% Chances---Minor water pooling in low lying areas.]")
elif rainfall>=30 and rainfall<50:
    print("Moderate risk[15%-30% Chances---Water may accumulate on roads,affecting traffic.]")
elif rainfall>=50 and rainfall<100:
    print("High risk[30%-60% Chances---Streets and underpaases may start flooding,drains may overflow.]")
elif rainfall>=100 and rainfall<150:
    print("Very high risk[60%-85% Chances---Significant water logging in urban areas,possible evacuation alerts.]")
elif rainfall>=150 and rainfall<200:
    print("Severe risk[85%-95% Chances---Flash floods likely,rivers may overflow,and homes in low line areas at risk.]")
elif rainfall>=200:
    print("Extreme risk[95%-100% Chances---widespread flooding,possible landslides,mass evacuation required.]")
else:
    print("Enter an integer only")
print("This is a general estimation and can vary based on local geography and drainage capacity.")
