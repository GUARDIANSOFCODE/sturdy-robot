import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (28, 170, 156)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)

# Board
board = [[None]*3 for _ in range(3)]
CELL_SIZE = WIDTH // 3
FONT = pygame.font.SysFont(None, 100)

# Draw the grid lines
def draw_lines():
    SCREEN.fill(WHITE)
    # Vertical
    pygame.draw.line(SCREEN, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(SCREEN, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    # Horizontal
    pygame.draw.line(SCREEN, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(SCREEN, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

# Draw X or O
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = FONT.render('X', True, X_COLOR)
                SCREEN.blit(text, (col * CELL_SIZE + 60, row * CELL_SIZE + 30))
            elif board[row][col] == 'O':
                text = FONT.render('O', True, O_COLOR)
                SCREEN.blit(text, (col * CELL_SIZE + 60, row * CELL_SIZE + 30))

# Check for winner
def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Check draw
def is_draw():
    return all(all(cell is not None for cell in row) for row in board)

# Reset game
def reset_game():
    global board, current_player
    board = [[None]*3 for _ in range(3)]
    current_player = 'X'
    draw_lines()

# Game loop
draw_lines()
current_player = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] is None:
                board[row][col] = current_player
                if check_winner(current_player):
                    print(f"{current_player} wins!")
                    game_over = True
                elif is_draw():
                    print("Draw!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()
            game_over = False

    draw_lines()
    draw_figures()
    pygame.display.update()
