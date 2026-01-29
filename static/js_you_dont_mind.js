/***************** Show tmr *****************/
const tmrEl = document.querySelector("header span");

function showTm() {
  const now = new Date();
  const mins = now.getMinutes().toString();
  const hours = now.getHours().toString();

  const formattedMins = mins.padStart(2, "0");

  tmrEl.innerText = `${hours}:${formattedMins}`;
}

function showCurrentTm() {
  showTm();

  const now = new Date();
  const nextMinute = (60 - now.getSeconds()) * 1000 - now.getMilliseconds();

  setTimeout(() => {
    showTm();

    setInterval(showTm, 60000);
  }, nextMinute);
}

showCurrentTm();
