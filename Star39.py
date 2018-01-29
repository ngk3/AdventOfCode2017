class Particle:
	def __init__(self, position, velocity, acceleration):
		position = position.replace("p=<", "").replace(">", "").strip()
		self.pos = position.split(",")
		velocity = velocity.replace("v=<", "").replace(">", "").strip()
		self.vel = velocity.split(",")
		acceleration = acceleration.replace("a=<", "").replace(">", "").strip()
		self.acc = acceleration.split(",")
		for i in range(3):
			self.pos[i] = int(self.pos[i])
			self.vel[i] = int(self.vel[i])
			self.acc[i] = int(self.acc[i])
				
	def move(self):
		for i in range(3):
			self.vel[i] += self.acc[i]
			self.pos[i] += self.vel[i]
					
	def getDistanceOrigin(self):
		return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
					
def readFileAndCreateParticles(file_name):
	particles = []
	for part in open(file_name, 'r'):
		part_splitted = part.split(",")
		particles.append(Particle(part_splitted[0], part_splitted[1], part_splitted[2]))
	return particles
		
def findClosestParticleOrigin(particles):
	index = 0
	distance = particles[0].getDistanceOrigin()
	for p in range(len(particles)):
		if particles[p].getDistanceOrigin() < distance:
			index = p
			distance = particles[p].getDistanceOrigin()
	return index
			
def findLongRunOrigin(particles):
	index = 0
	count = 0
	while count < 10:
		new_index = findClosestParticleOrigin(particles)
		if new_index != index:
			index = new_index
			count = 0
		else:
			count += 1
		for p in particles:
			p.move()
	return index
			
particles = readFileAndCreateParticles("testing.txt")
print "Particle closest to (0,0,0) in long run is Particle ", findLongRunOrigin(particles)