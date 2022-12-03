function savechat() {

  let body = document.body.innerText;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:5000/save');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({ body: body }));

}
