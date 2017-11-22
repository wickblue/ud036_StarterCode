import fresh_tomatoes
import media

# create individual movie variables with characteristics

inception = media.Movie("Inception",
                        "Heist inside dream world.",
                        "https://goo.gl/WQQ62c",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

inglorious_bastards = media.Movie("Inglorious Bastards",
                                  "A team of US spies hunt down the Nazis",
                                  "https://goo.gl/sKWkDY",
                                  "https://youtu.be/qRYDNWXuip8")

american_psycho = media.Movie("American Psycho",
                              "A killer on Wall St. operates in plain sight",
                              "https://goo.gl/Tcd6AC",
                              "https://www.youtube.com/watch?v=2GIsExb5jJU")

the_social_network = media.Movie("The Social Network",
                                 "How a Harvard kid created Facebook",
                                 "https://goo.gl/E9jy1F",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

good_will_hunting = media.Movie("Good Will Hunting",
                                "A janitor from Southie is a genius",
                                "https://goo.gl/JptpxY",
                                "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

the_godfather = media.Movie("The Godfather",
                            "Vito Corleone runs his family business",
                            "https://goo.gl/RzGm8L",
                            "https://www.youtube.com/watch?v=5DO-nDW43Ik")

# creates an array of the movies defined above

movies = [inception, inglorious_bastards, american_psycho,
          the_social_network, good_will_hunting, the_godfather]

# opens up final web page and creates HTML file
fresh_tomatoes.open_movies_page(movies)
