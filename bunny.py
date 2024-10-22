class Bunny:
    # Set physical characteristics
    def __init__(bunny, arm_length, leg_length, eyes, tail, furry):
        bunny.arm_length = arm_length
        bunny.leg_length = leg_length
        bunny.eyes = eyes
        bunny.tail = tail
        bunny.furry = furry

    # Print physical characteristics
    def describe(bunny):
        print(f"Bunny characteristics:")
        print(f"  Arm length: {bunny.arm_length} cm")
        print(f"  Leg length: {bunny.leg_length} cm")
        print(f"  Eyes: {bunny.eyes}")
        print(f"  Tail: {'Yes' if bunny.tail else 'No'}")
        print(f"  Furry: {'Yes' if bunny.furry else 'No'}")

# Creating Bunny class
bunny = Bunny(arm_length=53.09, leg_length=79.64, eyes=2, tail=True, furry=True)

# tell to describe
bunny.describe()