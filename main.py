import js
p5 = js.window
sun_img1 = p5.loadImage('img/sun1.png')
sun_img2 = p5.loadImage('img/sun2.png')
earth_img = p5.loadImage('img/green.png')
program_state = 'Default'
planet_state = 'MIDDLE'

font = p5.loadFont('PressStart2P(1).otf')
# variable to store sound data:
sound = p5.loadSound('BGM3.mp4')  


class cloud():
  def __init__(self):
    self.img = p5.loadImage('img/cloud.png')
    self.x = 150   
    self.y = 300
  
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.scale(0.34)
    p5.image(self.img,  0, 0)
    p5.pop()
cloud=cloud()   

class sprinkle():
  x = 0
  y = 0
  width =4
  height = 4

  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def draw(self):
    p5.fill(160,180,225)
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.ellipse(0, 0, self.width, self.height)
    else:
      p5.ellipse(0, 0, self.width/3, self.height/3)
    self.timer = p5.millis()
    p5.pop()
    
class sprinkleChild(sprinkle): 
  def draw(self):
    p5.fill(220,200,94)
    p5.push()
    p5.translate(self.x+10, self.y-50)
    if(p5.millis() % 1000 < 500):
      p5.ellipse(0, 0, self.width, self.height)
    else:
      p5.ellipse(0, 0, self.width/3, self.height/3)
    self.timer = p5.millis()
    p5.pop()
    
class sprinkleChild2(sprinkle): 
  def draw(self):
    p5.fill(240,150,230)
    p5.push()
    p5.translate(self.x+10, self.y-50)
    if(p5.millis() % 1000 < 500):
      p5.ellipse(0, 0, self.width, self.height)
    else:
      p5.ellipse(0, 0, self.width/3, self.height/3)
    self.timer = p5.millis()
    p5.pop()
# create an instance of Sprite object:
sprinkle1 = sprinkle(x = 75, y = 150)  

sprinkle2 = sprinkleChild(x = 225, y = 150)  

sprinkle3 = sprinkleChild(x = 255, y = 280)  
class shooting():
  def __init__(self):
    self.timer = p5.millis()
    self.img1 = p5.loadImage('img/s0.png')
    self.img2 = p5.loadImage('img/s1.png')
    self.img3 = p5.loadImage('img/s2.png')
    self.x = 260  
    self.y = 200
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.scale(0.5)
    if(p5.millis() % 2000 < 1300):
      p5.image(self.img1, 0, 0)
    elif(1000<p5.millis() % 2000 < 1700):
      p5.image(self.img2, 0, 0)
    elif(1700<p5.millis() % 2000 < 2000):
      p5.image(self.img3, 0, 0)
    self.timer = p5.millis()
    p5.pop()
shooting=shooting()  
  
class Planet():  
  def __init__(self):
    self.timer = p5.millis()
    self.img1 = p5.loadImage('img/planet1.png')
    self.img2 = p5.loadImage('img/planet2.png')
    self.x = 185  
    self.y = 40  

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.scale(0.07)
    if(p5.millis() % 2000 < 1000):
      p5.image(self.img1, 0, 0)
    else:
      p5.image(self.img2, 0, 0)
    self.timer = p5.millis()
    p5.pop()

planet=Planet()

class Earth():
  def __init__(self):
    self.timer = p5.millis()
    self.img = p5.loadImage('img/green.png')
    self.imgcold = p5.loadImage('img/cold.png')
    self.imghot = p5.loadImage('img/hot.png')
    self.x = 165  
    self.y = 525
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y+2)
    p5.image(self.img,  0, 0)
    p5.pop()

  def drawcold(self):
    p5.push()
    p5.translate(self.x-14, self.y-10)
    p5.image(self.imgcold,  0, 0)
    p5.pop()

  def drawhot(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.imghot,  0, 0)
    p5.pop()
    
earth=Earth()

