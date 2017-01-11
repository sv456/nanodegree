import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story","A story of a boy and his toys","http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print toy_story.storyline

avatar=media.Movie("Avatar","About aliens","https://www.movieposter.com/posters/archive/main/98/MPW-49246","https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print avatar.storyline
#avatar.show_trailer()

battlefield=media.Movie("Battlefield","About saving country","http://dice-wp-prd.s3.amazonaws.com/wp-content/uploads/2014/12/15191329/bf3bg.jpg","https://www.youtube.com/watch?v=ymwXbF1VTKU&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DymwXbF1VTKU&has_verified=1")
#battlefield.show_trailer()

naruto=media.Movie("Naruto","About shinobi world","http://cdn.zonarutoppuden.com/ns/peliculas-naruto-shippuden.jpg","https://www.youtube.com/watch?v=mksl3tYdyK4")

movies=[toy_story,avatar,battlefield,naruto]
fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS

#print media.Movie.__doc__
