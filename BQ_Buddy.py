# Book Quote Buddy Code in Place Final Project (Name is not final yet)
# Since we already know that we are using the random library, let's import random first
import random
# First, we need an opening message

print()
print()
print("Welcome to Book Quote Buddy!")
print("*" * 30)
print("*" * 30)
print()
print()

# My plan is to have the first prompt to ask the user if they would like to see a quote that is randomly generated.

# First we create a list of really good quotes that we can generate randomly.
# Let's create an empty list first.

author_quote = []
# Then let's populate the list. I did it this way so that it's easier to add more quotes to the list in the future.
# We need to keep track of the authors so that we can use that information for the quiz later on. 

# The quotes from index 0 - 8 are from C.S. Lewis
author_quote.append("Courage, dear heart.") # index 0
author_quote.append("Remember that all world draw to an end and that noble death is a treasure which no one is too poor to buy.")
author_quote.append("For what you see and hear depends a good deal on where you are are standing: it also depends on what sort of person you are.")
author_quote.append("This was the very reason why you were brought to Narnia, that by knowing me here for a little, you may know me better there.")
author_quote.append("One day you will be old enough to start reading fairytales again.")
author_quote.append("Crying is all right in its way while it lasts, but you can't go on crying forever.")
author_quote.append("Every year you grow, you will find me bigger.")
author_quote.append("All get what they want; they do not always like it. - The Magician's nephew ")
author_quote.append("'Strange things do happen sometimes,' said Edmund Pevensie cautiously. 'But they don't happen all the time.'") # index 8
# The quotes from index 9 - 27 are from Paulo Coelho
author_quote.append("There is only one thing that makes a dream impossible to achieve: the fear of failure.") #index 9
author_quote.append("And, when you want something, all the universe conspires in helping you to achieve it.")
author_quote.append("It's the possibility of having a dream come true that makes life interesting")
author_quote.append("One is loved because one is loved. No reason is needed for loving.")
author_quote.append("When we love, we always strive to become better than we are. When we strive to become better than we are, everything around us becomes better too.")
author_quote.append("If you're brave enough to say goodbye, life will reward you with a new hello.")
author_quote.append("The secret of life, though, is to fall seven times and to get up eight times.")
author_quote.append("Remember that wherever your heart is, there you will find your treasure.")
author_quote.append("It's the simple things in life that are the most extraordinary; only wise men are able to understand them.")
author_quote.append("The world is changed by your example, not by your opinion.")
author_quote.append("Insanity is the only sane reaction to an insane world.")
author_quote.append("Anyone who lives in their own world is crazy. Like schizophrenics, psychopaths, maniacs. I mean people who are different from others.")
author_quote.append("If only everyone could know and live with their inner craziness. Would the world be a worse place for it? No, people would be fairer and happier.")
author_quote.append("Life is a gift, and it's up to us to make the most of it.")
author_quote.append("The danger of an adventure is worth a thousand days of ease and comfort")
author_quote.append("I realized that despite the risks, living is the one and only way to experience the wonders of life.")
author_quote.append("If one day I could get out of here, I would allow myself to be crazy. Everyone is indeed crazy, but the craziest are the ones who don't know they're crazy; they just keep repeating what others tell them to.")
author_quote.append("I want to continue being crazy; living my life the way I dream it, and not the way the other people want it to be.")
author_quote.append("And the craziest thing of all is that people are afraid of being different. Why? They are afraid of being ostracized, of being ridiculed and rejected.") # index 27
# The quotes from index 28 - 38 is from JK Rowling
author_quote.append("It is our choices, Harry, that show what we truly are, far more than our abilities.") #index 28
author_quote.append("Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.")
author_quote.append("Fear of a name only increases fear of the thing itself.")
author_quote.append("It does not do to dwell on dreams and forget to live." )
author_quote.append("There's no point getting all worked up about what we can't control.")
author_quote.append("You can't buy friends with good deeds and money.")
author_quote.append("Friends are the family you choose.")
author_quote.append("It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.")
author_quote.append("I solemnly swear that I am up to no good.")
author_quote.append("Fear of a name only increases fear of the thing itself.")
author_quote.append("You have a right to a little foolishness.") #index 38
# The quotes from 39 - 48 is from Stephen King
author_quote.append("Monsters are real, and ghosts are real too. They live inside us, and sometimes, they win.") #index 39
author_quote.append("We make up horrors to help us cope with the real ones.")
author_quote.append("Get busy living or get busy dying.")
author_quote.append("Life is like a wheel. It's always turning, and on comes good times and bad times. But keep on turning, and you'll get back to the good times.")
author_quote.append("If being a kid is about learning how to live, then being a grown-up is about learning how to die.")
author_quote.append("The trust of the innocent is the liar's most useful tool.")
author_quote.append("Sometimes the bad guys are your heroes in disguise." )
author_quote.append("It is better to be good than evil, but one achieves goodness at a terrific cost.")
author_quote.append("They're animals, all right. But why are you so goddam sure that makes us human beings?")
author_quote.append("You can never truly escape your past, no matter how far you walk.") #index 48
# The quotes from index 49 - 58 is from Neil Gaiman
author_quote.append("A book is a dream that you hold in your hands.") #index 49
author_quote.append("That which is dreamed can never be lost, can never be undreamed.")
author_quote.append("Stories are the bridges between us. They are the things that make us human.")
author_quote.append("Being brave doesn't mean you aren't scared. Being brave means you are scared, really scared, badly scared, and you do the right thing anyway.")
author_quote.append("Sometimes you wake up. Sometimes the fall kills you. And sometimes, when you fall, you fly.")
author_quote.append("Life is a disease: sexually transmitted, and invariably fatal.")
author_quote.append("There are so many fragile things, after all. People break so easily, and so do dreams and hearts." )
author_quote.append("Every town needs a bookstore. It holds the potential for information and for joy.")
author_quote.append("I mean, maybe I am crazy. I mean, maybe. But if this is all there is, then I don't want to be sane." )
author_quote.append("He had noticed that events were cowards: they didn't occur singly, but instead they would run in packs and leap out at him all at once.") #index 58
# The quotes from index 59 - 66 is from Jane Austen
author_quote.append("There is a stubbornness about me that never can bear to be frightened at the will of others.") #index 59
author_quote.append("The more I know of the world, the more I am convinced that there are elderly people of good sense almost as often as young ones.")
author_quote.append("A lady's imagination is very rapid; it jumps from admiration to love, from love to matrimony in a moment.")
author_quote.append("I always say that if you can take to people with little faults and weaknesses, you make a good friend.")
author_quote.append("My good opinion once lost is lost forever.")
author_quote.append("To be fond of dancing was a certain step towards falling in love.")
author_quote.append("Society can be terribly unjust in its judgments.")
author_quote.append("I could easily forgive his pride, if he had not mortified mine.") #index 66
# The quotes from index 67 to 77 is from Haruki Murakami
author_quote.append("I am all alone, but I am not lonely. It is a strange sensation, a comfortable loneliness.") # index 67
author_quote.append("A certain solitude is unavoidable in life.")
author_quote.append("You can never lose anything if you are alone. But you can lose yourself if you love someone.")
author_quote.append("Pain is inevitable. Suffering is optional." )
author_quote.append("Time seems to accelerate as you get older. Days feel like hours and hours feel like minutes.")
author_quote.append("It is the process of searching, rather than the finding, that makes a journey meaningful.")
author_quote.append("If you remember me, then I don't care if everyone else forgets.")
author_quote.append("The heartaches we suffer from young love are like the measles in childhood, they leave behind a lifelong immunity.")
author_quote.append("It is said that solitude is a prerequisite for true creativity.")
author_quote.append("Human lives are not mountains. They are waves. In a broad sense, they all flow in the same direction—towards death. But in detail, each life has its own twists and turns, its own highs and lows, its own eddies and whirlpools.")
author_quote.append("Even if nobody remembers you, even if nobody thinks of you, you have still lived your life to the very end. That is something nobody can take away from you.") #index 77
# The quotes from index 78 - 84 are from J.R.R. Tolkien
author_quote.append("The world is indeed full of peril, and in every wood there lurks danger. But there is also beauty.") #index 78
author_quote.append("All that is gold does not glitter, not all those who wander are lost.")
author_quote.append("Faithless is he that says farewell when the road darkens.")
author_quote.append("The world is changed by your example, not by your opinion.")
author_quote.append("It is useless to meet revenge with revenge; it will heal nothing.")
author_quote.append("Even the smallest person can change the course of the future.")
author_quote.append("Many that live deserve death. And some that die deserve life. Can you give it to them? Then do not be too eager to deal out death in judgement. For even the very wise cannot see all ends.") #index 84
# The quotes from index 85 - 90 are from Mark Haddon
author_quote.append("And sometimes I worry that all the people who seem happy all the time are really only pretending.") #index 85
author_quote.append("The more I learn about the world, the more it seems to me that everything is a mystery, and maybe all grown-ups are a bit like me and don't actually know how the world works at all.")
author_quote.append("Sometimes we get sad about things and we don't like to tell other people that we are sad about them. We like to keep it a secret. Or sometimes, we are sad but we really don't know why we are sad, so we say we aren't sad but we really are.")
author_quote.append("Maybe it's not about finding the answers, but learning how to live with the questions.")
author_quote.append("Hope is a dangerous thing. It can keep you going, but it can also lead you astray.")
author_quote.append("Sometimes the truth isn't what matters. Sometimes what matters is the story you tell yourself.") # index 90
# The quotes from index 91 - 98 are from john green
author_quote.append("My thoughts are stars I cannot fathom into constellations.") #index 91
author_quote.append("That's the thing about pain though. It demands to be felt.")
author_quote.append("We do not read books to escape reality; we read to create it.")
author_quote.append("Maybe there are infinite versions of us, and in some of them, we are happy.")
author_quote.append("And you know, maybe the reason we memorize the words to all those songs, the reason we keep singing them, is because we don't really know what the future holds. So we sing these songs to feel a little more anchored, a little more connected.")
author_quote.append("Sometimes, putting distance between yourself and the people you love is the only way to save the love.")
author_quote.append("You gave me a forever within the numbered days, and I'm grateful.")
author_quote.append("You don't get to choose if you get hurt in this world...but you do have some say in who hurts you. I like my choices.") #index 98



