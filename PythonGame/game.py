import pygame

pygame.init()
screenWidth = 900
screenHeight = 600
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("2D platformer")

walkRight = [pygame.image.load('images\\player_right (1).png'), pygame.image.load('images\\player_right (2).png'), 
pygame.image.load('images\\player_right (3).png'), pygame.image.load('images\\player_right (4).png'), 
pygame.image.load('images\\player_right (5).png'), pygame.image.load('images\\player_right (6).png'),
pygame.image.load('images\\player_right (7).png'),
pygame.image.load('images\\player_right (9).png'), pygame.image.load('images\\player_right (10).png'),
pygame.image.load('images\\player_right (11).png'),] #pygame.image.load('C:\\Users\\Suren\\Desktop\\game\\player_right (8).png'),

walkLeft = [pygame.image.load('images\\player_left (1).png'), pygame.image.load('images\\player_left (2).png'), 
pygame.image.load('images\\player_left (3).png'), pygame.image.load('images\\player_left (4).png'), 
pygame.image.load('images\\player_left (5).png'), pygame.image.load('images\\player_left (6).png'),
pygame.image.load('images\\player_left (7).png'),
pygame.image.load('images\\player_left (9).png'), pygame.image.load('images\\player_left (10).png'),
pygame.image.load('images\\player_left (11).png') ] #pygame.image.load('C:\\Users\\Suren\\Desktop\\game\\player_left (8).png'),

player_stand = pygame.image.load('images\\p1_front.png')
bg = pygame.image.load('images\\bg_1.jpg')
player_jump = pygame.image.load('images\\p1_jump.png')

clock = pygame.time.Clock()

x = 30 #Start coordinate X (left right)
y = screenHeight / 2 + screenHeight / 3 #Start coordinate Y (up down)

width = 72 #Right/left
height = 97 #Up/down 

speed = 7 #Player speed

indent = 10 #Wall width

jump = False
jumpInst = 10
jumpCount = jumpInst

reloadVar = 1

left = False
right = False

lastMove = "right"

animCount = 0

class Bullet():
   def __init__(self, x, y, radius, color, side):
      self.x = x #bullet x coordinate
      self.y = y #bullet y coordinate
      self.radius = radius #bullet radius
      self.color = color #bullet color
      self.side = side #bullet side
      self.vel = 8 * side #bullet speed

   def draw(self, win):
      pygame.draw.circle(win, 
         self.color, (self.x, self.y), self.radius)

def drawWindow():
   global animCount

   #win.fill((128,0,128))
   win.blit(bg, (0,0))

   if animCount + 1 >= 30:
      animCount = 0

   if left:
      win.blit(walkLeft[animCount // 3], (x,y))
      animCount += 1
   elif right:
      win.blit(walkRight[animCount // 3], (x,y))
      animCount += 1
   elif jump:
      win.blit(player_jump, (x,y))
   else:
      win.blit(player_stand, (x,y))

   for f in bulletS:
      f.draw(win)


   pygame.display.update()

run = True
bulletS = []
while run:
   clock.tick(30)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

   for k in bulletS:
      if k.x < screenWidth and k.x > 0:
         k.x += k.vel
      else:
         bulletS.pop(bulletS.index(k))




   keys = pygame.key.get_pressed()

   if keys[pygame.K_f]:
      if lastMove == "right":
         side = 1
      else:
         side = -1
      if reloadVar == 5:
         if len(bulletS) < 20: #bullet limit
            bulletS.append(Bullet(round(x + width // 2), 
               round(y + height // 2 + 3), 5, (255,0,0), 
               side))
            reloadVar = 1
      else:
         reloadVar += 1



   if keys[pygame.K_LEFT] and x > indent:
      x -= speed
      left = True
      right = False
      lastMove = "left"
   elif keys[pygame.K_RIGHT] and x < screenWidth - width - (indent - 5):
      x += speed
      left = False
      right = True
      lastMove = "right"
   else:
      left = False
      right = False
      animCount = 0
   if not(jump):
      if keys[pygame.K_SPACE]:
         jump = True
   else:
      if jumpCount >= -jumpInst:
         if jumpCount < 0:
            y += (jumpCount ** 2) / 2
         else:
            y -= (jumpCount ** 2) / 2
         jumpCount -= 1
      else:
         jump = False
         jumpCount = jumpInst

   drawWindow()
   

pygame.quit()