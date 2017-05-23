import math

def main():
	r = float(input("Enter radius:"))
	print "The area is: " + str(area(r))
	print "The circumference is: " + str(circ(r))
	
def area(radius):
	return math.pi * radius * radius

def circ(radius):
	return math.pi * radius * 2

if __name__ == "__main__":
	main()