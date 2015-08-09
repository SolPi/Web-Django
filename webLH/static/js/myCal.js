$(document).ready(function() {

	$('.calendar').fullCalendar({
		theme: true,
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		editable: true,
		height: 'auto',
		dayClick: function() {

	        $(this).css('background-color', 'red');

	    },
		eventLimit: true, // allow "more" link when too many events
		events: [
			{
				title: 'All Day Event',
				start: '2015-08-01'
			},
			{
				title: 'Long Event',
				start: '2015-08-07',
				end: '2015-08-10'
			},
			{
				id: 999,
				title: 'Repeating Event',
				start: '2015-08-09T16:00:00'
			},
			{
				id: 999,
				title: 'Repeating Event',
				start: '2015-08-16T16:00:00'
			},
			{
				title: 'Conference',
				start: '2015-08-11',
				end: '2015-08-13'
			},
			{
				title: 'Meeting',
				start: '2015-08-12T10:30:00',
				end: '2015-08-12T12:30:00'
			},
			{
				title: 'Lunch',
				start: '2015-08-12T12:00:00'
			},
			{
				title: 'Meeting',
				start: '2015-08-12T14:30:00'
			},
			{
				title: 'Happy Hour',
				start: '2015-08-12T17:30:00'
			},
			{
				title: 'Dinner',
				start: '2015-08-12T20:00:00'
			},
			{
				title: 'Birthday Party',
				start: '2015-08-13T07:00:00'
			},
			{
				title: 'Click for Google',
				url: 'http://google.com/',
				start: '2015-08-28'
			}
		]
	});

});