from fastapi import FastAPI, HTTPException


from Services import (
    Achievement_router,
    Boosters_router,
    Challenges_router,
    ChallengesAchievement_router,
    ChallengesBoosters_router,
    Course_router,
    CourseAchievement_router,
    Division_router,
    Lesson_router,
    LessonBoosters_router,
    Progress_router,
    Question_router,
    Section_router,
    Stage_router,
    User_router,
    UserAchievement_router,
    UserBoosters_router,
    UserCourse_router,
    UserQuestion_router,

)
app = FastAPI(
    title="Duolingo API",
    version="0.0.1",
    description="This is an example of a CRUD using services for Duolingo.",
)

app.include_router(Achievement_router)
app.include_router(Boosters_router)
app.include_router(Challenges_router)
app.include_router(ChallengesAchievement_router)
app.include_router(ChallengesBoosters_router)
app.include_router(Course_router)
app.include_router(CourseAchievement_router)
app.include_router(Division_router)
app.include_router(Lesson_router)
app.include_router(LessonBoosters_router)
app.include_router(Progress_router)
app.include_router(Question_router)
app.include_router(Section_router)
app.include_router(Stage_router)
app.include_router(User_router)
app.include_router(UserAchievement_router)
app.include_router(UserBoosters_router)
app.include_router(UserCourse_router)
app.include_router(UserQuestion_router)



@app.get("/")
async def root():
    """This method is used to get the root of the API."""
    return {"message": "Welcome to the Duolingo API!"}


@app.get("/Duolingo/init_data")
def init_data():
    """This method is used to initialize data."""
    from Initialization.Init_Users import InitUsers
    InitUsers().create_users(3)