jQuery(document).ready(function($) {
    $("div.collapseheader").click(function () {
        $header = $(this).children("span").first();
        $codearea = $(this).children(".input_area");
        $codearea.slideToggle(500, function () {
            $header.text(function () {
                return $codearea.is(":visible") ? "Collapse Code" : "Expand Code";
            });
        });
    });
});

function pad(s) { return (s < 10) ? '0' + s : s; }
function PocketAPI(tag, container) {
	$.getJSON('http://api.dornea.nu/pocket/get/' + tag, function(data) {
		var table = '<table class="table table-condensed">';
		table += " \
			<thead>\
				<tr>\
					<th class='col-md-2'>Date</th>\
					<th>Link</th>\
					<th>Excerpt</th>\
				</tr>\
			</thead>\
		";

		$.each(data.list, function(index, item) {
			console.log(item);
			var d = new Date(item.time_added * 1000);
			var date = [pad(d.getFullYear()), pad(d.getMonth()+1), pad(d.getDate())].join('-');
			table += '<tr><td>' + date + '</td><td><a href="' + item.resolved_url + '">' + item.resolved_url + '</a></td>';        table += '<td>' + item.excerpt + '</tr>';
		});

		table += '</table>';
		$(container).append(table);
    });
}