# We need the length of the list as a range when coming up with a random number
length_of_author_quote = len(author_quote) 



# Now that we have a list of quotes that we can generate ranomly, we can now ask the user if they want to see a quote.
# This idea and this program is a gift for my wife. So I actually asked her for some author names and I used those to search for quotes. Which is why the prompt mentions favourite book.
while play_again:
    first_prompt = input("Would you like to see a quote from your favourite book? (y or n): ")
    print()
    print()
    
    if first_prompt == "y":
        random_quote_number = random.randint(0,length_of_author_quote)
       
       # This is how we know which author is the correct one.
    
        cs_lewis = 0 <= random_quote_number <= 8
        p_coelho = 9 <= random_quote_number <= 27
        jk_rowling = 28 <= random_quote_number <38
        s_king = 38 <= random_quote_number <= 48
        n_gaiman = 49 <= random_quote_number <= 58
        j_austen = 59 <= random_quote_number <= 66
        h_murakami = 67 <= random_quote_number <= 77
        jrr_tolkien = 78 <= random_quote_number <= 84
        m_haddon = 85 <= random_quote_number <= 90
        j_green = 91 <= random_quote_number <=98
    
        print(author_quote[random_quote_number])
        for i in range(3):
            print()
    
        # After we show the user a quote that is randomly generated, we ask if the user wants to play a game where they can try to guess the author.
        # This is the tricky part.
    
        game = input("Would you like to guess the author for this quote? (y or n): ")
        if game == "y":
            
            # I used the index number information to create conditions with booleans so that the program knows which author is the correct one.
            if cs_lewis:
                author = "C.S. Lewis"
            elif p_coelho:
                author = "Paulo Coelho"
            elif jk_rowling:
                author = "J.K. Rowling"
            elif s_king:
                author = "Stephen King"
            elif n_gaiman:
                author = "Neil Gaiman"
            elif j_austen:
                author = "Jane Austen"
            elif h_murakami:
                author = "Haruki Murakami"
            elif jrr_tolkien:
                author = "J.R.R. Tolkien"
            elif m_haddon:
                author = "Mark Haddon"
            elif j_green:
                author = "John Green"
    
            # For this section, I created 4 random lists. The author names are inside the 4 different lists, but spread out along with random author names that are not actually quoted.
    
            # For each list, the program will check if the correct author is in the list, if it is, that option will be the correct one.
            # If it's not in the list, it will generate a different random author that is not the correct answer as part of the Multiple Choice Question.
            
            list_for_mcq1 = ["Stephen King", "Neil Gaiman", "J.R.R. Tolkien", "Mark Haddon","Suzanne Collins", "Ernest Cline", "Orson Scott Card"]
            list_for_mcq2 = ["Dan Brown" , "Paulo Coelho", "James Rollins", "J.K. Rowling", "Charlotte Bronte", "Matt Haig", "Salman Rushdie"]
            list_for_mcq3 = ["C.S. Lewis", "Sir Arthur Conan Doyle", "Jane Austen", "John Green", "John Grisham","Nicholas Sparks", "F. Scott Fitzgerald"]
            list_for_mcq4 = ["Harlan Coben", "Haruki Murakami", "Khaled Hossaini", "Chuck Palahnuik", "Kazuo Ishiguro", "Gabriel Garcia Maruez"]
            
    
            if author in list_for_mcq1:
                print()
                print("Who do you think is the author of this quote?")
                print()
                print("a. " + author)
                length_of_mcq_answers2 = len(list_for_mcq2)
                length_of_mcq_answers3 = len(list_for_mcq3)
                length_of_mcq_answers4 = len(list_for_mcq4)
                random_author2 = list_for_mcq2[random.randint(0,length_of_mcq_answers2-1)]
                print("b. " + random_author2)
                random_author3 = list_for_mcq3[random.randint(0,length_of_mcq_answers3-1)]
                print("c. " + random_author3)
                random_author4 = list_for_mcq4[random.randint(0,length_of_mcq_answers4-1)]
                print("d. " + random_author4)
                user_guess = input("answer either a, b, c or d: ")
    
                if user_guess == "a":
                    print("Correct!")
                    print()
                    print()
                    print()
                    print("Thank you for playing!")
                else:
                    print()
                    print()
                    print("Incorrect!")
                    print()
                    print("The author of this quote is " + author + ".")
                    print("That was a good try! Thank you for playing")
                    print()
                    print()
    
            # The program ends like this. I did not put an endless loop to the program. I prefer it this way. If the user would like to try the quote engine again, the program has to be restarted.
    
            elif author in list_for_mcq2:
                print()
                print("Who do you think is the author of this quote?")
                print()
                length_of_mcq_answers1 = len(list_for_mcq1)
                length_of_mcq_answers3 = len(list_for_mcq3)
                length_of_mcq_answers4 = len(list_for_mcq4)
                random_author1 = list_for_mcq1[random.randint(0,length_of_mcq_answers1-1)]
                print("a. " + random_author1)
                
                print("b. " + author)
                random_author3 = list_for_mcq3[random.randint(0,length_of_mcq_answers3-1)]
                print("c. " + random_author3)
                random_author4 = list_for_mcq4[random.randint(0,length_of_mcq_answers4-1)]
                print("d. " + random_author4)
    
                user_guess = input("answer either a, b, c or d: ")
    
                if user_guess == "b":
                    print("Correct!")
                    print()
                    print()
                    print()
                    print("Thank you for playing!")
                else:
                    print()
                    print()
                    print("Incorrect!")
                    print()
                    print("The author of this quote is " + author + ".")
                    print("That was a good try! Thank you for playing!")
                    print()
                    print()
    
            # As mentioned before, if the name of the author is in list 1, the first program executes. If it's in list 2, the second program exectes, and so on and so forth. 
            # This is a little primapive and not automated enough for a super simple program, however the randomly generated author names of the multiple choice question allows the game to still be interesting.
    
            elif author in list_for_mcq3:
                print()
                print("Who do you think is the author of this quote?")
                print()
                length_of_mcq_answers1 = len(list_for_mcq1)
                length_of_mcq_answers2 = len(list_for_mcq2)
                length_of_mcq_answers4 = len(list_for_mcq4)
                random_author1 = list_for_mcq1[random.randint(0,length_of_mcq_answers1-1)]
                print("a. " + random_author1)
                random_author2 = list_for_mcq2[random.randint(0,length_of_mcq_answers2-1)]
                print("b. " + random_author2)
                
                print("c. " + author)
                random_author4 = list_for_mcq4[random.randint(0,length_of_mcq_answers4-1)]
                print("d. " + random_author4)
                user_guess = input("answer either a, b, c or d: ")
    
                if user_guess == "c":
                    print("Correct!")
                    print()
                    print()
                    print()
                    print("Thank you for playing!")
                else:
                    print()
                    print()
                    print("Incorrect!")
                    print()
                    print("The author of this quote is " + author + ".")
                    print("That was a good try! Thank you for playing")
                    print()
                    print()
    
            if author in list_for_mcq4:
                print()
                print("Who do you think is the author of this quote?")
                print()
                length_of_mcq_answers1 = len(list_for_mcq1)
                length_of_mcq_answers2 = len(list_for_mcq2)
                length_of_mcq_answers3 = len(list_for_mcq3)
                random_author1 = list_for_mcq1[random.randint(0,length_of_mcq_answers1-1)]
                print("a. " + random_author1)
                random_author2 = list_for_mcq2[random.randint(0,length_of_mcq_answers2-1)]
                print("b. " + random_author2)
                random_author3 = list_for_mcq3[random.randint(0,length_of_mcq_answers3-1)]
                print("c. " + random_author3)
        
                print("d. " + author)
    
                user_guess = input("answer either a, b, c or d: ")
    
                if user_guess == "d":
                    print("Correct!")
                    print()
                    print()
                    print()
                    print("Thank you for playing!")
                else:
                    print()
                    print()
                    print("Incorrect!")
                    print()
                    print("The author of this quote is " + author + ".")
                    print("That was a good try! Thank you for playing")
                    print()
                    print()
    
    
    
    if first_prompt == "n":
        print("Okay! If you would want to see quotes from your favourite book! You know where to find me!")
        print("*" * 30)
        print("*" * 30)
        print()
        print()
    
    play_again = play_again_prompt == "y"
    print("Would you like to see another quote?")
    play_again_prompt = input("answer y or n")
    
    
    
    
    
    
    
    # The program ends when the user answer No to the first prompt. However, by design, you can just restart the program. 
    # Book Quote Buddy is designed to be used once in a while only. Not 2 to 3 hours in one go. It can also be customized to the books and author that you love. It can also be constantly updated and expanded.
