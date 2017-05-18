#on appelle ce fichier .WSGI pour forcer/marquer le fait que c'est le point d'entre pour le cote serveur

#Installation
from flask import Flask
application = Flask(__name__)

if __name__ == "__main__":
    application.run()

#lsite des routes:


#Page dynamique API
from flask import request, escape

@application.route("/") #fonction
def hello():
    return "Hello World!"

@application.route("/info.php")
def info_php():
    return "Pas de ça chez moi!"

@application.route("/salut/<string:name>")
def salutation(name):
    return "Salut " + name + "!"

@application.route("/calculator")
def calculator_v1():
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    return "a + b = %d" % (a * b)

@application.route("/static/index.html")
@application.route("/index.html")
def index():
    return send_file("static/index.html", "text/html") #pourquoi on met le "text/html"

#exemple test
@application.route("/hello")
def test():
    a=hello()
    b=info_php()
    return a + b

#partie AJAX
from flask import send_file, jsonify #, render_template

@application.route('/ajax') #permet d'utiliser un URL minimal
def ajax():
    #return render_template('static/ajax.html') #render_template
    return send_file('static/ajax.html') #send_file a choisir selon
#quelle est la difference entre ces deux methodes


@application.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a * b) # utilise le format de données JSON

#le dernier orm est celui qui est utilisé
import quizz as orm


##READ##
#recuperer des donnees
#@application.route('/score', methods=['GET', 'POST'])
#def highscore():
    #a = request.args.get('name', 0, type=str)
    #resultat=orm.HighScore.get().where(orm.HighScore.player=="joueur1")
    #return jsonify(result ="best : "+resulat)

    #a = request.args.get('name', 0, type=str)
    #result = ""
    #for f in orm.HighScore.get():
        #result += "%s %s %d " %(f.player,f.game,f.score)
    #return jsonify(orm.HighScore.select().where(orm.HighScore.player=="joueur1"))
    #return result
#for f in orm.HighScore.select().where(orm.HighScore.player=="joueur"):
    #result += "%s %s %d " %(f.player,f.game,f.score)


#HighScore
@application.route('/scorebis', methods=['GET', 'POST'])
def highscorebis():
    a = request.args.get('name', 0, type=str)
    result = ""
    for f in orm.HighScore.select().where(orm.HighScore.player==a):
        result += "%s %s %d " %(f.player,f.game,f.score)
    if result=="":
        return jsonify("User not found.")
    return jsonify(result)


#quizz
@application.route('/getquizzdata', methods=['GET', 'POST'])
def getquizzdata():
    result = ""
    for f in orm.Quizz.select():
        result += "%s %s %s %d " %(f.name,f.img,f.label_name,f.label_nb)
    if result=="":
        return jsonify("User not found.")
    return jsonify(result)


##/READ##
##CREATE##
#sauvegarde dans la DB
@application.route('/savescore', methods=['GET', 'POST'])
def savescore():
    a = request.args.get('name', 0, type=str)
    b = request.args.get('game', 0, type=str)
    c = request.args.get('score', 0, type=int)
    orm.HighScore.create(player=a,game=b,score=c)
    return jsonify(result ="Saved")

##/CREATE##
##UPDATE##

##/UPDATE##
##DELETE##
@application.route('/delete_score', methods=['GET', 'POST'])
def updatescore():
    a = request.args.get('name', 0, type=str)
    result = ""
    for f in orm.HighScore.select().where(orm.HighScore.player==a):
        result += "%s %s %d " %(f.player,f.game,f.score)
    if result=="":
        return jsonify(result="User not found.")
    f.player=""
    f.game=""
    f.score=0
    f.save()
    return jsonify(result="Score deleted")
    #orm.HighScore.select().where(orm.HighScore.player==a).score = 100000
    #orm.HighScore.select().where(orm.HighScore.player==a).save()

##/DELETE##
