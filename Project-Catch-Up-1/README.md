
# Duolingo DataBase Design

## Project Description
This project focuses on replicating Duolingo’s database to understand how its core components are organized and managed. Duolingo is one of the most popular platforms for language learning, notable for its ability to personalize the user experience, adapt to skill levels, and motivate users with a reward system.

The main goal of this project is to analyze and model the key elements of Duolingo’s system, creating an entity-relationship diagram and database model that replicates the fundamental functionalities of the platform.

## Progress So Far

### 1. **Identification of Key Components**
An exhaustive analysis was conducted on the critical functionalities that make up Duolingo. These include:
   - **Users**: Progress information, accumulated experience, gems, lives, and achievements.
   - **Courses and Lessons**: Available languages, lesson structures divided by difficulty levels.
   - **Exercises**: Interactive content for practice and reinforcement of language concepts.
   - **Reward System**: Boosters, challenges, achievements, and gem rewards for goal completion.

### 2. **Definition of Entities and Attributes**
The main entities that are part of the system were identified, such as:
   - **User**: Name, nickname, progress, streak days, gems, and boosters.
   - **Course**: Language, level, and user progress.
   - **Lesson**: Exercise type, resolution time, accuracy, and experience points.
   - **Question**: Exercise content, correct answers, and results.

### 3. **Definition of Relationships**
Relationships between the main entities were established to ensure that data is correctly connected and structured. Key relationships include:
   - **User-Course**: A user can be enrolled in multiple courses, and a course can have multiple users.
   - **User-Lesson**: A user can complete several lessons, and a lesson can be taken by multiple users.
   - **Lesson-Question**: A lesson contains several questions, and each question is associated with a lesson.

### 4. **Entity-Relationship Model**
An entity-relationship diagram has been designed to capture the relationships between the main tables. This will serve as the foundation for implementing the physical model in a real database.

### 5. **Definition of Data-Structure, Constraints and Properties**
At this stage, the structure of the data within the database is meticulously defined. Each entity's attributes are mapped to specific data types to ensure efficient storage and retrieval. The data structure is crafted to reflect the relationships between entities while preserving flexibility and scalability.

## Next Steps
- **Implementation**: Create the schema in a database management system.
- **Testing and Adjustments**: Test the database with sample data to validate the integrity and efficiency of the model.
