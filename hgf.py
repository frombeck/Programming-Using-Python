def nn_movie(movie_likeness, reviews, uid, mid):
       likes = movie_likeness[mid].argsort()
     # reverse the sorting so that most alike are in
      # beginning
       likes = likes[::-1]
     # returns the rating for the most similar movie available
       for ell in likes:
           if reviews[u,ell] > 0:
               return reviews[u,ell]
