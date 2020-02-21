def kinetic_energy(mass, velocity):
	ke = .5 * mass * (velocity ** 2)
	return ke

def main(count):
	for x in range(count):
		mass = float(input("Enter the object's mass: "))
		velocity = float(input("Enter the object's velocity: "))
		ke = kinetic_energy(mass, velocity)
		print('Mass', mass, 'Velocity', velocity, 'Kinetic Energy', ke)


number = int(input('Enter number of calculations: '))
main(number)