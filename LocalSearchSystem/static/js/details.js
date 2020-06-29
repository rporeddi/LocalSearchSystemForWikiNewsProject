(async () => {
  const response = await fetch('https://en.wikipedia.org/wiki/Hello');
  const text = await response.text();
  const dom = await new JSDOM(text);
  console.log(dom.window.document.querySelector("h1").textContent);
})()