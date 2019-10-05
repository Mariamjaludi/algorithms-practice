# Movies On Flight
# You are on a flight and wanna watch two movies during this flight. You are
# given int[] movie_duration which includes all the movie durations. You are
# also given the duration of the flight which is d in minutes. Now, you need to
# pick two movies and the total duration of the two movies is less than or equal
# to (d - 30min). Find the pair of movies with the longest total duration. If
# multiple found, return the pair with the longest movie.

movie_duration = [90, 85, 75, 60, 120, 150, 125]
d = 250

ans = [90, 125]

def movies(movie_duration, d):
    if len(movie_duration) == 0:
        return []

    maxMovietime = d - 30
    movie_duration.sort()
    left = 0
    right = len(movie_duration) - 1
    
    dec = 0

    while left < right:
        currentSum = movie_duration[left] + movie_duration[right]
        if currentSum == maxMovietime + dec:
            return [movie_duration[left], movie_duration[right]]
        elif currentSum > maxMovietime + dec:
            right -= 1
        elif currentSum < maxMovietime + dec:
            left += 1
        if left >= right:
            dec -= 1
            left = 0
            right = len(movie_duration) - 1

print(movies(movie_duration, d))
