"""Steering Behaviors Script

Script to demonstrate the usage of steering behaviors for VideoGames AI.

Green Agent is Autonomous, Red One is Controlled by the player. 
To drive the red agent, use the cursor keys to turn and change speed. 
With F5 debug mode is activated.
F1 and F2 to change behaviour of the green agent.
F3 and F4 to increase/decrease the slow motion.
"""

import pygame
import pygame.gfxdraw
from os import path
from enum import Enum
import math
import random

class UpdateType(Enum):
    Autonomous = 0,
    Manual = 1

class SteeringType(Enum):
    Kinematic = 0,
    NonKinematic = 1

class DebugShape(Enum):
    Vector = 0,
    Cross = 1

def wrap_angle_180(x):
    x = math.fmod(x + 180.0, 360.0)
    if x < 0:
        x += 360.0
    return x - 180.0

def rotate2D(pivot = pygame.math.Vector2(0.0,0.0), point = pygame.math.Vector2(0.0,0.0), angle = 0.0):
    s = math.sin(angle)
    c = math.cos(angle)
    dist = point - pivot

    return pygame.math.Vector2(c * dist.x - s * dist.y + pivot.x, s * dist.x + c * dist.y + pivot.y)

class DebugDraw:

    delta = 0.01

    def __init__(self):
        self.commands = []
        self.history = []
        self.enabled = False

    def add_shape(self, shape = DebugShape.Vector, pos = pygame.math.Vector2(0.0, 0.0), v = pygame.math.Vector2(0.0,0.0),color = (255,0,0)):
        self.commands.append((shape, pos, v, color))

    def add_point(self, pos = pygame.math.Vector2(0.0, 0.0)):
        self.history.append(pygame.math.Vector2(pos))
        if len(self.history) > 1000:
            del self.history[0]

    def render(self, surface):
        if self.enabled:
            self.render_hist(surface)
            for command in self.commands:
                if command[0] == DebugShape.Vector:
                    self.render_vector(surface, command[1], command[2], command[3])
                if command[0] == DebugShape.Cross:
                    self.render_cross(surface, command[1], command[3])
            self.commands = []

    def render_vector(self, surface, pos, v, color):
        if v.length() > 0:
            dest = pos + v        
            pygame.gfxdraw.line(surface, int(pos.x), int(pos.y), int(dest.x), int(dest.y), color)

            p_tmp = dest - (v.normalize() * 5.0)
            pi_q = math.pi / 4.0
            p_arrow1 = rotate2D(dest, p_tmp, pi_q)
            p_arrow2 = rotate2D(dest, p_tmp, -pi_q)

            pygame.gfxdraw.line(surface, int(dest.x), int(dest.y), int(p_arrow1.x), int(p_arrow1.y), color)
            pygame.gfxdraw.line(surface, int(dest.x), int(dest.y), int(p_arrow2.x), int(p_arrow2.y), color)


    def render_cross(self, surface, pos, color):
        disp = 6.0
        p1 = pygame.math.Vector2(pos.x + disp, pos.y + disp)
        p2 = pygame.math.Vector2(pos.x + disp, pos.y - disp)
        p3 = pygame.math.Vector2(pos.x - disp, pos.y + disp)
        p4 = pygame.math.Vector2(pos.x - disp, pos.y - disp)

        pygame.gfxdraw.line(surface, int(p1.x), int(p1.y), int(p4.x), int(p4.y), color)
        pygame.gfxdraw.line(surface, int(p2.x), int(p2.y), int(p3.x), int(p3.y), color)

    def render_hist(self, surface):
        for point in self.history:
            pygame.gfxdraw.pixel(surface, int(point.x), int(point.y), (0,0,0))

class KinematicStatus:

    def __init__(self, position = pygame.math.Vector2(0.0, 0.0), orientation = 0.0 , velocity = pygame.math.Vector2(0.0, 0.0), rotation = 0.0,  speed = 0.0):
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.rotation = rotation
        self.speed = speed

class Steering:

    def __init__(self, linear = pygame.math.Vector2(0.0, 0.0), angular = 0.0):
        self.linear = linear
        self.angular = angular

class KinematicSteering:
    def __init__(self, velocity = pygame.math.Vector2(0.0, 0.0), rotation = 0.0):
        self.velocity = velocity
        self.rotation = rotation

class Agent:

    def __init__(self, image, update_type, steering = None):
        self.body = Body(image, update_type, steering)
        self.mind = Mind()

    def update(self, delta_time):
        self.body.update(delta_time)
        self.mind.update(delta_time)

    def render(self, surface):
        self.body.render(surface)

