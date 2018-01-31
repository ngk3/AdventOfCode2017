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
    
    # Function used to get the position of the Particle as a String
    def getPosition(self):
        return str(self.pos[0]) + "," + str(self.pos[1]) + "," + str(self.pos[2])
    
    # Function used to compare the position of the Particle with a position-string
    def comparePositions(self, pos_string):
        pos_string_splitted = pos_string.split(",")
        return self.pos[0] == pos_string_splitted[0] and self.pos[1] == pos_string_splitted[1] and self.pos[2] == pos_string_splitted[2]

# Function used to read the input file and return the particles created from the input file        
def readFileAndCreateParticles(file_name):
    particles = dict([])
    count = 0
    for part in open(file_name, 'r'):
        part_splitted = part.strip().split(", ")
        particles[count] = Particle(part_splitted[0], part_splitted[1], part_splitted[2])
        count += 1
    return particles

# Function used to find the number of particles left after all collisions are resolved
def findNumParticlesAfterCollisions(num_zero_collide, particles):
    count = 0
    current_len_particles = len(particles)
    while count < num_zero_collide:
        # If collision is found, reset the count timer
        if current_len_particles > len(particles):
            current_len_particles = len(particles)
            count = 0
        else:
            count += 1
            
        # Get all the new positions of the particles and frequency
        all_positions = dict([])
        for p in particles.keys():
            adding_pos = particles[p].getPosition()
            if adding_pos in all_positions.keys():
                all_positions[adding_pos] += 1
            else: 
                all_positions[adding_pos] = 1
        
        # Remove any collision particles 
        collision_positions = []
        for ap in all_positions.keys():
            if all_positions[ap] > 1:
                collision_positions.append(ap)
                
        for p in particles.keys():
            if particles[p].getPosition() in collision_positions:
                del particles[p]
            
        # Move every particle
        for p in particles.keys():
            particles[p].move()
    return len(particles)
			
particles = readFileAndCreateParticles("Star39_input.txt")
print "Number of particles left after collisions =", findNumParticlesAfterCollisions(1000, particles)