from fastapi import FastAPI
import random

app = FastAPI()

jokes = [
    "Why did the logistic regression model break up? It couldn't handle the relationship!",
    "A data engineer’s favorite exercise is the pipeline push-up: build, fail, debug, repeat.",
    "Why was the deep learning model so good at making friends? It had too many layers!",
    "Overfitting is when your model is so obsessed with the training data that it refuses to move on.",
    "Why do Python programmers prefer NumPy? Because their love for arrays is limitless!",
    "A statistician drowned in a river that was, on average, only three feet deep.",
    "Why did the AI break up with the neural network? Too many hidden layers!",
    "Linear regression is great—until life throws you some curves.",
    "Why did the data analyst bring a ladder? To reach the highest level of confidence!",
    "Pandas is not just a Python library; it's also what data scientists turn into after debugging all night.",
    "Why do data scientists love coffee? Because it helps them stay statistically significant!",
    "A machine learning model walks into a bar. The bartender says, 'What’ll you have?' The model replies, 'I don’t know yet, let me see some examples.'",
    "Why did the data scientist go to therapy? Too many unresolved dependencies!",
    "Big data is like teenage sex—everyone talks about it, nobody really knows how to do it, and everyone thinks everyone else is doing it.",
    "How do data scientists flirt? They say, 'Are you a p-value? Because you’ve got my interest!'",
    "I tried to make a data visualization, but it was just a scatterplot of my career choices.",
    "Why don’t data scientists ever get lost? They always have a map (reduce).",
    "Data scientists don’t have trust issues. They just need a 95% confidence interval before committing.",
    "Why was the neural network cold? It had too many dropouts!",
    "Deep learning is like trying to bake a cake without a recipe, but you keep adjusting the ingredients until it tastes good.",
]


@app.get("/joke")
def get_joke():
    """
    Get a random joke about data science
    """
    return {"joke": random.choice(jokes)}


@app.post("/joke")
def update_joke(joke: str):
    """
    Update the jokes array

    Args:
    joke (str): The joke to add to the jokes array

    """
    jokes.append(joke)

    return {"message": "Joke added successfully!"}
