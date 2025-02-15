USE DuolingoDB;

-- Insertar datos en la tabla Question
INSERT INTO Question (content, answer, isCorrect, type) VALUES
('¿Cómo se dice "hola" en inglés?', 'Hello', TRUE, 'Vocabulario'),
('¿Cuál es la capital de Francia?', 'París', TRUE, 'Geografía'),
('¿2 + 2?', '4', TRUE, 'Matemáticas'),
('¿El sol es una estrella?', 'Sí', TRUE, 'Ciencia');

-- Insertar datos en la tabla Division
INSERT INTO Division (name, currentPosition, zone, users) VALUES
('Bronce', 1, 'América', 100),
('Plata', 2, 'Europa', 200),
('Oro', 3, 'Asia', 150);

-- Insertar datos en la tabla Challenges
INSERT INTO Challenges (description, progress, goal, reward) VALUES
('Completa 10 lecciones', 5, 10, '100 gemas'),
('Gana 3 divisiones', 1, 3, 'Booster especial'),
('Responde 50 preguntas', 25, 50, '500 EXP');

-- Insertar datos en la tabla Boosters
INSERT INTO Boosters (name, cost, benefit, maxNumber) VALUES
('Doble EXP', 50, 'Gana el doble de EXP por 1 hora', 3),
('Vida extra', 30, 'Obtén una vida adicional', 5),
('Respuesta rápida', 20, 'Reduce el tiempo de respuesta', 2);

-- Insertar datos en la tabla Achievement
INSERT INTO Achievement (name, progressPercentage, goal) VALUES
('Principiante', 25.00, 'Completa 10 lecciones'),
('Intermedio', 50.00, 'Completa 50 lecciones'),
('Avanzado', 75.00, 'Completa 100 lecciones');

-- Insertar datos en la tabla Lesson
INSERT INTO Lesson (type, Questions_FK, EXP, time, accuracy) VALUES
('Vocabulario', 1, 10, '00:10:00', 90),
('Geografía', 2, 15, '00:15:00', 85),
('Matemáticas', 3, 20, '00:20:00', 95);

-- Insertar datos en la tabla Section
INSERT INTO Section (name, lessons_FK, guide) VALUES
('Básico', 1, 'Guía para principiantes'),
('Intermedio', 2, 'Guía para intermedios'),
('Avanzado', 3, 'Guía para avanzados');

-- Insertar datos en la tabla Stage
INSERT INTO Stage (sections_FK, level) VALUES
(1, 'A1'),
(2, 'A2'),
(3, 'B1');

-- Insertar datos en la tabla Course
INSERT INTO Course (language, stages_FK) VALUES
('Inglés', 1),
('Francés', 2),
('Alemán', 3);

-- Insertar datos en la tabla User
INSERT INTO User (name, nickname, joinDate, division_FK, timesInTop, email, password, courses_FK, achievements_FK, followed, followers, gemsNumber, livesNumber, boostersNumber, isPremium) VALUES
('Juan Pérez', 'juanp', '2023-01-01', 1, 2, 'juan@example.com', 'password123', 1, 1, 10, 5, 100, 5, 2, FALSE),
('Ana Gómez', 'anag', '2023-02-15', 2, 1, 'ana@example.com', 'password456', 2, 2, 15, 10, 200, 4, 3, TRUE);

-- Insertar datos en la tabla Progress
INSERT INTO Progress (Course_FK, User_FK, streakDays, DailyEXP, WeeklyEXP, TotalEXP, percentage) VALUES
(1, 1, 5, 100, 500, 1000, 50.00),
(2, 2, 3, 150, 750, 1500, 75.00);

-- Insertar datos en la tabla UserCourse
INSERT INTO UserCourse (User_FK, Course_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla UserQuestion
INSERT INTO UserQuestion (User_FK, Question_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla UserBoosters
INSERT INTO UserBoosters (User_FK, Boosters_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla UserAchievement
INSERT INTO UserAchievement (User_FK, Achievement_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla CourseAchievement
INSERT INTO CourseAchievement (Course_FK, Achievement_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla LessonBoosters
INSERT INTO LessonBoosters (Lesson_FK, Boosters_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla ChallengesBoosters
INSERT INTO ChallengesBoosters (Challenges_FK, Boosters_FK) VALUES
(1, 1),
(2, 2);

-- Insertar datos en la tabla ChallengesAchievement
INSERT INTO ChallengesAchievement (Challenges_FK, Achievement_FK) VALUES
(1, 1),
(2, 2);