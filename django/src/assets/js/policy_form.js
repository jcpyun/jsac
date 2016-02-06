var currCircle = 1
var currBar = 0

mapp_nums = {
	1: "first",
	2: "second",
	3: "third",
	4: "fourth",
	5: "fifth"
}

$(document).ready(function() {
	$(".prev-btn").click(function () {
		if (currCircle == 1) return;

		// clear previous circle
		num_str = mapp_nums[currCircle]
		$("." + num_str).removeClass("half-empty")

		// half empty next circle
		currCircle -= 1
		if (currCircle == 0) return;
		num_str = mapp_nums[currCircle]
		$("." + num_str).removeClass("filled").addClass("half-empty")

		if (currCircle == 5) return;
		// clear previous bar
		num_str = mapp_nums[currBar]
		$("." + num_str + "-bar").removeClass("filled")
		currBar -= 1 

	})

	$(".next-btn").click(function () {
		if (currCircle == 6) return;

		// fill previous circle
		num_str = mapp_nums[currCircle]
		$("." + num_str).removeClass("half-empty").addClass("filled")
		
		// half-empty next circle
		currCircle += 1
		if (currCircle == 6) return;
		num_str = mapp_nums[currCircle]
		$("." + num_str).addClass("half-empty")

		// fill prev bar
		currBar += 1
		num_str = mapp_nums[currBar]
		$("." + num_str + "-bar").addClass("filled")
	})

	function getIconOfPanelHeading(heading) {
		return $(heading).find(".panel-title").find(".link-clicker").find(".select-circle");
	}


	$(".panel-title > a").click(function() {
		if ($(this).parent().parent().hasClass("active")) {
			$(".panel-heading.active").children().children().children().removeClass("glyphicon-ok-sign").addClass("glyphicon-record");
			$(".panel-heading.active").removeClass("active");
			return;
		}
		$(".panel-heading.active").removeClass("active");
		$(this).parent().parent().addClass("active");
		console.log($(this).find(".panel-title").find(".link-clicker").find(".select-circle"))
		$(".select-circle.glyphicon-ok-sign").removeClass("glyphicon-ok-sign").addClass("glyphicon-record");
		$(".panel-heading.active").children().children().children().removeClass("glyphicon-record").addClass("glyphicon-ok-sign");
	});




})