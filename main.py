import pygame
from math import radians, sin, cos
from datetime import datetime


class Clock():
    def __init__(self):
        self.width, self.height = 600, 600
        self.orange = (120, 56, 7)
        self.black = (20, 19, 19)
        self.FPS = 60
        self.center = (self.width//2, self.height//2)
        self.clock_redius = self.width//2
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Analog Clock")
        self.clock = pygame.time.Clock()
    
    
    def numbers(self, number, size, position):
        font = pygame.font.SysFont('calibri', size, True, False)
        text = font.render(str(number), True, self.orange)
        text_rect = text.get_rect(center=position)
        self.screen.blit(text, text_rect)
    
    def polar_to_cartesian(self, r, theta):
        x = r * sin(radians(theta))
        y = r * cos(radians(theta))
        return self.width//2 + x, self.height//2 - y
    
    def draw_circle(self, screen):
        pygame.draw.circle(self.screen, self.orange, self.center, self.clock_redius - 10, 5)
         
        pygame.draw.circle(self.screen, self.orange, self.center, 7)
        
        
        for number in range(1, 13):
            self.numbers(number, 40, self.polar_to_cartesian(self.clock_redius - 60, number * 30))
        
        
        for number in range(0, 360, 6):
            if number % 5:
                pygame.draw.line(self.screen, self.orange, self.polar_to_cartesian(self.clock_redius - 15, number),
                                 self.polar_to_cartesian(self.clock_redius - 25, number), 2)

            else:
                pygame.draw.line(self.screen, self.orange, self.polar_to_cartesian(self.clock_redius - 15, number),
                                 self.polar_to_cartesian(self.clock_redius - 30, number), 6)
        
    
    def draw_clock_hand(self):
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        secound = current_time.second
        
        #Hour hand
        
        R = self.clock_redius - 150
        theta = (hour + minute / 60 + secound / 3600) * (360 / 12)
        pygame.draw.line(self.screen, self.orange, self.center, self.polar_to_cartesian(R, theta), 11)
        
        #Minute hand
        R = self.clock_redius - 110
        theta = (minute + secound / 60) * (360 / 60)
        pygame.draw.line(self.screen, self.orange, self.center, self.polar_to_cartesian(R, theta), 9)
        
        #Second hand
        R = self.clock_redius - 110
        theta = secound * (360 / 60)
        pygame.draw.line(self.screen, self.orange, self.center, self.polar_to_cartesian(R, theta), 4)
        
        
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    exit()
                    
                    
            self.screen.fill(self.black)
            self.draw_circle(self.screen)
            self.draw_clock_hand()
            
            pygame.display.update()
            self.clock.tick(self.FPS)
            
if __name__ == "__main__":
    myclock = Clock()
    myclock.run()
    