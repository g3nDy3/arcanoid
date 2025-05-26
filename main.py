import pygame
pygame.init()
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

platform_x = 200
platform_y = 330

dx = 3
dy = 3

move_right = False
move_left = False

game_over = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ область: прямоугольник в нужном месте и нужного цвета """
        #запоминаем прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


#создание мяча и платформы 
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 30)

#создание врагов
start_x = 5
start_y = 5
count = 9
monsters = []
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)
    for i in range (count):
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1


while not game_over:
    ball.fill()
    platform.fill()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                move_right = True 
            if event.key == pygame.K_LEFT:
                move_left = True 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False 
            if event.key == pygame.K_LEFT:
                move_left = False 
        

    if move_right:
        platform.rect.x +=3
    if move_left: 
        platform.rect.x -=3
    ball.rect.x += dx
    ball.rect.y += dy
    if  ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.colliderect(platform.rect):
        dy *= -1


    for m in monsters:
        m.draw()
    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)
