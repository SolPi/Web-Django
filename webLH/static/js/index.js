function changePage(li){
	if(li.id != page){
		$("#"+page).removeClass("active");
		li.className = li.className + " active";
		$("#div-"+li.id).show();
		$("#div-"+page).hide();
		page = li.id;
	}
}