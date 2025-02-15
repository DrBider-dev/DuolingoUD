-- This sql script is for MySql
CREATE DATABASE IF NOT EXISTS DuolingoDB;
USE DuolingoDB;

-- Tablas sin claves foráneas
CREATE TABLE IF NOT EXISTS Question (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    content TEXT NOT NULL,
    answer TEXT NOT NULL,
    isCorrect BOOLEAN NOT NULL,
    type VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Division (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    currentPosition INT NOT NULL,
    zone VARCHAR(50),
    users INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Challenges (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT NOT NULL,
    progress INT DEFAULT 0,
    goal INT NOT NULL,
    reward VARCHAR(300)
);

CREATE TABLE IF NOT EXISTS Boosters (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    cost INT NOT NULL,
    benefit TEXT,
    maxNumber INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Achievement (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    progressPercentage DECIMAL(5,2) NOT NULL,
    goal VARCHAR(100) NOT NULL
);

-- Tablas con dependencias de nivel 1
CREATE TABLE IF NOT EXISTS Lesson (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(20) NOT NULL,
    Questions_FK INT,
    EXP INT,
    time TIME,
    accuracy INT,
    FOREIGN KEY (Questions_FK) REFERENCES Question(id_PK)
);

CREATE TABLE IF NOT EXISTS Section (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    lessons_FK INT,
    guide TEXT,
    FOREIGN KEY (lessons_FK) REFERENCES Lesson(id_PK)
);

CREATE TABLE IF NOT EXISTS Stage (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    sections_FK INT,
    level VARCHAR(2),
    FOREIGN KEY (sections_FK) REFERENCES Section(id_PK)
);

CREATE TABLE IF NOT EXISTS Course (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    language VARCHAR(60) NOT NULL,
    stages_FK INT,
    FOREIGN KEY (stages_FK) REFERENCES Stage(id_PK)
);

-- Tabla User con múltiples dependencias
CREATE TABLE IF NOT EXISTS User (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    nickname VARCHAR(50) NOT NULL UNIQUE,
    joinDate DATE DEFAULT (CURRENT_DATE()),
    division_FK INT,
    timesInTop INT DEFAULT 0,
    email VARCHAR(75) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL,
    courses_FK INT NOT NULL,
    achievements_FK INT,
    followed INT DEFAULT 0,
    followers INT DEFAULT 0,
    gemsNumber INT DEFAULT 0,
    livesNumber INT DEFAULT 5,
    boostersNumber INT DEFAULT 0,
    isPremium BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (division_FK) REFERENCES Division(id_PK),
    FOREIGN KEY (courses_FK) REFERENCES Course(id_PK),
    FOREIGN KEY (achievements_FK) REFERENCES Achievement(id_PK)
);

-- Tablas restantes con dependencias
CREATE TABLE IF NOT EXISTS Progress (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    Course_FK INT NOT NULL,
    User_FK INT NOT NULL,
    streakDays INT NOT NULL DEFAULT 0,
    DailyEXP INT NOT NULL DEFAULT 0,
    WeeklyEXP INT NOT NULL DEFAULT 0,
    TotalEXP INT NOT NULL DEFAULT 0,
    percentage DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (Course_FK) REFERENCES Course(id_PK),
    FOREIGN KEY (User_FK) REFERENCES User(id_PK)
);

-- Tablas de relación (N:M)
CREATE TABLE IF NOT EXISTS UserCourse (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    User_FK INT,
    Course_FK INT,
    FOREIGN KEY (User_FK) REFERENCES User(id_PK),
    FOREIGN KEY (Course_FK) REFERENCES Course(id_PK)
);

CREATE TABLE IF NOT EXISTS UserQuestion (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    User_FK INT,
    Question_FK INT,
    FOREIGN KEY (User_FK) REFERENCES User(id_PK),
    FOREIGN KEY (Question_FK) REFERENCES Question(id_PK)
);

CREATE TABLE IF NOT EXISTS UserBoosters (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    User_FK INT,
    Boosters_FK INT,
    FOREIGN KEY (User_FK) REFERENCES User(id_PK),
    FOREIGN KEY (Boosters_FK) REFERENCES Boosters(id_PK)
);

CREATE TABLE IF NOT EXISTS UserAchievement (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    User_FK INT,
    Achievement_FK INT,
    FOREIGN KEY (User_FK) REFERENCES User(id_PK),
    FOREIGN KEY (Achievement_FK) REFERENCES Achievement(id_PK)
);

CREATE TABLE IF NOT EXISTS CourseAchievement (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    Course_FK INT,
    Achievement_FK INT,
    FOREIGN KEY (Course_FK) REFERENCES Course(id_PK),
    FOREIGN KEY (Achievement_FK) REFERENCES Achievement(id_PK)
);

CREATE TABLE IF NOT EXISTS LessonBoosters (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    Lesson_FK INT,
    Boosters_FK INT,
    FOREIGN KEY (Lesson_FK) REFERENCES Lesson(id_PK),
    FOREIGN KEY (Boosters_FK) REFERENCES Boosters(id_PK)
);

CREATE TABLE IF NOT EXISTS ChallengesBoosters (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    Challenges_FK INT,
    Boosters_FK INT,
    FOREIGN KEY (Challenges_FK) REFERENCES Challenges(id_PK),
    FOREIGN KEY (Boosters_FK) REFERENCES Boosters(id_PK)
);

CREATE TABLE IF NOT EXISTS ChallengesAchievement (
    id_PK INT PRIMARY KEY AUTO_INCREMENT,
    Challenges_FK INT,
    Achievement_FK INT,
    FOREIGN KEY (Challenges_FK) REFERENCES Challenges(id_PK),
    FOREIGN KEY (Achievement_FK) REFERENCES Achievement(id_PK)
);