import time
import pygame
from . import window, gui
from .io.editing_hid import KEYMAPPINGS, EditingHID
from .data import view, editor

TICK_RATE = 144

pygame.init()
window.init()
gui.manager.init()
hid = EditingHID(KEYMAPPINGS, editor.mouse_event)

clock = pygame.time.Clock()
running = True
previous_time = time.time()
while running:

    # delta time
    clock.tick(TICK_RATE)

    dt = time.time() - previous_time
    previous_time = time.time()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        gui.manager.process_event(event)
        hid.process_event(event)
        window.process_event(event)

    hid.process_input()

    # drawing
    window.clear()
    view.blit()
    gui.manager.blit()
    window.refresh()

pygame.quit()
