import media
import fresh_tomatoes


# Passing Movie's Title, Storyline, Poster URL, Trailer URL as arguments
# to init
justice_league = media.Movie('''Justice League''', '''Fueled by his
restored faith in humanity and inspired by Superman's
(Henry Cavill) selfless act, Bruce Wayne (Ben Affleck)
enlists newfound ally Diana Prince to face an even greater
threat. Together, Batman and Wonder Woman work quickly to recruit
a team to stand against this newly awakened enemy. Despite the
formation of an unprecedented league of heroes -- Batman, Wonder
Woman, Aquaman, Cyborg and the Flash -- it may be too late to
save the planet from an assault of catastrophic proportions.''', '''http://t0.g
static.com/images?q=tbn:ANd9GcTbr9aajZtJiuhXc_biRws9jzCi4u1q4M
WvyPVe0rGO9Z0RwDqT''', '''https://www.youtube.com/watch?v=r9-DM9uBtVI''')

thor_ragnarok = media.Movie('''Thor: Ragnarok''', '''Imprisoned on the
other side of the universe, the mighty Thor finds himself in
deadly gladiatorial contest that pits him against the Hulk,
his former ally and fellow Avenger. Thor's quest for survival
leads him in a race against time to prevent the all-powerfulHela from d
estroying his home world and the Asgardian civilization.''', '''http://t
3.gstatic.com/images?q=tbn:ANd9GcST1uigGrukMvSAVUefFNuQ0NMZAR-FjfFIwSZFCR5Zk
yMSgCyj''', '''https://www.youtube.com/watch?v=ue80QwXMRHg''')

iron_man2 = media.Movie('''Iron Man 2''', '''With the world now aware
that he is Iron Man, billionaire inventor Tony Stark
(Robert Downey Jr.) faces pressure from all sides to
share his technology with the military. He is reluctant
to divulge the secrets of his armored suit, fearing the
information will fall into the wrong hands. With Pepper
Potts (Gwyneth Paltrow) and \"Rhodey\" Rhodes (Don Cheadle)
by his side, Tony must forge new alliances and confront a
powerful new enemy.''', '''https://upload.wikimedia.org/wikipedia/en/e/ed/Iron
_Man_2_poster.jpg''', '''https://www.youtube.com/watch?v=DIfgxIv5xmk''')

gifted = media.Movie('''Gifted''', '''The plot follows an intellectually
gifted 7-year-old who becomes the subject of a custody battle
between her uncle and grandmother.''', '''https://upload.wikimedia.or
g/wikipedia/en/f/fe/Gifted_film_poster.jpg''', '''https://www.youtube.
com/watch?v=hqTSKqBCdf0''')

logan = media.Movie('''Logan''', '''In 2029 the mutant population has
shrunken significantly and the X-Men have disbanded. Logan,
whose power to self-heal is dwindling, has surrendered himself
to alcohol and now earns a living as a chauffeur. He takes care
of the ailing old Professor X whom he keeps hidden away''', '''https://uploa
d.wikimedia.org/wikipedia/en/3/37/\Logan_2017_poster.jpg''', '''https://
www.youtube.com/watch?v=hqTSKqBCdf0''')

civilwar = media.Movie('''Captain America:Civil War''', '''In Captain
America: Civil War, disagreement over international oversight
of the Avengers fractures them into opposing factions one led by
Steve Rogers and the other by Tony Stark.''', '''https://upload.wikime
dia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg''', '''h
ttps://www.youtube.com/watch?v=dKrVegVI0Us''')

# Passing Movies List to open_movies_page function
movies = [justice_league, thor_ragnarok, iron_man2, gifted, logan, civilwar]
fresh_tomatoes.open_movies_page(movies)
