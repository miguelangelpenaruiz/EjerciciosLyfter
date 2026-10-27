class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Torso: 
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm


class Foot:
    def __init__(self):
        pass


class Leg:
    def __init__(self, foot):
        self.foot = foot


class Human:
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg


my_head = Head()
my_right_hand = Hand()
my_left_hand = Hand()
my_right_arm = Arm(my_right_hand)
my_left_arm = Arm(my_left_hand)
my_torso = Torso(my_head, my_right_arm, my_left_arm)
my_right_foot = Foot()
my_left_foot = Foot()
my_right_leg = Leg(my_right_foot)
my_left_leg = Leg(my_left_foot)

me = Human(my_torso, my_right_leg, my_left_leg)

print(me.torso.right_arm.hand)