class human():
  def __init__(self,x =200, y=360,x1 =210, y1=310,x2 =240, y2=360, x3 =200, y3=350, x4 =215, y4=328):
    self.img = p5.loadImage('img/human.png')
    self.imgcold = p5.loadImage('img/float.png')
    self.imghot = p5.loadImage('img/human.png')
    self.imgcold1 = p5.loadImage('img/person1.png')
    self.imgcold2 = p5.loadImage('img/person2.png')
    self.imgcold3 = p5.loadImage('img/person3.png')
    self.imgcold4 = p5.loadImage('img/door.png')
    self.x = x  
    self.y = y
    self.x1 = x1  
    self.y1 = y1
    self.x2 = x2  
    self.y2 = y2
    self.x3 = x3  
    self.y3 = y3
    self.x4 = x4  
    self.y4 = y4
  def draw(self):
    p5.push()
    p5.translate(self.x+15, self.y-15)
    p5.scale(0.5)
    p5.image(self.img,  0, 0)
    p5.pop()
  def drawcold(self):
    p5.push()
    p5.translate(self.x4, self.y4)
    p5.scale(0.5)
    p5.image(self.imgcold4,  0, 0)
    p5.pop()
    p5.push()
    p5.translate(self.x1, self.y1)
    p5.scale(0.55)
    p5.image(self.imgcold1,  0, 0)
    p5.pop()
    p5.push()
    p5.translate(self.x2, self.y2)
    p5.scale(0.55)
    p5.image(self.imgcold2,  0, 0)
    p5.pop()
    p5.push()
    p5.translate(self.x3, self.y3)
    p5.scale(0.55)
    p5.image(self.imgcold3,  0, 0)
    p5.pop()
  def drawhot(self):
    p5.push()
    p5.translate(self.x+15, self.y-15)
    p5.scale(0.5)
    p5.image(self.img,  0, 0)
    p5.pop()
  def float(self):
    self.x1 += 0.04
    self.y1 -= 0.12
    self.x2 -= 0.12
    self.y2 -= 0.18
    self.x3 -= 0.14
    self.y3 -= 0.28
    
human=human() 

