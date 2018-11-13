
///////// IEX API ////////


// info
// get_info = (ticker) => {
  
//   let Http = new XMLHttpRequest();
//   let url_info=`https://api.iextrading.com/1.0/stock/${ticker}/company`;
//   Http.open("GET", url_info);
//   Http.send();
//   Http.onreadystatechange = (e) => {
//     //console.log(Http.responseText)
//   }
// }



// get_info(ticker)





let ticker = document.getElementById("ticker").innerHTML;
ticker = ticker.split(" ")[1];
console.log(ticker)


async function getLogo(ticker) {
  try {
      const result = await fetch(`https://api.iextrading.com/1.0//stock/${ticker}/logo`);
      const data = await result.json(); // wait in background
      const url = data["url"];
      document.getElementById("company_logo").src = `${data["url"]}`;
      return data; // return a promise
  } catch(error) {
      console.log(error);
  }
}

getLogo(ticker);