function changeImageURL(imgId, newUrl) {
	//The image object accessed through its id we mentioned in the DIV block which is going to be visible currently
	var img = document.getElementById(imgId);
	img.src = newUrl;
	return;	
}

