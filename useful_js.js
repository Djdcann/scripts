// Return URL Parameters by name
// Ex: http://thing.com/?cat=cool getParameterByName('cat') returns 'cool'
function getParameterByName(name) {
        var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
        return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
    }
