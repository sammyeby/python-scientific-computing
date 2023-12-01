INSERT INTO Album (title, artist_id) VALUES ('Stillmatic', 1);
INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 3);
INSERT INTO Album (title, artist_id) VALUES ('IV', 2);


INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Ether', 5, 437, 0, 1, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('You are da Man', 5, 325, 0, 1, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Black Dog', 5, 297, 0, 3, 2);
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Stairway', 5, 482, 0, 3, 2);
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('About to Rock', 5, 313, 0, 2, 3);
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Who Made Who', 5, 207, 0, 2, 3);


SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id=Artist.id

SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id

SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id

-- Across all four tables - (One to Many Relationship)
SELECT Track.title, Artist.name, Album.title, Genre.name, Track.rating FROM Track JOIN Genre JOIN Album JOIN Artist ON 
Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id


-- Many To Many Relationship Database Queries - Data Modelled at the connection
CREATE TABLE "Member" ("user_id" INTEGER , "course_id" INTEGER , "role" INTEGER, PRIMARY KEY (user_id, course_id))

INSERT INTO User (name, email) VALUES ('Samuel', 'contact@samuelumeh.com'); -- 1 [Py, SQL, Typ, PHP, Rea]
INSERT INTO User (name, email) VALUES ('Julia', 'jul@tsugi.com'); -- 2 [SQL, Typ, PHP, Rea]
INSERT INTO User (name, email) VALUES ('Chuck', 'ed@tsugi.com'); -- 3 [Py, SQL, Rea, PHP]
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.com'); -- 4 [Py, SQL, PHP]

INSERT INTO Course (title) VALUES ('Python'); -- 1
INSERT INTO Course (title) VALUES ('SQL'); -- 2
INSERT INTO Course (title) VALUES ('TypeScript'); -- 3
INSERT INTO Course (title) VALUES ('PHP'); -- 4
INSERT INTO Course (title) VALUES ('React'); -- 5

-- Samuel                               
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (1, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (1, 4, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (1, 5, 1);

-- Julia
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 4, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 5, 0);

-- Chuck
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 2, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 5, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 4, 1);

-- Sue
INSERT INTO Member (user_id, course_id, role) VALUES (4, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (4, 2, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (4, 5, 0);

-- Get Data
SELECT User.name, Member.role, Course.title FROM User JOIN Member JOIN Course ON
Member.user_id = User.id AND Member.course_id = Course.id ORDER BY Course.title, Member.role DESC, User.name


