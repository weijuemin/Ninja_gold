$(function(){
	var log = $('.log').text();
	if(log.indexOf('Ouch') !== -1) {
		$('p:contains("Ouch")').addClass('loseMoney');
	}
})