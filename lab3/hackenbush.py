import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Simple Hackenbush Dog")

BG_COLOR = (30, 30, 30)
EDGE_COLOR = (0, 150, 200)
GROUND_COLOR = (100, 50, 0)

def point_key(p):
    return (round(p[0]), round(p[1]))

def build_graph(edges):
    graph = {}
    for e in edges:
        a, b = point_key(e[0]), point_key(e[1])
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph

def find_stable_nodes(graph):
    stable = set()
    for node in graph:
        if node[1] >= 495:
            stable.add(node)
    frontier = list(stable)
    while frontier:
        current = frontier.pop()
        for neighbor in graph.get(current, []):
            if neighbor not in stable:
                stable.add(neighbor)
                frontier.append(neighbor)
    return stable

def edge_is_stable(edge, stable_nodes):
    a, b = point_key(edge[0]), point_key(edge[1])
    return (a in stable_nodes) or (b in stable_nodes)

def draw_edges(edges, stable_nodes):
    for e in edges:
        a, b = e
        color = EDGE_COLOR if (point_key(a) in stable_nodes or point_key(b) in stable_nodes) else (100, 100, 100)
        pygame.draw.line(screen, color, a, b, 5)

def edge_clicked(edge, pos):
    ax, ay = edge[0]
    bx, by = edge[1]
    px, py = pos

    ABx, ABy = bx - ax, by - ay
    APx, APy = px - ax, py - ay

    AB_len_sq = ABx**2 + ABy**2
    if AB_len_sq == 0:
        return False

    t = max(0, min(1, (APx*ABx + APy*ABy) / AB_len_sq))
    closest_x = ax + t * ABx
    closest_y = ay + t * ABy

    dist_sq = (px - closest_x)**2 + (py - closest_y)**2
    return dist_sq < 100

edges = [
    # Legs (to ground)
    [(150, 500), (150, 450)],  # left front leg
    [(150, 450), (160, 430)],

    [(180, 500), (180, 460)],  # right front leg
    [(180, 460), (190, 440)],

    [(250, 500), (250, 460)],  # left back leg
    [(250, 460), (240, 440)],

    [(280, 500), (280, 450)],  # right back leg
    [(280, 450), (270, 430)],

    # Body
    [(160, 430), (270, 430)],  # belly
    [(160, 430), (160, 400)],  # left side body
    [(270, 430), (270, 400)],  # right side body
    [(160, 400), (270, 400)],  # back

    # Neck and head
    [(270, 400), (290, 380)],  # neck
    [(290, 380), (310, 370)],  # head top
    [(310, 370), (320, 380)],  # head front
    [(320, 380), (310, 390)],  # head bottom
    [(310, 390), (290, 400)],  # head back

    # Tail
    [(160, 400), (140, 380)],
    [(140, 380), (130, 370)],
    [(130, 370), (120, 375)],
]

def main():
    current_edges = edges.copy()

    while True:
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, GROUND_COLOR, (0, 495, WIDTH, HEIGHT - 495))

        graph = build_graph(current_edges)
        stable_nodes = find_stable_nodes(graph)

        draw_edges(current_edges, stable_nodes)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_edge = None
                for e in current_edges:
                    if edge_clicked(e, pos):
                        if edge_is_stable(e, stable_nodes):
                            clicked_edge = e
                            break
                if clicked_edge:
                    current_edges.remove(clicked_edge)
                    graph = build_graph(current_edges)
                    stable_nodes = find_stable_nodes(graph)
                    current_edges = [e for e in current_edges if edge_is_stable(e, stable_nodes)]

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
