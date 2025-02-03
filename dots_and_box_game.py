# dash - dot game # goal is to train a neural network and train using reinforcement learning

 display board
def display_board(horizontal_lines, vertical_lines, boxes):
    print('  ' + ' '.join(f"{i}" for i in range(4)))
    
    for r in range(4):
        # Print row number and dots/horizontal lines
        line = [f"{r} "]
        for c in range(4):
            line.append('.')
            if c < 3:
                line.append('-' if (r, c) in horizontal_lines else ' ')
        print(''.join(line))
        
        # Print vertical lines and box numbers between rows
        if r < 3:
            v_line = ['  ']  # Align with row number spacing
            for c in range(4):
                v_line.append('|' if (r, c) in vertical_lines else ' ')
                if c < 3:
                    # assign box name  if exists
                    owner = boxes.get((r, c), ' ')
                    v_line.append(str(owner))
            print(''.join(v_line))

def check_completed_boxes(line_r, line_c, is_horizontal, horizontal_lines, vertical_lines, boxes, current_player):
    new_boxes = []
    
    if is_horizontal:
        # Check box above the line
        if line_r > 0:
            box_r = line_r - 1
            box_c = line_c
            if (box_r, box_c) not in boxes:
                top = (box_r, box_c) in horizontal_lines
                bottom = (box_r+1, box_c) in horizontal_lines
                left = (box_r, box_c) in vertical_lines
                right = (box_r, box_c+1) in vertical_lines
                if top and bottom and left and right:
                    new_boxes.append((box_r, box_c))
        
        # Check box below the line
        if line_r < 3:
            box_r = line_r
            box_c = line_c
            if (box_r, box_c) not in boxes:
                top = (box_r, box_c) in horizontal_lines
                bottom = (box_r+1, box_c) in horizontal_lines
                left = (box_r, box_c) in vertical_lines
                right = (box_r, box_c+1) in vertical_lines
                if top and bottom and left and right:
                    new_boxes.append((box_r, box_c))
    else:
        # Check box to the left of the line
        if line_c > 0:
            box_r = line_r
            box_c = line_c - 1
            if (box_r, box_c) not in boxes:
                top = (box_r, box_c) in horizontal_lines
                bottom = (box_r+1, box_c) in horizontal_lines
                left = (box_r, box_c) in vertical_lines
                right = (box_r, box_c+1) in vertical_lines
                if top and bottom and left and right:
                    new_boxes.append((box_r, box_c))
        
        # Check box to the right of the line
        if line_c < 3:
            box_r = line_r
            box_c = line_c
            if (box_r, box_c) not in boxes:
                top = (box_r, box_c) in horizontal_lines
                bottom = (box_r+1, box_c) in horizontal_lines
                left = (box_r, box_c) in vertical_lines
                right = (box_r, box_c+1) in vertical_lines
                if top and bottom and left and right:
                    new_boxes.append((box_r, box_c))
    
    #  add  boxes and scores
    for box in new_boxes:
        boxes[box] = current_player
    return len(new_boxes)

def main():
    horizontal_lines = set()
    vertical_lines = set()
    boxes = {}
    scores = {1: 0, 2: 0}
    current_player = 1
    total_lines = 24  # 12 horizontal + 12 vertical

    while len(horizontal_lines) + len(vertical_lines) < total_lines:
        display_board(horizontal_lines, vertical_lines, boxes)
        print(f"Player {current_player}'s turn. Current scores: {scores[1]}-{scores[2]}")
        
        while True:
            try:
                start_r, start_c = map(int, input("Enter start dot (row col 0-3): ").split(','))
                end_r, end_c = map(int, input("Enter end dot (row col 0-3): ").split(','))
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
                continue

            # Validate coordinates
            if not all(0 <= x <= 3 for x in [start_r, start_c, end_r, end_c]):
                print("Coordinates must be between 0-3.")
                continue

            # Check adjacency
            if (start_r == end_r and abs(start_c - end_c) == 1) or \
               (start_c == end_c and abs(start_r - end_r) == 1):
                
                # Determine line type
                is_horizontal = (start_r == end_r)
                line_r = start_r if is_horizontal else min(start_r, end_r)
                line_c = min(start_c, end_c) if is_horizontal else start_c
                lines = horizontal_lines if is_horizontal else vertical_lines
                
                # Check if line exists
                if (line_r, line_c) in lines:
                    print("Line already exists!")
                    continue
                
                # Add line
                lines.add((line_r, line_c))
                # Check  completed boxes  and update score 
                num_boxes = check_completed_boxes(line_r, line_c, is_horizontal, 
                                                 horizontal_lines, vertical_lines,
                                                 boxes, current_player)
                scores[current_player] += num_boxes
                break
            else:
                print("Dots must be adjacent horizontally or vertically.")

        # if box completed let current player one more chance or switch to another player  
        if num_boxes == 0:
            current_player = 2 if current_player == 1 else 1

    # Final display and winner
    display_board(horizontal_lines, vertical_lines, boxes)
    print(f" Final score  - Player 1: {scores[1]}, Player 2: {scores[2]}")
    if scores[1] > scores[2]:
        print("Player 1 wins!")
    elif scores[2] > scores[1]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()

