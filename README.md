# GreedySession

The above program will calculate the total and Valid Sessions per user.

Logic - 

1.Group the whole data with respect to a praticulat user i.e.find out all the session created by a particular User.

2.Sort the resulting data with respect to date and time object.

3.Search for the first occurance of the Event "ggstart".

4.Store the first occurance object of "ggstart" in previous event and then start iterating to find another event.

5.Check the time difference between current and previous event :-
  
      i. if the time difference is less than 30 than include the event in current session.
  
      ii.If time difference is greater than 30 than do the following :-
   
         a. check if the previous and current event is "ggstop" - > then break the session.
   
         b. check if the previous session was "ggstop" and current session is "ggstart"
                 -> then break the session.
   
         c. check if the previous and current session both are "ggstart" -> then break the session.
   
         d. else continue.
   
6 total_session_time is calculated by mesureing the time difference between start event and end event.

    a. If the session time is greater than 60 then it is considered valid session.
  
    b. If the session time is greater than 1 and smaller than 60 then it is considered invalid session.
  
7.Average session time is calculated by taking (total_session_time/valid_session).

#User Insight

    1. There are a total of 17419 user for 20 different gmes.
  
    2.A maximum number of 11495 users play the game with game_id = 10655435.
  
    3.Sdk version 7.6 is the most popular version used by a majority of users.
  
#Data Discrepancies
  
- >Unused attributes can be omitted from the dataset for example :-
         
- >Attributes debug, random, and params are not required because they are empty most of time.

#Runing the Code

- > run the file model.py and check your result in Output.txt

- > python model.py > output.txt
