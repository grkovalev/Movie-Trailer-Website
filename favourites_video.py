import video
import fresh_tomatoes


four_rooms = video.movie("Four Rooms",
                          120,
                          "https://upload.wikimedia.org/wikipedia/en/c/c8/Four_rooms_ver2.jpg",
                          "https://www.youtube.com/watch?v=Rieq_TR7cV0")

skool_of_rock = video.movie("School of Rock",
                             109 ,
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

the_fith_element = video.movie('The Fith Element',
                                126,
                                "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
                                "https://www.youtube.com/watch?v=fQ9RqgcR24g")

movies_list = [four_rooms, skool_of_rock,the_fith_element]

fresh_tomatoes.open_movies_page(movies_list)

