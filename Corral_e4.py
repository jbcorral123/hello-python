import geometry

userinput= input("Enter the side lengths of a triangle: ")
inputs= userinput.split(",")

(a, b, c)= (float(num) for num in inputs)

P = geometry.triangle_perimeter(a, b, c)
A = geometry.triangle_heronsarea(a, b, c)

print("Perimeter: {:.4f}".format(P))
print("Area: {:.4f}".format(A))