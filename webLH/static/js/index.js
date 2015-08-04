function changePage(li){
	if(li.id != page){
		$("#"+page).removeClass("active");
		li.className = li.className + " active";
		switch(li.id) {
		    case 'init':
		        $("#inicio").show()
		        break;
		    case 'cal':
		        $("#calendario").show()
		        break;
		    case 'act':
		        $("#actividades").show()
		        break;
		    case 'soc':
		        $("#socios").show()
		        break;
		    case 'cont':
		        $("#contacto").show()
		        break;
		    case 'new':
		        $("#new_socio").show()
	    }
		switch(page) {
		    case 'init':
		        $("#inicio").hide()
		        break;
		    case 'cal':
		        $("#calendario").hide()
		        break;
		    case 'act':
		        $("#actividades").hide()
		        break;
		    case 'soc':
		        $("#socios").hide()
		        break;
		    case 'cont':
		        $("#contacto").hide()
		        break;
		    case 'new':
		        $("#new_socio").hide()
	    }
	}
}