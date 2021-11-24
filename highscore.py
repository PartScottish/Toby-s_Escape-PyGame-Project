#Matthew Laws
#Memor Patris
#10/12/2020

class high_score_persister():
#CONTRIB: Paul Vincent Craven - inspiration for reading/writing the score

    def __init__(self):
        self.high_score = 0
        self.high_score_has_changed = True

    
    def get_high_score(self):       
        if self.high_score_has_changed == True:
            self.high_score_has_changed = False
            # Try to read the high score from a file
            try:
                high_score_file = open("high_score.txt", "r")
                self.high_score = int(high_score_file.read())
                high_score_file.close()
                #print("The high score is", self.high_score)
            except IOError:
                # Error to handle no previous highscore
                print("No Highscore Set.")
            except ValueError:
                # File exists with invalid data format.
                print("I'm confused. Starting with no high score.")
                
        return self.high_score
     
     
    def save_high_score(self, new_high_score):       
        if new_high_score > self.high_score:
            try:
                # Writing the highscore
                high_score_file = open("high_score.txt", "w")
                high_score_file.write(str(new_high_score))
                high_score_file.close()
                self.high_score_has_changed = True
            except IOError:
                # Error handling in the event of not being able to save the highscore
                print("There was an error, highscore not saved.")