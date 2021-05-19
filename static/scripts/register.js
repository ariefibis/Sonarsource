const username_input = document.getElementById('username');

const debounce = (func, delay) => { 
  let debounceTimer 
  return function() { 
      const context = this
      const args = arguments 
          clearTimeout(debounceTimer) 
              debounceTimer 
          = setTimeout(() => func.apply(context, args), delay) 
  } 
}

function xhrSuccess() { 
  this.callback.apply(this, this.arguments); 
}

function xhrError() { 
  console.error(this.statusText); 
}

function validate_username(username, callback) {
  var xhr = new XMLHttpRequest();
  xhr.callback = callback;
  xhr.arguments = Array.prototype.slice.call(arguments, 2);
  xhr.onload = xhrSuccess;
  xhr.onerror = xhrError;
  xhr.open("GET", 'username/'+username, true);
  xhr.send(null);
}

username_input.addEventListener('input', debounce(function(evt){
  validate_username(this.value, function() {
    const available = JSON.parse(this.responseText).available;
    if (available) {
      username_input.setCustomValidity('');
    } else {
      username_input.setCustomValidity('This username is not available');
    }
    username_input.reportValidity();
  });
}, 300));
