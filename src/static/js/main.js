
///////// IEX API ////////
// const ticker = {{ plot.ticker|tojson }}
// console.log(ticker)

let ticker = document.getElementById("ticker").innerHTML;
ticker = ticker.split(" ")[1];
console.log(ticker)


// info
get_info = (ticker) => {
  
  let Http = new XMLHttpRequest();
  let url_info=`https://api.iextrading.com/1.0/stock/${ticker}/company`;
  Http.open("GET", url_info);
  Http.send();
  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }
  (e) => {
    console.log(Http.responseText)
  }
}



// logo
get_logo = (ticker) => {
  
  let Http = new XMLHttpRequest();
  let url_logo=`https://api.iextrading.com/1.0//stock/${ticker}/logo`;
  Http.open("GET", url_logo);
  Http.send();
  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }
  (e) => {
    console.log(Http.responseText)
  }
}

get_info(ticker)
get_logo(ticker)