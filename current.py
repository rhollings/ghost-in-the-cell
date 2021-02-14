import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]

# game loop
while True:
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    myFactoryId = -1
    enemyFactoryId = -1
    troops = 0
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        
        if entity_type == "FACTORY":
            if arg_1 == 1:
                myFactoryId = entity_id
                troops = arg_2
            else:
                enemyFactoryId = entity_id

    # Ability to make muliti moves per turn()how to write??"
    if myFactoryId != -1 and enemyFactoryId != -1:
        print("MOVE", myFactoryId, "", enemyFactoryId, "",troops)
    else:
        print("WAIT")
