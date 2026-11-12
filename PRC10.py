# We define a class to act as our Tree Node
class PlayerNode:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.left = None
        self.right = None

class PacManLeaderboard:
    def __init__(self):
        self.root = None
        
    def add_score(self, name, score):
        # If leaderboard is empty, this player becomes the root
        if self.root is None:
            self.root = PlayerNode(name, score)
            print(f"Added {name} as the first score!")
        else:
            self._insert(self.root, name, score)
            
    def _insert(self, current_node, name, score):
        # If score is smaller, it goes to the left branch
        if score < current_node.score:
            if current_node.left is None:
                current_node.left = PlayerNode(name, score)
                print(f"Added {name} with score {score}.")
            else:
                self._insert(current_node.left, name, score)
        # If score is bigger (or equal), it goes to the right branch
        else:
            if current_node.right is None:
                current_node.right = PlayerNode(name, score)
                print(f"Added {name} with score {score}.")
            else:
                self._insert(current_node.right, name, score)

    def display_leaderboard(self):
        print("\n--- PAC-MAN HALL OF FAME ---")
        # We use Right-Root-Left traversal to get descending order (Highest first)
        self._reverse_inorder(self.root)
        print("----------------------------\n")

    def _reverse_inorder(self, node):
        if node is not None:
            self._reverse_inorder(node.right)      # Go to largest scores first
            print(f"Player: {node.name} | Score: {node.score}")
            self._reverse_inorder(node.left)       # Then go to smaller scores

# --- Main Program with User Input ---
if __name__ == "__main__":
    game_board = PacManLeaderboard()
    
    while True:
        print("1. Add a New Pac-Man Score")
        print("2. View Leaderboard")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            player_name = input("Enter player name: ")
            player_score = int(input("Enter player score: "))
            game_board.add_score(player_name, player_score)
            print("-" * 30)
            
        elif choice == '2':
            game_board.display_leaderboard()
            
        elif choice == '3':
            print("Game Over. Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")
'''
1. Add a New Pac-Man Score
2. View Leaderboard
3. Exit
Enter your choice (1/2/3): 1
Enter player name: Om
Enter player score: 23000
Added Om as the first score!
------------------------------
1. Add a New Pac-Man Score
2. View Leaderboard
3. Exit
Enter your choice (1/2/3): 2

--- PAC-MAN HALL OF FAME ---
Player: Om | Score: 23000
----------------------------

1. Add a New Pac-Man Score
2. View Leaderboard
3. Exit
Enter your choice (1/2/3): 3
Game Over. Exiting...
'''