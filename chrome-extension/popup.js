let editSite = document.getElementById("editSite");
let savePreview = document.getElementById("savePreview");

// When the savePreview button is clicked, save the document and upload it somewhere for preview
savePreview.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: savePagePreview,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function setPageContentEditable() {
  document.body.contentEditable = "true";
  alert("You can now edit any text on this page.");
}

// Save Page preview and generate share url
function savePagePreview() {
  console.log(document.documentElement.innerText);

  let body = document.body.innerText;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:5000/save');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({ body: body }));
  alert("Saved chat thread, probably");
}
