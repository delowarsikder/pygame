from Vector2Class import Vector2

A = Vector2(10.0, 20.0)
B = Vector2(30.0, 35.0)
AB = Vector2.from_points(A, B)
print("Vector AB is :", AB)
print("AB * 2 is :", AB * 2)
print("AB / 2 is :", AB / 2)

# print("AB + (–10, 5) is", AB + (–10, 5))
# print ("Magnitude of AB is", AB.get_magnitude())
# print ("AB normalized is", AB.get_normalized())
