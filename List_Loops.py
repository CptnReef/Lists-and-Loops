#Question 1 ----------------------------------------------------------------
songs = ["ROCKSTAR", "Do It", "For The Night"]

print("\n") #Question 2 ----------------------------------------------------
print(songs[0])
print(songs[2])
print(songs[1:3])

print("\n") #Question 3 ----------------------------------------------------
songs[2] = "Shake It Off!"
print(songs)

print("\n") #Question 4 ----------------------------------------------------
songs.append("Lasers")
print(songs)
songs.extend(["Hold On", "Fergalicious"])
print(songs)
del songs[5]
print(songs)

print("\n") #Question 6 ----------------------------------------------------
animals = ["Cat","Dog","Bird"]
print(animals)
animals.append("Fish")

print(animals[2])

del animals[0]
print(animals)

for anim in range(len(animals)):
    print(animals[anim])
