from flask import Flask
app=Flask(__name__)
@app.route ('/')
def hello_world():
    return "<div style='backgroung : blue'><h1>Harish</h1><br><p>Hi, I'm Harish. I am currently pursuing a bachelor's degree in mechanical engineering. I'm in my early 20s and have many plans for my future, so it's time to take action. I'm obssed with the cars which makes me very happy and I used to watch F1 my favourite Drives are Niki Lauda, Michael Schumacher, Lewis Hamilton, Charles Leclerc, Max Verstappen, Lando Norris etc.. </p></div>"
if __name__=='__main__':
    app.run(debug=True)