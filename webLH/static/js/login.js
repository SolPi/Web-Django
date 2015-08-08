function login($modal){
	var token = $("[name=csrfmiddlewaretoken]", $modal).val();
	var mail = $("#mail", $modal).val();
	var psw = $("#psw", $modal).val();
	$.ajax({method: "POST",
	  	url: "login",
	  	data: { csrfmiddlewaretoken: token, mail: mail, psw: psw }
	}).done(function( msg ) {
    	alert( msg.msg );
  });
}