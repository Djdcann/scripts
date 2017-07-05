//Return URL Parameters by name
//Ex: http://thing.com/?cat=cool getParameterByName('cat') returns 'cool'
function getParameterByName(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

//Bootstrap Modal inside a modal fix
$(document).on('show.bs.modal', '.modal', function () {
    var zIndex = 1040 + (10 * $('.modal:visible').length);
    $(this).css('z-index', zIndex);
    setTimeout(function () {
        $('.modal-backdrop').not('.modal-stack').css('z-index', zIndex - 1).addClass('modal-stack');
    }, 0);
});

//copy text to clipboard
function copyTextToClipboard(text) {
  	    var textArea = document.createElement("textarea");
        
  	    textArea.style.position = 'fixed';
  	    textArea.style.top = 0;
  	    textArea.style.left = 0;
        
  	    textArea.style.width = '2em';
  	    textArea.style.height = '2em';

  	    textArea.style.padding = 0;
        
  	    textArea.style.border = 'none';
  	    textArea.style.outline = 'none';
  	    textArea.style.boxShadow = 'none';
        
  	    textArea.style.background = 'transparent';
        
        
  	    textArea.value = text;
        
  	    document.body.appendChild(textArea);
        
  	    textArea.select();
        
  	    try {
  		  var successful = document.execCommand('copy');
  		  var msg = successful ? 'successful' : 'unsuccessful';
  		  console.log('Copying text command was ' + msg);
  	    } catch (err) {
  		  console.log('Oops, unable to copy');
  	    }
        
  	    document.body.removeChild(textArea);
    }
