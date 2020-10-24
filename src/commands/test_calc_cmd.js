url = 'https://raw.githubusercontent.com/Sharpieman20/Sharpie-s-Speedrunning-Tools/main/links/testcalc.txt';

function yourCallback( retrievedText ) { 
    return retrievedText;
};


fetch(url).then((response) => response.text().then(yourCallback))