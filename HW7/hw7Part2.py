'''
This program asks a user for multiple imputs and choses the best and worst movie that falls within the inputed criteria. 
Kelly Steele 4/12/2018
'''
#inputing,opening, and reading files for data
import json

movies = json.loads(open("movies.json").read())
ratings = json.loads(open("ratings.json").read())

#ask user for various inputs
min_year=int(input("Min year => "))
print(min_year)
max_year=int(input("Max year => "))
print(max_year)
weight_imdb=(input("Weight for IMDB => "))
print(weight_imdb)
weight_imdb=float(weight_imdb)
weight_twitter=(input("Weight for Twitter => "))
print(weight_twitter)
weight_twitter=float(weight_twitter)
print('')
    
genre='yeeeet' #starting the while loop
            
while genre.lower()!='stop': #as long as the user does not input stop, the loop continues
    genre=input("What genre do you want to see? ") #user is asked for genre
    print(genre)
        
    in_year=[] #keeps track of movies following criteria
    for i in movies: #iterates through all possible movies
        if movies[i]['movie_year']<=max_year and movies[i]['movie_year']>=min_year and genre.title() in movies[i]['genre']:
            in_year.append(i) #adds to in_year
            
    if len(in_year)>0: #if there are movies to chose from, ratings are determined
        movies_and_ratings=[] #stores worst movie rating, code, and name
        for i in in_year:
            if i in ratings: #checks for twitter rating
                if len(ratings[i])>2: #ensures at least 3 twitter ratings
                    average_twitter_rating=sum(ratings[i])/len(ratings[i]) #creates twitter average
                    imdb_rating=movies[i]['rating'] #finds imdb rating
                    weighted_rating=(weight_imdb* imdb_rating + weight_twitter * average_twitter_rating)/(weight_imdb+weight_twitter) #uses weights to create weighted rating
                    movies_and_ratings.append((weighted_rating,movies[i]['name'],i)) #adds movie and rating to list
        movies_and_ratings=sorted(movies_and_ratings,reverse=True) #sorts for best movie
        if len(movies_and_ratings)>0: #ensures twitter ratings didnt rule out all possibilies
            best_i=movies_and_ratings[0][2] #dtermines best movie code
            
            print('\nBest:\n\tReleased in {}, {} has a rating of {:.2f}\n'.format(movies[best_i]['movie_year'],movies[best_i]['name'],movies_and_ratings[0][0])) #prints best movie
                          
            movies_and_ratings=sorted(movies_and_ratings) #resorts in opposite order to find worst rating
    
            worst_i=movies_and_ratings[0][2] #determines worst movie code
            print('Worst:\n\tReleased in {}, {} has a rating of {:.2f}\n'.format(movies[worst_i]['movie_year'],movies[worst_i]['name'],movies_and_ratings[0][0])) #prints worst movie
        else: 
            print("\nNo {} movie found in {} through {}\n".format(genre.title(),min_year,max_year)) #prints if no movie found for criteria
                            
    elif len(in_year)==0 and genre.lower()!='stop':
        print("\nNo {} movie found in {} through {}\n".format(genre.title(),min_year,max_year)) #prints if no movie found for criteria
    
            
        
    
    
    
    
