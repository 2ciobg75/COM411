# Ask the user if the book cover is hard or soft
print("What type of cover does the book have (soft or hard)?")
book_cover = input()

# If the cover is soft ask the user if it is perfect bound
if book_cover == "soft":
    print("Is the book perfect-bound? (y/n)")
    book_soft = input()
    if book_soft == "y":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")