class Body:

    max_speed = 100.0

    def __init__(self, image, update_type, steering):
        self.steering = steering
        self.target = None
        self.state = KinematicStatus()
        self.image = image
        self.update_type = update_type

    def update(self, delta_time):
        if self.update_type == UpdateType.Autonomous:
            if self.steering is not None:
                result = self.steering.calculate(self.state, self.target.body.state)
                if self.steering.steering_type == SteeringType.Kinematic:
                    self.update_kinematic(delta_time, result)
                else:
                    self.update_non_kinematic(delta_time, result)

                if self.steering.needs_orientation:
                        self.set_orientation()
        else:
            self.update_manual(delta_time)

        self.keep_in_bounds()
        self.keep_in_speed()

        debug_draw.add_point(self.state.position)
        debug_draw.add_shape(DebugShape.Vector, self.state.position, self.state.velocity, (255,0,0))

    def render(self, surface):
        image = pygame.transform.rotate(self.image, -self.state.orientation)
        render_rect = image.get_rect()
        render_rect.center = self.state.position.xy
        surface.blit(image, render_rect)

    def set_target(self, target):
        self.target = target

    def set_steering(self, steering):
        self.steering = steering

    def update_kinematic(self, delta_time, steering):
        time = delta_time * 0.001  #dt comes in miliseconds
        self.state.velocity = steering.velocity
        self.state.position += steering.velocity * time
        self.state.rotation = steering.rotation
        self.state.orientation += steering.rotation * time

        self.keep_in_bounds()

    def update_non_kinematic(self, delta_time, steering):
        time = delta_time * 0.001  #dt comes in miliseconds
        self.state.velocity += steering.linear
        self.state.position += self.state.velocity * time
        self.state.rotation += steering.angular
        self.state.orientation += self.state.rotation * time

        self.keep_in_bounds()
        self.keep_in_speed()

    def update_manual(self, delta_time):
        time = delta_time * 0.001  #dt comes in miliseconds
        orientation = pygame.math.Vector2(0.0, 0.0)
        orientation.from_polar((1.0, self.state.orientation))
        self.state.velocity = orientation.normalize() * self.state.speed
        self.state.position += self.state.velocity * time

    def keep_in_speed(self):
        if self.state.velocity.length() > Body.max_speed:
            self.state.velocity = self.state.velocity.normalize() * Body.max_speed

    def keep_in_bounds(self):
        if self.state.position.x > screen_size[0]:
            self.state.position.x = 0.0
        if self.state.position.x < 0.0:
            self.state.position.x = screen_size[0]
        if self.state.position.y > screen_size[1]:
            self.state.position.y = 0.0
        if self.state.position.y < 0.0:
            self.state.position.y = screen_size[1]

    def set_orientation(self):
        if self.state.velocity.length_squared() > 0:
            self.state.orientation = math.degrees(math.atan2(self.state.velocity.y, self.state.velocity.x))

class Mind:

    def __init__(self):
        pass

    def update(self, delta_time):
        pass

class SteeringBehaviour:

    def __init__(self):
        pass

    def calculate(self, character, target):
        pass

class KinematicSeek(SteeringBehaviour):

    def __init__(self):
        self.max_speed = 100.0
        self.needs_orientation = True
        self.steering_type = SteeringType.Kinematic

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        result = KinematicSteering()
        #going full speed towards the target
        result.velocity = (target.position - character.position).normalize() * self.max_speed
        result.rotation = 0.0  #no rotation
        return result

class KinematicFlee(SteeringBehaviour):

    def __init__(self):
        self.max_speed = 100.0
        self.needs_orientation = True
        self.steering_type = SteeringType.Kinematic

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        result = KinematicSteering()
        #going full speed opposite to the target
        result.velocity = (character.position - target.position).normalize() * self.max_speed
        result.rotation = 0.0 #no rotation
        return result

class KinematicArrive(SteeringBehaviour):

    def __init__(self):
        self.max_speed = 100.0
        self.sq_radius = 25.0   #squared radius
        self.time_to_target = 0.5
        self.needs_orientation = True
        self.steering_type = SteeringType.Kinematic

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        result = KinematicSteering()
        #direction to the target
        result.velocity = target.position - character.position
        if result.velocity.length_squared() < self.sq_radius:  #inside the radius
            result.velocity.x = 0.0   #no velocity
            result.velocity.y = 0.0
        else:
            result.velocity /= self.time_to_target    #velocity adjusted to time
            if result.velocity.length() > self.max_speed:   #max out
                #normalized direction to max speed
                result.velocity = result.velocity.normalize() * self.max_speed
        result.rotation = 0.0  #no rotation
        return result

