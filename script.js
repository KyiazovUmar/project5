const apiKey = "1E5ZxnNUbbGQarWjMA7tCwp3Btm38GvRkv";

function getWeather() {
  const city = document.getElementById("city-input").value;

  if (!city) {
    alert("Шаардын атын жазыңыз!");
    return;
  }

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=ky`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      if (data.cod !== 200) {
        document.getElementById("weather-result").innerHTML = "Шаар табылган жок.";
        return;
      }

      const weather = `
        <h2>${data.name}</h2>
        <p>${data.weather[0].description}</p>
        <p>Температура: ${data.main.temp}°C</p>
        <img src="http://openweathermap.org/img/wn/${data.weather[0].icon}.png">
      `;

      document.getElementById("weather-result").innerHTML = weather;
    })
    .catch(error => {
      console.error(error);
      document.getElementById("weather-result").innerHTML = "Ката чыкты.";
    });
}
