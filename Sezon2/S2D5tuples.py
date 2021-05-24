welcome = "Welcome to my Nightmare","Alice Cooper",1975
bad = "Bad Comapny", "Bad Company", 1974
budgie = "Nightflight","Budgie", 1981
imelda = "More Mayhem","Emilda May", 2011
metallica = "Ride the Lightning", "Metallica",1984

print(metallica[0])
print(metallica[1])
print(metallica[2])

#metallica[0] = "Master of Puppets"
#TypeError: 'tuple' object does not support item assignment
metallica2=list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)