class KinematicWander(SteeringBehaviour):

    def __init__(self):
        self.max_speed = 50.0
        self.max_rotation = 90.0
        self.needs_orientation = False
        self.steering_type = SteeringType.Kinematic

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        orientation = pygame.math.Vector2(0.0, 0.0)
        #orientation of character as vector
        orientation.from_polar((1.0, character.orientation))

        result = KinematicSteering()
        result.velocity = orientation * self.max_speed  #max speed
        #rotate to random (binomial distribution around 0)
        result.rotation = self.max_rotation * (random.random() - random.random())

        return result

class Seek(SteeringBehaviour):

    def __init__(self):
        self.max_acceleration = 5.0
        self.needs_orientation = True
        self.steering_type = SteeringType.NonKinematic
    
    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        result = Steering()
        #acceleration towards the target
        result.linear = (target.position - character.position).normalize() * self.max_acceleration
        result.angular = 0.0   #no angular

        return result

class Flee(SteeringBehaviour):

    def __init__(self):
        self.max_acceleration = 5.0
        self.needs_orientation = True
        self.steering_type = SteeringType.NonKinematic
    
    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        result = Steering()
        #acceleration opposite to the target
        result.linear = (character.position - target.position).normalize() * self.max_acceleration
        result.angular = 0.0  #no angular

        return result

class Arrive(SteeringBehaviour):

    def __init__(self):
        self.max_acceleration = 5.0
        self.max_speed = 100.0
        self.slow_radius = 100.0
        self.time_to_target = 1.0
        self.needs_orientation = True
        self.steering_type = SteeringType.NonKinematic
    
    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        #direction to the target
        direction = target.position - character.position
        distance = direction.length()  #distance to target

        target_speed = self.max_speed  #max speed
        if distance < self.slow_radius:  #inside the slow zone
            #speed slowing down
            target_speed = (self.max_speed * distance) / self.slow_radius

        #velocity towards the target
        target_velocity = direction.normalize() * target_speed
        #linear acceleration adjusted to time
        result = Steering()
        result.linear = (target_velocity - character.velocity) / self.time_to_target
        if result.linear.length() > self.max_acceleration:  #max out
            #normalized to max acceleration
            result.linear = result.linear.normalize() * self.max_acceleration

        result.angular = 0.0  #no angular

        return result

class VelocityMatching(SteeringBehaviour):

    def __init__(self):
        self.max_acceleration = 5.0
        self.time_to_target = 1.0
        self.needs_orientation = True
        self.steering_type = SteeringType.NonKinematic
    
    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):       
        result = Steering()
        #linear acceleration adjusted to time
        result.linear = (target.velocity - character.velocity) / self.time_to_target
        if result.linear.length() > self.max_acceleration:  #max out
            #normalized to max acceleration
            result.linear = result.linear.normalize() * self.max_acceleration

        result.angular = 0.0  #no angular

        return result

class Align(SteeringBehaviour):

    def __init__(self):
        self.max_ang_acc = 20.0
        self.max_rotation = 90.0
        self.slow_radius = 2.0
        self.time_to_target = 0.1
        self.needs_orientation = False
        self.steering_type = SteeringType.NonKinematic
    
    def calculate(self, character = KinematicStatus(), target = KinematicStatus()): 
        #rotation between character and target wrapped to (-PI, PI) 
        rotation = wrap_angle_180(target.orientation - character.orientation)
        rotation_size = abs(rotation)  #absolute value of rotation

        target_rotation = self.max_rotation  #max
        if rotation_size < self.slow_radius:  #inside the slow zone
            #speed of rotation slowing down
            target_rotation = (self.max_rotation * rotation_size) / self.slow_radius

        target_rotation = math.copysign(target_rotation, rotation)  #positive or negative

        result = Steering()
        #angular acceleration adjusted to time
        result.angular = (target_rotation - character.rotation) / self.time_to_target
        if abs(result.angular) > self.max_ang_acc:  #too fast
            #normalized to max
            result.angular = math.copysign(1, result.angular) * self.max_ang_acc

        result.linear = pygame.math.Vector2(0.0, 0.0)  #no linear

        return result

class Pursue(Seek):

    def __init__(self):
        super().__init__()
        self.max_prediction = 2.0

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):  
        #distance to the target
        distance = (target.position - character.position).length()
        speed = character.velocity.length()  #speed of character

        prediction = self.max_prediction  #max prediction
        if speed > (distance / self.max_prediction):  #reasonable prediction
            prediction = distance / speed  #calc prediction time

        #new target
        new_target = KinematicStatus(pygame.math.Vector2(target.position), target.orientation, pygame.math.Vector2(target.velocity), target.rotation, target.speed)
        #position of new target
        new_target.position += target.velocity * prediction

        debug_draw.add_shape(DebugShape.Cross, new_target.position, color = (0,0,255))

        #delegate to seek behavior with new target
        return super().calculate(character, new_target)

