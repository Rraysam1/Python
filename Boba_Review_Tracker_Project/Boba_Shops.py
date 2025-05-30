# Boba Review Database
# Ray Sam
# 05-12-2025

# Function to add a new boba review
def add_review():
    print("Leave a new boba review!")  

    # Prompt the user to enter details for the review
    shop = input("Shop name: ")
    drink = input("Drink name: ")
    location = input("Location (city): ") 
    rating = input("Rating (1–5): ")
    comments = input("Any comments? (optional): ")

    
    with open("boba_reviews.txt", "a") as file:                         # Open the file in "append" mode so we don't erase previous reviews
        file.write(f"{drink},{shop},{location},{rating},{comments}\n")  # Save all the details in a single line, separated by commas
    
    print("Review saved!\n")  

# Function to view all saved reviews
def view_reviews():
    print("\nYour Boba Reviews:")

    try:
        # Open the file in "read" mode
        with open("boba_reviews.txt", "r") as file:
            reviews = file.readlines()

        if not reviews:
            print("No reviews available. Please add a review first.\n")
            return  # Exit the function if no reviews are found

        # Display the reviews if available
        for line in reviews:
            # Split line into exactly 5 parts (drink, shop, location, rating, comments)
            parts = line.strip().split(",", 4)
            
            if len(parts) == 5:  # Check if we have all 5 parts
                drink, shop, location, rating, comments = parts
                print(f"- {drink} from {shop} in {location}: {rating}/5 — {comments}")    #Our actual output here
            else:
                print("Error: Missing information. Skipping this review.")

    # If the file doesn't exist yet, catch the error
    except FileNotFoundError:
        print("No reviews found yet. Please add a review first.\n")

# Main program loop — keeps running until the user chooses to exit
def main():
    while True:
        # Display the main menu
        print("\nBoba Rating System")
        print("1. Add a Review")
        print("2. View Reviews")
        print("3. Exit")

        # Ask the user for their choice
        choice = input("Choose an option (1-3): ")

        # Route to the right function based on choice
        if choice == "1":
            add_review()
        elif choice == "2":
            view_reviews()
        elif choice == "3":
            print("Goodbye!")  # Exit message
            break  # Stop the while loop → exits the program
        else:
            print("Invalid choice. Try again.")  # Catch wrong input

# Start the program by calling the main function
main()
