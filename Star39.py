# Class to represent each Particle
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
			
    # Moves the particle according to its position, velocity, and acceleration 
    def move(self):
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]
					
    # Gets the distance from the Origin (0, 0)
    def getDistanceOrigin(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])

# Function used to read the input file and return the particles created from the input file        
def readFileAndCreateParticles(file_name):
    particles = dict([])
    count = 0
    for part in open(file_name, 'r'):
        part_splitted = part.strip().split(", ")
        particles[count] = Particle(part_splitted[0], part_splitted[1], part_splitted[2])
        count += 1
    return particles

# Function used to find the closest particle to the origin at any tick    
def findClosestParticleOrigin(particles):
	index = 0
	distance = particles[0].getDistanceOrigin()
	for p in range(len(particles)):
		if particles[p].getDistanceOrigin() < distance:
			index = p
			distance = particles[p].getDistanceOrigin()
	return index

# Function used to find the closest particle in the long-run (when the same index closest to the particle num_match_end times in a row)    
def findLongRunOrigin(num_match_end, particles):
	index = 0
	count = 0
	while count < num_match_end:
        # Check if a new index is closer and reset count if so
		new_index = findClosestParticleOrigin(particles)
		if new_index != index:
			index = new_index
			count = 0
		else:
			count += 1
        # Move every particle
		for p in particles.keys():
			particles[p].move()
	return index
			
particles = readFileAndCreateParticles("Star39_input.txt")
print "Particle closest to (0,0,0) in long run is Particle ", findLongRunOrigin(1000, particles)