class Face(Align):

    def __init__(self):
        super().__init__()

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):  
        #direction to target
        direction = target.position - character.position
        #new target
        new_target = KinematicStatus(pygame.math.Vector2(target.position), target.orientation, pygame.math.Vector2(target.velocity), target.rotation, target.speed)
        #orientation of new target facing direction
        new_target.orientation = math.degrees(math.atan2(direction.y, direction.x))

        #delegate to align behavior with new target
        return super().calculate(character, new_target)

class LookGoing(Align):

    def __init__(self):
        super().__init__()

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        if character.velocity.length() == 0:  #no movement
            return Steering()

        new_target = KinematicStatus(pygame.math.Vector2(target.position), target.orientation, pygame.math.Vector2(target.velocity), target.rotation, target.speed)
        #orientation of new target facing velocity
        new_target.orientation = math.degrees(math.atan2(character.velocity.y, character.velocity.x))

        #delegate to align behavior with new target
        return super().calculate(character, new_target)

class Wander(Face):

    def __init__(self):
        super().__init__()
        self.wander_offset = 50.0
        self.wander_radius = 20.0
        self.wander_rate = 100.0
        self.wander_orientation = 0.0
        self.max_acceleration = 2.0

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        #update wander orientation, rate * binomial distribution
        self.wander_orientation += self.wander_rate * (random.random() - random.random())
        new_target = KinematicStatus()
        #orientation of new target facing combined orientation
        new_target.orientation = self.wander_orientation + character.orientation

        char_orient = pygame.math.Vector2(0.0, 0.0)  #orientation of character as vector
        char_orient.from_polar((1.0, character.orientation))

        target_orient = pygame.math.Vector2(0.0, 0.0)  #orientation of new target as vector
        target_orient.from_polar((1.0, new_target.orientation))

        #the center of the circle
        new_target.position = character.position + (char_orient * self.wander_offset)
        #position of the target in the circle
        new_target.position += target_orient * self.wander_radius

        debug_draw.add_shape(DebugShape.Cross, new_target.position, color = (0,0,255))

        #delegate to face behavior
        result = super().calculate(character, new_target)
        #linear to full acceleration in direction of orientation
        result.linear = char_orient.normalize() * self.max_acceleration

        return result

pygame.init()

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size, 0, 32)
running = True
clock = pygame.time.Clock()
pygame.key.set_repeat(120)

red_agent_image = pygame.image.load(path.join(*['agent_red.png'])).convert_alpha()
green_agent_image = pygame.image.load(path.join(*['agent_green.png'])).convert_alpha()

agent_red = Agent(red_agent_image, UpdateType.Manual)
agent_green = Agent(green_agent_image, UpdateType.Autonomous)
agent_red.body.state.position = pygame.math.Vector2(screen_size[0]/2,screen_size[1]/2)
agent_green.body.set_target(agent_red)
debug_draw = DebugDraw()

steerings = [None, KinematicSeek(), KinematicFlee(), KinematicArrive(), KinematicWander(), Seek(), Flee(), Arrive(), VelocityMatching(), Align(), Pursue(), Face(), LookGoing(), Wander()]

current_steer = 0
slo_mo = 1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                agent_red.body.state.position = pygame.math.Vector2(event.pos[0],event.pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_F5:
                debug_draw.enabled = not debug_draw.enabled
            if event.key == pygame.K_UP:
                agent_red.body.state.speed += 20.0 if agent_red.body.state.speed < 120.0 else 0.0
            if event.key == pygame.K_DOWN:
                agent_red.body.state.speed -= 20.0 if agent_red.body.state.speed > 0.0 else 0.0
            if event.key == pygame.K_LEFT:
                agent_red.body.state.orientation -= 10.0
            if event.key == pygame.K_RIGHT:
                agent_red.body.state.orientation += 10.0
            if event.key == pygame.K_F1:
                current_steer = (current_steer - 1) % len(steerings)
                agent_green.body.set_steering(steerings[current_steer])
                print(f"New Steering Behaviour {steerings[current_steer].__class__}")
            if event.key == pygame.K_F2:
                current_steer = (current_steer + 1) % len(steerings)
                agent_green.body.set_steering(steerings[current_steer])
                print(f"New Steering Behaviour {steerings[current_steer].__class__}")
            if event.key == pygame.K_F3:
                if slo_mo > 1:
                    slo_mo -= 1
            if event.key == pygame.K_F4:
                if slo_mo < 5:
                    slo_mo += 1

    delta_time = clock.tick(30) / slo_mo

    agent_red.update(delta_time)
    agent_green.update(delta_time)

    screen.fill((200, 200, 200))

    debug_draw.render(screen)
    agent_red.render(screen)
    agent_green.render(screen)

    pygame.display.update()

pygame.quit()