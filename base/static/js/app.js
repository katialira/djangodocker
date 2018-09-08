$(function() {

  $('.carousel').carousel()

  $('.menu-palindromo').on('click', function(){
    $('.menu-hover').show();
  });


  $('.menu-close').on('click', function(){
    $('.menu-hover').hide();
  });  

	$('.pal-items').on('mouseenter', 'li', function(){
		$(this).siblings().children('.itemHVR').fadeIn('fast');
	});

	$('.pal-items').on('mouseleave', 'li', function(){
		$(this).siblings().children('.itemHVR').hide();
	});

  setTimeout( fadeInWord, 3500 );

});

function fadeInWord() {
  $esto = $( '.palindromo-letras > .animated' );
  if ( $esto.hasClass( 'stop' ) ){
    var seconds = ( Math.floor(Math.random() * 2) + 1  ) * 300;
    setTimeout( randomPink, seconds);

  } else {
    var seconds = ( Math.floor(Math.random() * 3) + 2  ) * 350;
    setTimeout( fadeInWord, seconds );
  }
  $esto.removeClass('opac').removeClass('animated').removeClass('fadeIn').next().addClass( 'animated' ).addClass( 'fadeIn' );
  
}

function randomPink() {
  var $what = $(".palindromo-letras span");
  $what.removeClass('animated').removeClass('fadeIn');
  var list = $what.toArray();
  var elemlength = list.length;
  var randomnum = Math.floor(Math.random()*elemlength);
  var randomitem = list[randomnum];
  $(randomitem).addClass( 'animated' ).addClass( 'fadeIn' );

    var seconds = ( Math.floor(Math.random() * 3) + 2  ) * 600;
    setTimeout( randomPink, seconds);

}

document.addEventListener('DOMContentLoaded', function() {
  var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    typeSpeed: 60,
    backSpeed: 20,
    startDelay: 0,
    loop: true,
    loopCount: Infinity,

  });

});

function prettyLog(str) {
  console.log('%c ' + str, 'color: green; font-weight: bold;');
}

