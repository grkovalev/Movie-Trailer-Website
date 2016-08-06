
import video
import fresh_tomatoes

# This code generate a web page with your favourites movies 


# Instance of movie
four_rooms = video.Movie("Four Rooms",
                          120,
                          "https://upload.wikimedia.org/wikipedia/en/c/c8/Four_rooms_ver2.jpg",
                          "https://www.youtube.com/watch?v=Rieq_TR7cV0")

skool_of_rock = video.Movie("School of Rock",
                             109 ,
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

the_fith_element = video.Movie('The Fith Element',
                                126,
                                "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
                                "https://www.youtube.com/watch?v=fQ9RqgcR24g")

# list of movies will be showed at a web page
movies_list = [four_rooms, skool_of_rock,the_fith_element]

# generate and show  aweb page by fresh tomatoes 
fresh_tomatoes.open_movies_page(movies_list)

