$(function() {
		$("#loading").hide();
		// <![CDATA[
        $('#button').click(function(){
            $("#loading").show();
            
        });//preloader
		
		$(window).bind("pageshow", function(event) {
			$("#loading").hide();
		});
		
		$(document).on("keydown", function(){
			$("#loading").hide();
		});
});