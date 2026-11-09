import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PIXEL HERO")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (20, 20, 30)
RED = (230, 60, 60)
YELLOW = (255, 220, 50)

font = pygame.font.SysFont("Arial", 30)

player = pygame.image.load("images/pygame.png.jpeg").convert()
player.set_colorkey((255, 255, 255))
player = pygame.transform.scale(player, (70, 80))

player_rect = player.get_rect(center=(400, 500))

player_speed = 5
lives = 3
score = 0

bullets = []
bullet_speed = 9

enemies = []
enemy_speed = 3

def create_enemy():
    x = random.randint(0, WIDTH - 40)
    y = -40

    rect = pygame.Rect(x, y, 40, 40)
    enemies.append(rect)

for i in range(4):
    create_enemy()

running = True
game_over = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = pygame.Rect(
                    player_rect.centerx - 6,
                    player_rect.top,
                    12,
                    15
                )
                bullets.append(bullet)

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_rect.x -= player_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_rect.x += player_speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_rect.y -= player_speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_rect.y += player_speed

        player_rect.clamp_ip(screen.get_rect())

        for bullet in bullets[:]:
            bullet.y -= bullet_speed

            if bullet.bottom < 0:
                bullets.remove(bullet)

        for enemy in enemies[:]:
            enemy.y += enemy_speed

            if enemy.top > HEIGHT:
                enemies.remove(enemy)
                create_enemy()

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    create_enemy()
                    break

        for enemy in enemies[:]:
            if player_rect.colliderect(enemy):
                lives -= 1
                enemies.remove(enemy)
                create_enemy()

                if lives <= 0:
                    game_over = True

    screen.fill((25, 30, 55))

    if not game_over:
        screen.blit(player, player_rect)

        for bullet in bullets:
            pygame.draw.rect(screen, YELLOW, bullet)

        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)
            pygame.draw.circle(screen, BLACK, enemy.center, 5)

        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)

        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (650, 20))

    else:
        text = font.render("GAME OVER", True, RED)
        result = font.render(f"Your score: {score}", True, WHITE)

        screen.blit(text, (310, 250))
        screen.blit(result, (310, 300))

    pygame.display.flip()

pygame.quit()