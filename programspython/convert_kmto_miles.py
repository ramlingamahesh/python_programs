
#1km = 1000 meters.

# 1 mile =  1760 yards

'''
Conversion formula:

                            1 kilometer is equal to 0.62137 miles.

                            Miles = kilometer * 0.62137

                            Kilometer = Miles / 0.62137   '''

# Collect input from the user
kilometers = float(input('How many kilometers?: '))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))

