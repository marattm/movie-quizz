// READ ME //

// Il faut changer toutes les boucles avec du innerHTML,
//faire la chaine de caractère avec puis appeller innerHTML !


///////////////
// FONCTIONS //
///////////////
function main(){
  create_block_question();
  create_rolling_menu(create_listing_menu());
  create_question_type();
  affichage_image();

}

function create_block_question() {
  for (var i = 0; i < nb_question; i++) {
    document.getElementById("question_tab").innerHTML += '<div id="question_type_'+i+'" class="question_type"><div id="question_name_'+i+'" class="question_name"></div><div id="question_image_'+i+'" class="question_image"></div><div id="question_entry_'+i+'" class="question_entry"><div id="question_answer_'+i+'" class="question_answer"><form><select id="rolling_menu_'+i+'" ></select></form> </div><div id="question_validation_'+i+'" class="question_validation"><input id="button_'+i+'" type="button" value="Confirmer"></div><p></p></div><p></p></div>';
  }
}
function create_rolling_menu(listingoption) {
  for (var i = 0; i < nb_question; i++) {
    document.getElementById("rolling_menu_"+i).innerHTML += listingoption;
  }
}
function create_listing_menu(){
  var list="";
  for (var i = 0; i <nb_question ; i++) {
    list += '<option>'+transistor[i].name+'</option>' ;
  }
  return list;
}

function create_question_type(){
  for (var i = 0; i < nb_question; i++) {
    document.getElementById("question_name_"+i).innerHTML += '<p>Q'+parseInt(i+1)+') What is the name of this transistor ? Choose one from the list below.</p>';
  }
}
function affichage_image() {
  for (var i = 0; i < nb_question; i++) {
    document.getElementById("question_image_"+i).innerHTML += '<img class="transistor_img"src= ../img/'+ transistor[i].img +' alt="Photo de T3" title="T3" /> ';
    create_rolling_menu();
  }
}






/* FONCTIONS POUR FAIRE APPARAITRE DES GROUPES DE LABELS DANS LES MENUS DEROULANTS (qq bugs a corriger)

  function create_rolling_menu_label(){
    //var label_nb=0;
    var label_name="";
    for (var i = 0; i < nb_question; i++) {
      if (label_name=!transistor[i].label_name){
        //label_nb++;

        document.getElementById("rolling_menu_"+i).innerHTML += '<optgroup label="_'+label_name+'" id="rolling_menu_'+i+'_group_'+transistor[i].label_nb+' class="rolling_menu_group""></optgroup>';
      }
      label_name=transistor[i].label_name;
    }
  }
  function create_rolling_menu_option(){
    for (var i = 0; i < nb_question; i++) {
      if ((transistor[i].label_nb==1)) {
        document.getElementById("rolling_menu_"+i+"_group_"+transistor[i].label_nb).innerHTML += '<option>'+transistor[i].name+'</option>' ;
      }
      if ((transistor[i].label_nb==2)) {
        document.getElementById("rolling_menu_"+i+"_group_"+transistor[i].label_nb).innerHTML += '<option>'+transistor[i].name+'</option>' ;
      }
    }
  }
  function create_rolling_menu_option(){
    for (var i = 0; i < nb_question; i++) {
      if ((transistor[i].label_nb==1)) {
        document.getElementById("rolling_menu_"+i+"_group_"+transistor[i].label_nb).innerHTML += '<option>'+transistor[i].name+'</option>' ;
      }
      if ((transistor[i].label_nb==2)) {
        document.getElementById("rolling_menu_"+i+"_group_"+transistor[i].label_nb).innerHTML += '<option>'+transistor[i].name+'</option>' ;
      }
    }
  }
*/




//exemple d'utilisation du jQuerry
//document.querySelector("h1").textContent += " AJOOOOUTé";


///////////////
// VARIABLES //
///////////////
var nb_question = 13;

var QuestionType = [
  {
    "name":"What is the name of this transistor ? Choose one from the list below."
  },
  {
    "name":"What is the type of this transistor ?"
  },
  {
    "name":"What is the main use of this transistor ?"
  }
];

var transistor = [ //liste car crochet
  {
    "name":"NPN", //tableau car 2 points
    "img":"pg_0001.png",
    "label_name":"t_bipolaire",
    "label_nb":"1"
  },
  {
    "name":"PNP",
    "img":"pg_0002.png",
    "label_name":"t_bipolaire",
    "label_nb":"1"
  },
  {
    "name":"NMOS",
    "img":"pg_0003.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"PMOS",
    "img":"pg_0004.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"NIGBT",
    "img":"pg_0005.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"PIGPT",
    "img":"pg_0006.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"nJFET",
    "img":"pg_0007.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"pJFET",
    "img":"pg_0008.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"nMOSFET(enhancement)",
    "img":"pg_0009.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },

  {
    "name":"pMOSFET(depletion)",
    "img":"pg_0010.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"nMOSFET(enhancement)",
    "img":"pg_0011.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"nMOSFET(depletion)",
    "img":"pg_0012.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  },
  {
    "name":"BOBAFET",
    "img":"pg_0013.png",
    "label_name":"t_effetdechamps",
    "label_nb":"2"
  }
];

///////////////
///// MAIN ////
///////////////

main();


'<p></p><div id="question_type_'+i+'" class="question_type"><div id="question_name_'+i+'" class="question_name"></div><div id="question_image_'+i+'" class="question_image"></div><div id="question_entry_'+i+'" class="question_entry"><div id="question_answer_'+i+'" class="question_answer"><form><select id="rolling_menu_'+i+'" ></select></form> </div><div id="question_validation_'+i+'" class="question_validation"><input id="button_'+i+'" type="button" value="Confirmer"></div><p></p></div><p></p></div><p></p>'
