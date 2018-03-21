# Visualization for TV series ratings.

This contains a dump of a JSON of episode grades for various TV shows, along with a script that visualizes the grades for the show as a whole and per episode.

Try running `do_show("Deadwood")` to show the ratings of the show Deadwood from IMDB and tv.com. It also shows you the two sites' rating plotted against each other to see how well they line up.

Try running `do_season("Deadwood")` to get a graph of the show's grade as the season went on.

Shows currently in the data:

 * Better Off Ted
 * Breaking Bad
 * Deadwood
 * Firefly
 * Game of Thrones
 * Lost
 * The Walking Dead
 * The Wire
 
 Currently the intent is to play with the data. I've noticed both sites have a general agreement in trend for shows, the different sites seem to have different preferences; IMDB folks liked Breaking Bad and Game of Thrones more than tv.com's visitors did, who in term prefered Firefly, Deadwood and Better Off Ted.
 
 It is interesting to see that tv.com viewers generally have a lower variance in the grades they give a show. 
 
 Another interesting trend is The Walking Dead show seemed to be on the decline up to the end of last season, but the grades are up at the start of this new season. This could be explained by those that liked it are more likely to have kept up and thus those are the only grades in yet, where those that lost interest towards the end of last season seemed to have stopped watching all together. We will tell if the numbers hold steady by the end of this season.
 
 A final interesting tidbit is that for Breaking Bad, both sites' visitors seemed to value the show about evenly for the first 3 seasons, but tv.com visitors then lowered their ratings of the final two seasons, whereas imdb visitors rated the final two seasons higher than the first three.
