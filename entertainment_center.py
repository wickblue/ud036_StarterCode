import fresh_tomatoes
import media

inception = media.Movie("Inception",
                        "Heist inside dream world.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

inglorious_bastards = media.Movie("Inglorious Bastards",
                     "A team of Jews and spies hunt down the Nazis",
                     "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                     "https://www.youtube.com/watch?v=qRYDNWXuip8")

american_psycho = media.Movie("American Psycho",
                              "A killer operates in plain sight in the banaesia of Wall St.",
                              "https://upload.wikimedia.org/wikipedia/en/6/63/Americanpsychoposter.jpg",
                              "https://www.youtube.com/watch?v=2GIsExb5jJU")

the_social_network = media.Movie("The Social Network",
                              "How a Harvard kid created Facebook",
                              "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                              "https://www.youtube.com/watch?v=lB95KLmpLR4")

good_will_hunting = media.Movie("Good Will Hunting",
                                "A janitor from Southie is a genius",
                                "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

the_godfather = media.Movie("The Godfather",
                            "Vito Corleone runs his family business",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=5DO-nDW43Ik")

movies = [inception, inglorious_bastards, american_psycho, the_social_network, good_will_hunting, the_godfather]

fresh_tomatoes.open_movies_page(movies)

