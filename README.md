# Spotify-Music-Recommender-System

In the first version of this code the cosine_similarity function of the sklearn library is used to find the similar features between the entered song and other songs in this dataset. 

This dataset contains 19 features as fallows:

	1. Valence: the positiveness of a track 
	
	2. Year: the year of a track releasing
	
	3. Acousticness: measure how acoustic a track is
	
	4. Artist: the name of a track's singer/producer
	
	5. Danceability: how suitable a track is for dance
	
	6. Duration ms: the duration of a track
	
	7. Energy: how energetic a track is
	
	8. Explicit: how much explicit content a track has
	
	9. ID: the unique id of a track in this dataset
	
	10. Key: the note the music is centered around
	
	11. Liveness: detects the presence of an audience in the recording
	
	12. Loudness: the overall loudness of a track in decibels (dB)
	
	13. Instrumentalness: predicts whether a track contains no vocals
	
	14. Speechiness: speechiness detects the presence of spoken words in a track 
	
	15. Tempo: the overall estimated tempo of a track in beats per minute (BPM)
	
	16. Mode: any of several ways of ordering the notes of a scale according to the intervals they form with the tonic
	
	17. Name: the name of a track 
	
	18. Popularity: how popular a track is
	
	19. Release_date: the date a track is released
	
In the second version of this code, I will fulfill some of my curiocities about the music like Valences over time, Popularity vs Danceability, etc..

As can be seen in the line plots, the valence (positivity) in the different songs of different artists are fluctuated over time. Moreover, there is no strong correlation between the danceability and popularity in the songs according the scatter plot.

It is worth mentioning that only small portion of the data can be used in the plots and recommender function because the whole version of the data both will mess the plots and cause an error after running the cosin1e_similariity function due to the shortage of the RAM Memory.

In the third version of this code, I will solve the recommendation issue using the Spotify API itself...