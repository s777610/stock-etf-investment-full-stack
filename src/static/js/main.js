import "@babel/polyfill";
///////// IEX API ////////

let ticker = document.getElementById("ticker").innerHTML;
ticker = ticker.split(" ")[1];

async function getLogo(ticker) {
  try {
    const result = await fetch(
      `https://api.iextrading.com/1.0/stock/${ticker}/logo`
    );
    const data = await result.json(); // wait in background
    const url = data["url"];
    document.getElementById("company_logo").src = `${data["url"]}`;
    return data; // return a promise
  } catch (error) {
    console.log(error);
  }
}

async function getInfo(ticker) {
  try {
    const result = await fetch(
      `https://api.iextrading.com/1.0/stock/${ticker}/company`
    );
    const data = await result.json(); // wait in background
    //console.log(data)
    const ceo = data["CEO"];
    const desc = data["description"];
    const industry = data["industry"];
    const website = data["website"];
    if (ceo) {
      document.getElementById("ceo").innerHTML = `CEO: ${ceo}`;
    }
    if (industry) {
      document.getElementById("industry").innerHTML = `Industry: ${industry}`;
    }
    document.getElementById("description").innerHTML = `${desc}`;
    document.getElementById("web").href = `${website}`;
    return data; // return a promise
  } catch (error) {
    console.log(error);
  }
}

getLogo(ticker);
getInfo(ticker);
