#import statement to import datetime,random,csv,pandas modules
import datetime,random,csv,pandas

# gameValueGen method to generate the Game_ID, Player_id points, dates and then save on csv format
def gameValueGen():

    # with function is used for file handling
    with open('Game_score.csv','w') as f:
        write=csv.writer(f)
        # these field is used for header of csv data
        write.writerow(["Game_ID", "Player_ID", "Points", "Dates"])

        for i in range(1,30): # for statement to generate the date 1 to 30
            date = datetime.datetime(2021, 8, i)

            # if statement to check the date is not tuesdays
            if date.isoweekday() != 2:

                # for statement to generate the game 1 to 5
                for game_for in range(1,6):

                    for player_for in range(1,random.randrange(75,126)):
                        points = random.randrange(75, 201)
                        write.writerow([str(game_for),str(player_for),str(points),str(date.date())])

            else: # else is ignore tuesdays
                pass

def findOut_top5():

    # with function is used for file handling
    with open('Game_score.csv','r') as f:

        # To read the csv file using pandas module.
        read=pandas.read_csv(f)
        print("Finded the top 5 players on each game :")

        # this for loop session is used for to produced the top 5 player on each game
        for i in range(1,6):
            Game_ID_Values=read[read['Game_ID'] == i]
            rows=Game_ID_Values.sort_values(by=['Points'],ascending=False)
            print(rows.iloc[0:5,:])

        print(" ")
        print("Finded the buttom 5 players on each game :")

        # this for loop session is used for to produced the buttom 5 player on each game
        for i in range(1, 6):
            Game_ID_Values = read[read['Game_ID'] == i]
            rows = Game_ID_Values.sort_values(by=['Points'], ascending=True)
            print(rows.iloc[0:5, :])

gameValueGen()
findOut_top5()