import pygame
pygame.init()


back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()


#переменные, отвечающие за координаты платформы
racket_x = 200
racket_y = 330


#флаг окончания игры
game_over = False
#класс из предыдущего проекта
class Area():
   def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height)
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


#класс для объектов-картинок
class Picture(Area):
   def __init__(self, filename, x=0, y=0, width=10, height=10):
       Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
       self.image = pygame.image.load(filename)
      
   def draw(self):
       mw.blit(self.image, (self.rect.x, self.rect.y))


#создание мяча и платформы   
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)


#создание врагов
start_x = 5 #координаты создания первого монстра
start_y = 5
count = 9 #количество монстров в верхнем ряду
monsters = [] #список для хранения объектов-монстров
for j in range(3): #цикл по столбцам
   y = start_y + (55 * j) #координата монстра в каждом след. столбце будет смещена на 55 пикселей по y
   x = start_x + (27.5 * j) #и 27.5 по x
   for i in range (count):#цикл по рядам (строкам) создаёт в строке количество монстров, равное count
       d = Picture('enemy.png', x, y, 50, 50) #создаём монстра
       monsters.append(d) #добавляем в список
       x = x + 55 #увеличиваем координату следующего монстра
   count = count - 1  #для следующего ряда уменьшаем кол-во монстров


while not game_over:
   ball.fill()
   platform.fill()
      
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           game_over = True


   #отрисовываем всех монстров из списка
   for m in monsters:
       m.draw()


   platform.draw()
   ball.draw()


   pygame.display.update()


   clock.tick(40)
