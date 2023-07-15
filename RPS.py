import random
import psycopg2
# Connect to the database
conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="heng",
        host="localhost",
        port='5432'
    )
cur = conn.cursor()
# Create a table if it does not exist
cur.execute("CREATE TABLE IF NOT EXISTS scores (name VARCHAR, age INTEGER, wins INTEGER, losses INTEGER)")
# Get the player name and age
print("Fill some info to play:)!!")
name = input("Enter Name: ")
age = int(input("Enter Age: "))

# Check if the player is already in the database
cur.execute("SELECT * FROM scores WHERE name = %s AND age = %s", (name, age))
row = cur.fetchone()

# If not, insert a new row with zero wins and losses
if row is None:
    cur.execute("INSERT INTO scores (name, age, wins, losses) VALUES (%s, %s, 0, 0)", (name, age))
    conn.commit()
    row = (name, age, 0, 0)

# Get the current wins and losses of the player
wins = row[2]
losses = row[3]

print("Welcome", name, "To RPS GAME!!!")
print("=================o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o==================")

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print("Player: ", player)
    print("Computer: ", computer)

    if player == computer:
        print("It's a tieミ⁠●⁠﹏⁠☉⁠ミ!!!")
    elif player == "rock" and computer == "scissors":
        print("You win (⁠つ⁠≧⁠▽⁠≦⁠)⁠つ!!!")
        wins += 1  # Increment the wins by one
    elif player == "paper" and computer == "rock":
        print("You win (⁠つ⁠≧⁠▽⁠≦⁠)⁠つ!!!")
        wins += 1  # Increment the wins by one
    elif player == "scissors" and computer == "paper":
        print("You win (⁠つ⁠≧⁠▽⁠≦⁠)⁠つ!!!")
        wins += 1  # Increment the wins by one
    else:
        print("You lose(⁠-̩̩⁠-̩̩⁠-̩̩⁠-̩̩⁠-̩̩⁠_⁠_⁠_⁠-̩̩⁠-̩̩⁠-̩̩⁠-̩̩⁠-̩̩⁠)!!!")
        losses += 1 
    cur.execute("UPDATE scores SET wins = %s, losses = %s WHERE name = %s AND age = %s", (wins, losses, name, age))
    conn.commit()
    print(f"Your score: {wins} wins, {losses} losses")
    if not input("Play again? y/n:").lower() == "y":
        running = False
print("Thanks for playing!!!!(⁠＾⁠∇⁠＾⁠)⁠ﾉ⁠♪")
cur.close()
conn.close()