class house():
  def __init__(self):
    self.img = p5.loadImage('img/house.png')
    self.imgcold = p5.loadImage('img/house.png')
    self.imghot = p5.loadImage('img/ruins.png')
    self.x = 80  
    self.y = 330
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.scale(0.4)
    p5.rotate(p5.radians(-5))
    p5.image(self.img,  0, 0)
    p5.pop()
  def drawcold(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.scale(0.4)
    p5.rotate(p5.radians(-5))
    p5.image(self.imgcold,  0, 0)
    p5.pop()
  def drawhot(self):
    p5.push()
    p5.translate(self.x, self.y-10)
    p5.scale(0.35)
    p5.rotate(p5.radians(-5))
    p5.image(self.imghot,  0, 0)
    p5.pop()
house=house() 

class moon():
  def __init__(self, x = 150, y = 180):
    self.img = p5.loadImage('img/moon.png')
    self.imgcold = p5.loadImage('img/Asteroid belt.png')
    self.imghot = p5.loadImage('img/moon.png')
    self.x = x
    self.y = y
  def draw(self):
    p5.push()
    p5.translate(self.x+20, self.y-5)
    p5.scale(0.2)
    p5.image(self.img,  0, 0)
    p5.pop()
  def drawcold(self):
    p5.push()
    p5.translate(self.x, self.y+50)
    p5.scale(0.4)
    p5.image(self.imgcold,  0, 0)
    p5.pop()
  def drawhot(self):
    p5.push()
    p5.translate(self.x, self.y+150)
    p5.scale(1.3)
    p5.image(self.img,  0, 0)
    p5.pop()
  def move(self):
    self.x += 0.05
    self.y -= 0.03
    if(self.x > p5.width + 40):
      self.x = 150
      self.y = 330 
moon=moon()

def setup():
  p5.createCanvas(300, 600)
  p5.rectMode(p5.CENTER)
  p5.imageMode(p5.CENTER)
  p5.textSize(18)
  print('move the planet..')
  p5.textFont(font)
  

def draw():
  global sound
  
  p5.background(9,50,20) 
  global program_state
  global planet_state
  p5.fill(255)  # fill with black
  p5.noStroke()  # no stroke
  
  # show cursor coordinates:
  p5.strokeWeight(1)  # 1-pixel stroke
  global planet
  p5.background(0)  
  if(planet_state == 'HOT') and (program_state == 'PLAY'):
    p5.background(35,5,35)
  if(planet_state == 'COLD') and (program_state == 'PLAY'):
    p5.background(11,22,37)
  if(p5.millis() % 1000 < 500):
        p5.image(sun_img1, 0, 0,sun_img1.width/2.8, sun_img1.height/2.8)
  else:
        p5.image(sun_img2, 0, 0,sun_img1.width/2.8, sun_img1.height/2.8)
  
  p5.stroke(60)
  p5.strokeWeight(6)
  p5.strokeCap(p5.ROUND) 
  p5.line(90, 40, 280, 40)
  p5.noStroke(0)
  planet.draw()
  p5.fill(255)
  p5.textSize(18)
  if(p5.keyIsPressed == True):
      if(p5.keyCode == p5.RIGHT_ARROW):
        if(planet.x < 260):
          planet.x += 0.8
          
      elif(p5.keyCode == p5.LEFT_ARROW):
        if(planet.x > 105):
          planet.x -= 0.8
  if(program_state == 'Default'):
    p5.textSize(16)
    p5.fill(255)
    p5.text('Click to start', 45, 170)
    p5.textSize(8)
    p5.text('In this project, you are able to', 25, 190)
    p5.text('move the planet to change its', 35, 205)
    p5.text('climate and ecology', 80, 220)
    earth.draw()
    
    
  if(program_state == 'PLAY'):
    p5.textSize(8)
    p5.text('Press arrows to move the planet', 45, 85)
    shooting.draw()
    earth.draw()
    if(planet.x<140):
      planet_state= 'HOT'  
    if(planet.x>240):
       planet_state= 'COLD'
    if(140<planet.x<240):
       planet_state= 'MIDDLE'
    
      
  if(planet_state == 'HOT') and (program_state == 'PLAY'):
    sound.play()
    #p5.background(170,30,100)
    p5.textSize(24)
    p5.fill(199,246,246)
    moon.drawhot()
    moon.move()
    earth.drawhot()
    cloud.draw()
    house.drawhot()
    human.drawhot()
    p5.text('CLOSE', 95, 450)
    # print('When the planet move closer to the sun, the temperature will increase and the climate will become hotter. Besides, the closer distance to the Sun will lead to a stronger gravitational pull of the sun, which means the gravity of the earth will increase. This will result in the crash of buildings. The moon will also be bigger becuase it has been dragged to the earth more.')
    
  elif(planet_state == 'COLD')and (program_state == 'PLAY'):
    p5.textSize(24)
    p5.fill(36,38,111)
    moon.drawcold()
    earth.drawcold()
    house.drawcold()
    human.drawcold()
    human.float()
    p5.text('FAR', 120, 450)
    
  elif(planet_state == 'MIDDLE')and (program_state == 'PLAY'):
    p5.textSize(24)
    p5.fill(28,52,86)
    shooting.draw()
    earth.draw()
    house.draw()
    human.draw()
    moon.draw()
    p5.text('MIDDLE', 82, 450)
    sprinkle1.draw()
    sprinkle2.draw()
    sprinkle3.draw()

def keyPressed(event):
  print('key pressed.. ' + p5.key)

def keyReleased(event):
  pass
  
def mousePressed(event):
  global program_state
  if(program_state == 'Default'):
    program_state = 'PLAY'


def mouseReleased(event):
  pass
