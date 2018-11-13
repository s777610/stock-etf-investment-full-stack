"use strict";

///////// IEX API ////////

var ticker = document.getElementById("ticker").innerHTML;
ticker = ticker.split(" ")[1];
console.log(ticker);

async function getLogo(ticker) {
    try {
        var result = await fetch("https://api.iextrading.com/1.0//stock/" + ticker + "/logo");
        var data = await result.json(); // wait in background
        var url = data["url"];
        document.getElementById("company_logo").src = "" + data["url"];
        return data; // return a promise
    } catch (error) {
        console.log(error);
    }
}

async function getInfo(ticker) {
    try {
        var result = await fetch("https://api.iextrading.com/1.0/stock/" + ticker + "/company");
        var data = await result.json(); // wait in background
        //console.log(data)
        var ceo = data["CEO"];
        var desc = data["description"];
        var industry = data["industry"];
        var website = data["website"];
        if (ceo) {
            document.getElementById("ceo").innerHTML = "CEO: " + ceo;
        };
        if (industry) {
            document.getElementById("industry").innerHTML = "Industry: " + industry;
        };
        document.getElementById("description").innerHTML = "" + desc;
        document.getElementById("web").href = "" + website;
        return data; // return a promise
    } catch (error) {
        console.log(error);
    }
}

getLogo(ticker);
getInfo(ticker);
