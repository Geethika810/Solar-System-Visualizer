import pygame
import math
import random
# ============================================
# INITIALIZE PYGAME
# ============================================
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Visualizer")
clock = pygame.time.Clock()
FPS = 60
# ============================================
# COLORS
# ============================================
BLACK = (5, 5, 10)
WHITE = (255, 255, 255)
ORBIT_COLOR = (150, 150, 0)
YELLOW = (255, 220, 0)
ORANGE = (255, 120, 20)
BLUE = (40, 120, 255)
GREEN = (40, 180, 70)
RED = (220, 60, 40)
BROWN = (180, 130, 80)
LIGHT_BLUE = (80, 180, 255)
# ============================================
# SUN POSITION
# ============================================
SUN_X = WIDTH // 2
SUN_Y = HEIGHT // 2
# ============================================
# CREATE STAR BACKGROUND
# ============================================
stars = []
for i in range(400):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.choice([1, 1, 1, 2])
    brightness = random.randint(120, 255)
    stars.append(
        (x, y, size, brightness)
    )
# ============================================
# PLANET DATA
# ============================================
planets = [
    {
        "name": "Mercury",
        "distance": 65,
        "radius": 6,
        "color": (170, 170, 170),
        "speed": 0.035,
        "angle": 0
    },
    {
        "name": "Venus",
        "distance": 90,
        "radius": 10,
        "color": (230, 180, 90),
        "speed": 0.028,
        "angle": 1
    },
    {
        "name": "Earth",
        "distance": 125,
        "radius": 12,
        "color": BLUE,
        "speed": 0.020,
        "angle": 2
    },
    {
        "name": "Mars",
        "distance": 155,
        "radius": 9,
        "color": RED,
        "speed": 0.017,
        "angle": 3
    },
    {
        "name": "Jupiter",
        "distance": 205,
        "radius": 25,
        "color": (210, 170, 120),
        "speed": 0.009,
        "angle": 4
    },
    {
        "name": "Saturn",
        "distance": 265,
        "radius": 22,
        "color": (220, 190, 130),
        "speed": 0.007,
        "angle": 5
    },
    {
        "name": "Uranus",
        "distance": 325,
        "radius": 16,
        "color": LIGHT_BLUE,
        "speed": 0.005,
        "angle": 6
    },
    {
        "name": "Neptune",
        "distance": 375,
        "radius": 18,
        "color": (80, 120, 220),
        "speed": 0.004,
        "angle": 0.5
    }
]
# ============================================
# DRAW STAR BACKGROUND
# ============================================
def draw_stars():
    for x, y, size, brightness in stars:
        color = (
            brightness,
            brightness,
            brightness
        )
        pygame.draw.circle(
            screen,
            color,
            (x, y),
            size
        )
# ============================================
# DRAW SUN
# ============================================
def draw_sun():
    # Outer glow
    pygame.draw.circle(
        screen,
        (120, 50, 10),
        (SUN_X, SUN_Y),
        55
    )
    pygame.draw.circle(
        screen,
        (220, 80, 10),
        (SUN_X, SUN_Y),
        48
    )
    pygame.draw.circle(
        screen,
        (255, 140, 20),
        (SUN_X, SUN_Y),
        42
    )
    pygame.draw.circle(
        screen,
        (255, 200, 40),
        (SUN_X, SUN_Y),
        34
    )
    # Small bright areas on Sun
    pygame.draw.circle(
        screen,
        (255, 230, 100),
        (SUN_X - 10, SUN_Y - 10),
        7
    )
    pygame.draw.circle(
        screen,
        (255, 180, 30),
        (SUN_X + 12, SUN_Y + 5),
        6
    )
    pygame.draw.circle(
        screen,
        (255, 240, 120),
        (SUN_X + 3, SUN_Y - 15),
        4
    )
