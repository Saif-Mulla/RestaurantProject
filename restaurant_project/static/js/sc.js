var videoPlayer = document.getElementById("videoPlayer");
var myVideo = document.getElementById("myVideo");


function stopVideo() {
	videoPlayer.style.display = "none";
}

function playVideo(file) {
	myVideo.src = file;
	videoPlayer.style.display = "block";
}

$(document).ready(function() {
	  var btn = $(".but1");
	  btn.click(function() {
	    btn.toggleClass("paused");
	    return false;
	  });
	});