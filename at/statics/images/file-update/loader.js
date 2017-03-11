
$(document).ready(function() {
"use strict";


// *************
// Selectbox
// *************
// $('.filter select').selectbox();


$('select.styled').customSelect();


// *************
// Validate
// *************
$('form').validate({
	onKeyup : true,
	eachValidField : function() {
		$(this).closest('div').removeClass('error').addClass('success');
	},
	eachInvalidField : function() {
		$(this).closest('div').removeClass('success').addClass('error');
	}
});

// insert-attr
$('.insert-attr').attr('data-pattern', "^[-a-z0-9!#$%&'*+/=?^_`{|}~]+(\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)*@([a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)*(aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|[a-z][a-z])$");


// *************
// Colorbox
// *************
$(".group1").colorbox({
	rel:'group1',
	className: 'hideElement',
	iframe:true,
	innerWidth:640,
	innerHeight:390,
});

$(".group2").colorbox({
	rel:'group2',
	title: false,
	width:"100%"
});

$(".group3").colorbox({
	rel:'group3',
	title: false,
	width:"100%"
});

$(".group5").colorbox({
	rel:'group1',
	className: 'hideElement',
	iframe:true,
	width: '100%',
	innerHeight:390,
});

// *************
// BxSlider
// *************
var bxSlider = $('.software_slider .form-bxslider').bxSlider({
	mode: 'fade',
	auto: false,
	pause: 10000,
	adaptiveHeight: true,
	pagerCustom: '#dafault_pager',
	onSliderLoad: function() {
		$('.form-bxslider li').each(function() {
			var setTimeoutID;
			if ( $(this).is(':visible') ) {
				setTimeoutID = setTimeout(function() {
					$('.fin_1').animate({ 'opacity': 1 }, 700);
				}, 400);
				setTimeoutID = setTimeout(function() {
					$('.fin_2').animate({ 'opacity': 1 }, 700);
				}, 800);
				setTimeoutID = setTimeout(function() {
					$('.fin_3').animate({ 'opacity': 1 }, 700);
				}, 1400);
			}
		});
	}
});

$('.xSlider').bxSlider({
	mode: 'fade',
	auto: false,
	pause: 10000,
	adaptiveHeight: true,
	onSliderLoad: function() {
		$('.form-bxslider li').each(function() {
			var setTimeoutID;
			if ( $(this).is(':visible') ) {
				setTimeoutID = setTimeout(function() {
					$('.fin_1').animate({ 'opacity': 1 }, 700);
				}, 400);
				setTimeoutID = setTimeout(function() {
					$('.fin_2').animate({ 'opacity': 1 }, 700);
				}, 800);
				setTimeoutID = setTimeout(function() {
					$('.fin_3').animate({ 'opacity': 1 }, 700);
				}, 1400);
			}
		});
	}
});



$('.aboutUs-slider').bxSlider({
	mode: 'horizontal',
	pause: 5000,
	autoHover: true,
	pager: false,
	auto: false
});




// devicePixelRatio
if (window.devicePixelRatio > 1.5) {
	var lowresImages = $('img');
	lowresImages.each(function(i) {
		var lowres = $(this).attr('src');
		var highres = lowres.replace(".", "r.");
		$(this).attr('src', highres);
	});
}
});