# ============================================
# DRAW EARTH
# ============================================
def draw_earth(x, y, radius):
    # Ocean
    pygame.draw.circle(
        screen,
        (30, 110, 220),
        (x, y),
        radius
    )
    # Land
    pygame.draw.circle(
        screen,
        (40, 170, 80),
        (x - 4, y - 3),
        radius // 2
    )
    pygame.draw.circle(
        screen,
        (60, 190, 80),
        (x + 5, y + 4),
        radius // 3
    )
    # Highlight
    pygame.draw.circle(
        screen,
        (180, 230, 255),
        (x - 4, y - 5),
        2
    )
# ============================================
# DRAW JUPITER
# ============================================
def draw_jupiter(x, y, radius):
    pygame.draw.circle(
        screen,
        (210, 170, 120),
        (x, y),
        radius
    )
    # Jupiter stripes
    pygame.draw.line(
        screen,
        (170, 130, 90),
        (x - radius + 4, y - 10),
        (x + radius - 4, y - 10),
        4
    )
    pygame.draw.line(
        screen,
        (245, 210, 160),
        (x - radius + 3, y),
        (x + radius - 3, y),
        5
    )
    pygame.draw.line(
        screen,
        (160, 120, 80),
        (x - radius + 5, y + 10),
        (x + radius - 5, y + 10),
        4
    )
    # Red spot
    pygame.draw.ellipse(
        screen,
        (180, 90, 60),
        (
            x + 5,
            y + 5,
            10,
            6
        )
    )
# ============================================
# DRAW SATURN
# ============================================
def draw_saturn(x, y, radius):
    # Back part of ring
    pygame.draw.ellipse(
        screen,
        (170, 150, 110),
        (
            x - radius - 15,
            y - 8,
            radius * 2 + 30,
            18
        ),
        5
    )
    # Planet
    pygame.draw.circle(
        screen,
        (220, 190, 130),
        (x, y),
        radius
    )
    # Planet stripes
    pygame.draw.line(
        screen,
        (180, 150, 100),
        (x - radius + 5, y - 5),
        (x + radius - 5, y - 5),
        3
    )
    pygame.draw.line(
        screen,
        (240, 215, 160),
        (x - radius + 5, y + 5),
        (x + radius - 5, y + 5),
        3
    )
    # Front part of ring
    pygame.draw.ellipse(
        screen,
        (200, 180, 130),
        (
            x - radius - 15,
            y - 8,
            radius * 2 + 30,
            18
        ),
        3
    )
# ============================================
# DRAW NORMAL PLANET
# ============================================
def draw_planet(planet, x, y):
    name = planet["name"]
    radius = planet["radius"]
    color = planet["color"]
    if name == "Earth":
        draw_earth(
            int(x),
            int(y),
            radius
        )
    elif name == "Jupiter":
        draw_jupiter(
            int(x),
            int(y),
            radius
        )
    elif name == "Saturn":
        draw_saturn(
            int(x),
            int(y),
            radius
        )
    else:
        pygame.draw.circle(
            screen,
            color,
            (int(x), int(y)),
            radius
        )
        # Highlight
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                int(x - radius * 0.3),
                int(y - radius * 0.3)
            ),
            max(1, radius // 4)
        )
# ============================================
# MAIN LOOP
# ============================================
running = True
while running:
    # ----------------------------------------
    # EVENTS
    # ----------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ----------------------------------------
    # BACKGROUND
    # ----------------------------------------
    screen.fill(BLACK)
    draw_stars()
    # ----------------------------------------
    # DRAW ORBIT CIRCLES
    # ----------------------------------------
    for planet in planets:
        pygame.draw.circle(
            screen,
            ORBIT_COLOR,
            (SUN_X, SUN_Y),
            planet["distance"],
            1
        )
    # ----------------------------------------
    # DRAW SUN
    # ----------------------------------------
    draw_sun()
    # ----------------------------------------
    # DRAW PLANETS
    # ----------------------------------------
    for planet in planets:
        # Update angle
        planet["angle"] += planet["speed"]
        # Calculate position
        x = (
            SUN_X
            + math.cos(planet["angle"])
            * planet["distance"]
        )
        y = (
            SUN_Y
            + math.sin(planet["angle"])
            * planet["distance"]
        )
        # Draw planet
        draw_planet(
            planet,
            x,
            y
        )
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()