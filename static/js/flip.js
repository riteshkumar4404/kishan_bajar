// TRIGGER EVENTS
$(document).ready(function() {

	// 3D CARD ANIMATION
	$('.front li').on('click', function(event){
		event.preventDefault();
		$('.back div').removeClass('active');
		$('#'+$(this).attr('id')+'Box').addClass('active');
		$('.box').addClass('active');
	});
	$('#closeBox').on('click', function(event){
		event.preventDefault();
		$('.back div').removeClass('active');
		$('.box').removeClass('active');
	});
});