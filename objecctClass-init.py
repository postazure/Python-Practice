class Ball:
    def __init__(self, color, size, direction, owner):
        self.color = color
        self.size = size
        self.direction = direction
        self.owner = owner

    def __str__(self):
        msg = "I'm " + self.owner + "'s ball"
        return msg
    
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
            
myBall = Ball("red","small", "down", "Max")
elyseBall = Ball("black", "Large", "down", "Elyse")


print myBall

print 'My ball is', myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print
myBall.bounce()
print "Now the ball's direction is", myBall.direction



print elyseBall
print elyseBall.owner + "'s ball is " + elyseBall.size
print elyseBall.owner + "'s ball is "+ elyseBall.color
print elyseBall.owner + "'s ball's direction is "+ elyseBall.direction
print "I'm going to bounce "+ elyseBall.owner +"'s ball"
print
elyseBall.bounce()
print "Now ", elyseBall.owner + "'s ball's directions is ", elyseBall.direction
