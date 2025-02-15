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
    description="This is an example of a CRUD using services for a football tournament.",
)

app.include_router(Achievement_router.router)
app.include_router(Boosters_router.router)
app.include_router(Challenges_router.router)
app.include_router(ChallengesAchievement_router.router)
app.include_router(ChallengesBoosters_router.router)
app.include_router(Course_router.router)
app.include_router(CourseAchievement_router.router)
app.include_router(Division_router.router)
app.include_router(Lesson_router.router)
app.include_router(LessonBoosters_router.router)
app.include_router(Progress_router.router)
app.include_router(Question_router.router)
app.include_router(Section_router.router)
app.include_router(Stage_router.router)
app.include_router(User_router.router)
app.include_router(UserAchievement_router.router)
app.include_router(UserBoosters_router.router)
app.include_router(UserCourse_router.router)
app.include_router(UserQuestion_router.router)



@app.get("/")
async def root():
    """This method is used to get the root of the API."""
    return {"message": "Welcome to the Football API!"}


@app.get("/tournament/init_data")
def init_data():
    """This method is used to initialize the tournament data."""
    try:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
        
        return {"message": "Data was created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e