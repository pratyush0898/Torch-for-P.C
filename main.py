import pygame
import sys

pygame.init()

# Set display flags for a resizable window
flags = pygame.RESIZABLE

# Create a Pygame screen (window)
screen = pygame.display.set_mode((800, 600), flags)
pygame.display.set_caption("Resizable Window Example")

# Initialize background color and torch color
background_color = (0, 0, 0)  # Initial background color is black
torch_color = (255, 255, 255)  # Initial torch color is white

# Load the torch image with transparency (white torch)
torch_image = pygame.image.load("torch.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            # Handle window resize event
            screen = pygame.display.set_mode((event.w, event.h), flags)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Toggle fullscreen
                if screen.get_flags() & pygame.FULLSCREEN:
                    screen = pygame.display.set_mode((800, 600), flags)
                else:
                    screen = pygame.display.set_mode((800, 600), flags | pygame.FULLSCREEN)
            elif event.key == pygame.K_b:
                # Change background to black
                background_color = (0, 0, 0)
                # Set torch color to white when background is black
                torch_color = (255, 255, 255) if torch_color == (0, 0, 0) else torch_color
            elif event.key == pygame.K_w:
                # Change background to white
                background_color = (255, 255, 255)
                # Set torch color to black when background is white
                torch_color = (0, 0, 0) if torch_color == (255, 255, 255) else torch_color
            elif event.key == pygame.K_t:
                # Toggle torch color between black and white
                torch_color = (255, 255, 255) if torch_color == (0, 0, 0) else (0, 0, 0)

    # Update game state here

    # Draw on the screen
    screen.fill(background_color)

    # Get the center position of the screen
    screen_center = screen.get_rect().center

    # Scale torch image based on the screen size and reduce its size
    scale_factor = min(screen.get_width() / (torch_image.get_width() * 2), screen.get_height() / (torch_image.get_height() * 2))
    torch_image_scaled = pygame.transform.scale(torch_image, (int(torch_image.get_width() * scale_factor), int(torch_image.get_height() * scale_factor)))

    # Get the rect of the scaled torch image
    torch_rect = torch_image_scaled.get_rect(center=screen_center)

    # Apply color mask to the torch image based on alpha channel
    torch_image_masked = torch_image_scaled.copy()
    torch_image_masked.fill(torch_color, special_flags=pygame.BLEND_RGB_MULT)

    # Draw the torch image
    screen.blit(torch_image_masked, torch_rect.topleft)

    pygame.display.flip()
