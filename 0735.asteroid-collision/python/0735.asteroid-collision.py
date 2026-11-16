# @leetcode slug=asteroid-collision id=735 qid=735
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        #Value repersent size, sign repersents direction,
        # if two meet, smaller one will explode

        #edge cases:
        #go from left to right, and find negative signs, each time you interact with negative, simulate collison.
        #need way to add or remove (whatewver ik its a stack problem)

        #what informatiom must be mainted:
        # stack of asteroids, which will be ruturned as answer, an iterative index, and value of said index.

        #algorithm:
        #iterate through array.
        #add to answer stack, untill you see a negative sign. 
        #if top is negative, skip iteration, if top is pos. ->
        #simulate collisions, untill either current gets destroyed, or the stack is empty
        #repeat.
        #join stack to form answer list.

        asteroidStack = []

        for currAsteroid in asteroids:
            survived = True

            while asteroidStack and asteroidStack[-1] > 0 and currAsteroid < 0:

                if asteroidStack[-1] < abs(currAsteroid):
                    asteroidStack.pop()

                elif asteroidStack[-1] == abs(currAsteroid):
                    asteroidStack.pop()
                    survived = False
                    break

                else:
                    survived = False
                    break

            if survived:
                asteroidStack.append(currAsteroid)

        return asteroidStack
