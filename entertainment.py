import media
import fresh_tomatoes
chaloo=media.movie("chaloo","story about revenge","https://www.the"
        "telugufilmnagar.com/wp-content/uploads/2017/11/"
        "Chalo-Teaser-1-1024x538.jpg","https://www.youtube.com/"
        "watch?v=6_BxEjvWsqs")
athadu=media.movie("athadu","A professional killer is hired to fake the assassination of a politician."
                   "But the politician is killed and he is framed for the murder"
                  " He assumes the identity of a dead man to escape from the law.","https://www.filmibeat.com/img/"
                   "220x100x275/popcorn/movie_posters/athadu-1538.jpg","https://www.youtube.com/watch?v=ckBU0s4-5cQ")
oh_my_friend=media.movie("oh_my_friend","Siri and Chandu are childhood friends but, because the"
                         "chemistry between them is too complicated,"
                         "they find it challenging to define their relation to their respective partners.","https://1847884116.rsc"
                         ".cdn77.org/telugu/gallery/"
                         "movies/ohmyfriend/main2.jpg"
                         ,"https://www.youtube.com/watch?v=JdsRM19S3Fg")

films=[chaloo,athadu,oh_my_friend]
fresh_tomatoes.open_films_page(films)
