import os

def generate_workout_plan(name, age, weight, goal, intensity):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return f'''
7 Day Workout Plan for {name}

Day 1 - Cardio
Day 2 - Upper Body
Day 3 - Core Workout
Day 4 - Rest
Day 5 - Lower Body
Day 6 - Cardio + Abs
Day 7 - Stretching

Goal: {goal}
Intensity: {intensity}
'''

    try:
        import google.generativeai as genai

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
Create a simple 7 day workout plan.

Name: {name}
Age: {age}
Weight: {weight}
Goal: {goal}
Intensity: {intensity}

Return day wise workout.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return "AI error: " + str(e)