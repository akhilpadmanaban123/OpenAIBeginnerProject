import openai
from flask import Flask, request, render_template


app=Flask(__name__)

openai.api_key="YOUR_KEY"   # Created from OpenAI account

def generate_answer(question):
    response=openai.Completion.create(engine='text-davinci-002',prompt=f'{question}',
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5)
    return response.choices[0].text

@app.route('/',methods=["GET", "POST"])
def index():
    if request.method=="POST":
        query=request.form["query"]
        ans=generate_answer(query)
        return render_template("index.html", response=ans)
    return render_template("index.html")

if __name__=="__main__":
    app.run() 
#Akhil Padmanaban
