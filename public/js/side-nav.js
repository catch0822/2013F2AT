$(function(){
	var   $nav = $( '#nav' )
	  , aRules = [];


	$( '<style>' + aRules.join( ', ' ) + '{ background : url( images/grey-pink-dot.png ) 0 100% no-repeat; }</style>' ).appendTo( $( 'head' ) );

	$nav
		.on( 'mouseenter', 'li', function(){
			$( this ).find( 'h1' ).stop().show().animate({ opacity:1, duration: 100, left: 30 }, { queue: false });
		})
		.on( 'mouseleave', 'li', function(){
			var self = this;
			$( this ).find( 'h1' ).stop().animate({ opacity:0, duration: 100, left: 15 }, { queue: false, complete : function(){ $( this ).hide(); } });
		});
});