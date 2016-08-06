# contains data structure for createion web 
# page elements by fresh_tomatoes.py

class Movie():
    def __init__(self, title, duration, poster_url, trailer_url):
        """Init metohd 
            Keyword arguments:
            title       -- title of the movie
            duration    -- duration of the Movie
            poster_url  -- url with poster picture
            trailer_url -- url with trailer video 
        """      
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url