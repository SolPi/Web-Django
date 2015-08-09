function registrar($form){
    $(this).submit(function(){return false});
    $form.validator('validate').on('submit', function (e) {
        var token = $("[name=csrfmiddlewaretoken]", $form).val();
        var mail = $("#mail_registrar").val();
        var pass = $("#pass_registrar").val();
        $.ajax({method: "POST",
            url: "resgistrar",
            data: { csrfmiddlewaretoken: token,
                    mail: mail,
                    pass: pass
                  }
        }).done(function( msg ) {
            alert( msg.msg );
        });
    });
}