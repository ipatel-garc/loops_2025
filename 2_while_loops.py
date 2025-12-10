# Given:
colors = ["red", "blue", "green", "yellow", "purple"]
print(len(colors))
# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
index=0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index+=1

#start with index 0 (first color)
#while index is less than length of colors (5)
# cherck if color at current index is yellow