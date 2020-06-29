function searchResult() {
    var searchQuery= localStorage.getItem("search_data");
    document.getElementById("write").innerHTML = searchQuery;
    fetchResults(searchQuery.trim())
}

function fetchResults(searchQuery) {
    const endpoint = `https://en.wikipedia.org/w/api.php?action=query&list=search&prop=info&inprop=url&utf8=&format=json&origin=*&srlimit=20&srsearch=${searchQuery}`;
  	fetch(endpoint)
  		.then(response => response.json())
  		.then(data => {
            const results = data.query.search;
            console.log(results)
            displayResults(results);
		})
    .catch(() => console.log('An error occurred'));
}

function displayResults(results) {
  // Store a reference to `.searchResults`
  const searchResults = document.querySelector('.searchResults');
  // Remove all child elements
  searchResults.innerHTML = '';
  // Loop over results array
  results.forEach(result => {
  const url = encodeURI(`https://en.wikipedia.org/wiki/${result.title}`);
  localStorage.setItem("URL", url); 
  searchResults.insertAdjacentHTML('beforeend',
      `<div class="resultItem">
        <h3 class="resultItem-title">
          <a href="${url}" target="_blank" rel="noopener">${result.title}</a>
        </h3>
        <span class="resultItem-snippet">${result.snippet}</span><br>
        <a href="${url}" class="resultItem-link" target="_blank" rel="noopener">${url}</a>
      </div>`
    );
  });
}

searchResult()

$('#easyPaginate').easyPaginate({
    paginateElement: 'div',
    elementsPerPage: 5,
    effect: 'climb'
});
