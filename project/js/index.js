$(document).ready(function() {
	$("#size").keyup(function(e) {
		if (e.which == 13) {
			var size = $('#size').val();
			var url = 'https://randomuser.me/api/?results='+size;
			$.ajax({
			  url: url,
			  dataType: 'json',
			  success: function(data) {
	    		$(".output").text(JSON.stringify(data));			
			  }
			});
		}
    });
});