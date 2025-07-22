import sqlite3
def main():
    con = sqlite3.connect("webcomics.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS comic(title, genre, rating, chapters_out, chapters_read)")

    # cur.execute("""
    # INSERT INTO comic VALUES \
    # ("Solo Leveling", "Dungeons/systems", 8.63, 200, 200),
    # ("The Lone Necromancer", "Dungeons/systems", 7.09, 146, 187)
    # """)

    # cur.execute("""
    # DELETE FROM comic
    # WHERE rowid NOT IN (
    #     SELECT MIN(rowid)
    #     FROM comic
    #     GROUP BY title
    # );
    # """)

    resp_val = 0
    print("Welcome to the webcomic database. What would you like to do?")
    while resp_val != 5:
        print("1. View comics\n2. Add comic\n3. Edit comic\n4. Remove comic\n5. Exit")
        response = input("Response: ")
        while True:
            try:
                resp_val = int(response)
                break
            except ValueError:
                print("Please enter a valid number. Try again. ")
                response = input("Response: ")
        if resp_val == 1:
            print("How would you like to sort your comics?")
            print("1. Title\n2. Genre\n3. Rating\n4. Chapters Released\n5. Chapters Read")
            sort = input("Response: ")
            while True:
                try:
                    sort_val = int(sort)
                    break
                except ValueError:
                    print("Please enter a valid number. Try again. ")
                    sort = input("Sorting Choice: ")
            if sort_val == 1:
                sort_asc = getSortType()
                if sort_asc == 1:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY title ASC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY title ASC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY title ASC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY title ASC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY title ASC"):
                            print(row)
                    else:
                        print("That was not a valid option. Returning to menu.")
                        continue
                elif sort_asc == 2:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY title DESC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY title DESC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY title DESC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY title DESC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY title DESC"):
                            print(row)
                    else:
                        print("That was not a valid option. Returning to menu.")
                        continue
                else:
                    print("That was not a valid option. Returning to menu.")
                    continue
            elif sort_val == 2:
                sort_asc = getSortType()
                if sort_asc == 1:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY genre ASC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY genre ASC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY genre ASC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY genre ASC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY genre ASC"):
                            print(row)
                elif sort_asc == 2:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY genre DESC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY genre DESC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY genre DESC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY genre DESC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY genre DESC"):
                            print(row)
                else:
                    print("That was not a valid option. Returning to menu.")
                    continue
            elif sort_val == 3:
                sort_asc = getSortType()
                if sort_asc == 1:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY rating ASC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY rating ASC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY rating ASC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY rating ASC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY rating ASC"):
                            print(row)
                elif sort_asc == 2:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY rating DESC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY rating DESC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY rating DESC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY rating DESC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY rating DESC"):
                            print(row)
                else:
                    print("That was not a valid option. Returning to menu.")
                    continue
            elif sort_val == 4:
                sort_asc = getSortType()
                if sort_asc == 1:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY chapters_out ASC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY chapters_out ASC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY chapters_out ASC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY chapters_out ASC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY chapters_out ASC"):
                            print(row)
                elif sort_asc == 2:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY chapters_out DESC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY chapters_out DESC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY chapters_out DESC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY chapters_out DESC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY chapters_out DESC"):
                            print(row)
                else:
                    print("That was not a valid option. Returning to menu.")
                    continue
            elif sort_val == 5:
                sort_asc = getSortType()
                if sort_asc == 1:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY chapters_read ASC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY chapters_read ASC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY chapters_read ASC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY chapters_read ASC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY chapters_read ASC"):
                            print(row)
                elif sort_asc == 2:
                    filter_val = getFilterChoice()
                    if filter_val == 1:
                        desired_genre = input("What is the genre you would like to look at? ")
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE genre = ? ORDER BY chapters_read DESC", (desired_genre,)):
                            print(row)
                    elif filter_val == 2:
                        desired_rating = float(input("What would you like the rating to be at or above? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE rating > ? ORDER BY chapters_read DESC", (desired_rating,)):
                            print(row)
                    elif filter_val == 3:
                        desired_chaps_out = int(input("How many chapters would you like to have been released already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_out > ? ORDER BY chapters_read DESC", (desired_chaps_out,)):
                            print(row)
                    elif filter_val == 4:
                        desired_chaps_read = int(input("How many chapters would you like to have read already? "))
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic WHERE chapters_read > ? ORDER BY chapters_read DESC", (desired_chaps_read,)):
                            print(row)
                    elif filter_val == 5:
                        for row in cur.execute("SELECT title, genre, rating, chapters_out, chapters_read" \
                        " FROM comic ORDER BY chapters_read DESC"):
                            print(row)
                else:
                    print("That was not a valid option. Returning to menu.")
                    continue
            else:
                print("That was not a valid option. Returning to menu.")
                continue
        elif resp_val == 2:
            title = input("What is the title of your new comic? ")
            genre = input("what is the genre of your new comic? ")
            rating = input("What is the MAL rating of your new comic? ")
            while True:
                try:
                    rating_val = float(rating)
                    break
                except ValueError:
                    print("Please enter a valid rating. Try again. ")
                    rating = input("Comic Rating: ")
            chaps_out = input("How many chapters are out for your new comic? ")
            while True:
                try:
                    released_val = int(chaps_out)
                    break
                except ValueError:
                    print("Please enter a valid number of chapters. Try again. ")
                    chaps_out = input("Chapters Released: ")
            chaps_read = input("How many chapters have you read of your new comic? ")
            while True:
                try:
                    read_val = int(chaps_read)
                    break
                except ValueError:
                    print("Please enter a valid number of chapters. Try again. ")
                    chaps_read = input("Chapters Read: ")
            cur.execute("""
            INSERT INTO comic (title, genre, rating, chapters_out, chapters_read)
            VALUES (?, ?, ?, ?, ?)
            """, (title, genre, rating_val, released_val, read_val))
            print("Comic successfully added!")
        elif resp_val == 3:
            title_to_edit = input("What is the title of the comic you would like to edit information for? ")
            new_genre = input("What is the genre you would like to change the comic to? ")
            new_rating = input("What is the new rating you would like to give the comic? ")
            while True:
                try:
                    new_rating_val = float(new_rating)
                    break
                except ValueError:
                    print("Please enter a valid rating. Try again. ")
                    new_rating = input("Comic Rating: ")
            new_chaps_out = input("What is the new number of chapters released? ")
            while True:
                try:
                    new_chaps_out_val = int(new_chaps_out)
                    break
                except ValueError:
                    print("Please enter a valid number of chapters. Try again. ")
                    new_chaps_out = input("Chapters Out: ")
            new_chaps_read = input("What is the new number of chapters that you have read? ")
            while True:
                try:
                    new_chaps_read_val = int(new_chaps_read)
                    break
                except ValueError:
                    print("Please enter a valid number of chapters. Try again. ")
                    new_chaps_read = input("Chapters Read: ")
            cur.execute("""
            UPDATE comic
            SET genre = ?, rating = ?, chapters_out = ?, chapters_read = ?
            WHERE title = ?
            """, (new_genre, new_rating_val, new_chaps_out_val, new_chaps_read_val, title_to_edit))
            print("Comic sucessfully updated!")
        elif resp_val == 4:
            title_to_delete = input("What is the title of the comic you would like to remove from the database? ")
            cur.execute("""
            DELETE FROM comic
            WHERE title = ?
            """, (title_to_delete,))
            print("Comic sucessfully deleted!")
        elif resp_val == 5:
            break
        else:
            print("That number was not a valid option. Please try again. ")
            continue

    con.commit()
    con.close()

def getSortType():
    print("What order would you like to sort your comics in? ")
    print("1. Ascending order\n2. Descending order")
    sort_asc = input("Sorting Type: ")
    while True:
        try:
            asc_val = int(sort_asc)
            break
        except ValueError:
            print("Please enter a valid number. Try again. ")
            sort_asc = input("Sorting Type: ")
    return asc_val

def getFilterChoice():
    print("How would you like to filter your comics? ")
    print("1. Genre\n2. Rating\n3. Chapters Released\n4. Chapters Read\n5. No Filter")
    filter = input("Response: ")
    while True:
        try:
            resp_filter = int(filter)
            break
        except ValueError:
            print("Please enter a valid number. Try again. ")
            filter = input("Filtering Choice: ")
    return resp_filter



if __name__ == "__main__":
    main()