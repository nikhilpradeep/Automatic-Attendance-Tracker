$(function() {

  // test to ensure jQuery is working
  console.log("whee!")

 
  $("#faculty_select").change(function() {

    // grab value
    var faculty = $("#faculty_select").val();

    // send value via GET to URL /<department_id>
    var get_request = $.ajax({
      type: 'GET',
      url: '/term/' + faculty + '/',
    });

    // handle response
    get_request.done(function(data){

      // data
      console.log(data)

      // add values to list 
      var option_list = [["", "Select term"]].concat(data);
      $("#term_select").empty();
	  
        for (var i = 0; i < option_list.length; i++) {
          $("#term_select").append(
            $("<option></option>").attr("value", option_list[i][1]).text(option_list[i][1]));
        }
      // show model list
      $("#term_select").show();
	  
	  
    });
  });

  $("#term_select").change(function() {

    // grab value
    
	var term = $("#term_select").val();

    // send value via GET to URL /<department_id>
    var get_request1 = $.ajax({
      type: 'GET',
      url: '/term1/' + term + '/',
    });

    // handle response
    get_request1.done(function(data){

      // data
      console.log(data)

     
	  
	  
	  var option_list1 = [["", "Select Subject"]].concat(data);
	  $("#subject_select").empty();
	  for (var i = 0; i < option_list1.length; i++) {
          $("#subject_select").append(
            $("<option></option>").attr("value", option_list1[i][1]).text(option_list1[i][1]));
        }
		$("#subject_select").show();
    });
  });
  
  
  
    $(function() {
        $('a#test').bind('click', function() {
            $.getJSON('/',
                function(data) {
              //do nothing
            });
            return false;
        });
    });


});

