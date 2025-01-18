@import url("https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap");
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  list-style: none;
  font-family: "Rubik", sans-serif;
}
:root {
  --font-color-main: #332464;
  --white-color: #fff;
}
body {
  background-color: #e0eefa;
}
.pc {
  width: 398px;
  height: 860px;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid var(--font-color-main);
  border-radius: 40px;
}

nav {
  position: fixed;
  left: 0;
  right: 0;
  margin: 0 auto;
  width: fit-content;
  bottom: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 250px;
  height: 60px;
  border-radius: 40px;
 border: 2px solid var(--white-color);
  background-color: var(--font-color-main);
}
nav ul {
  display: flex;
  gap: 2pc;
}
nav ul li a {
  color: var(--white-color);
  font-size: 18px;
}
.active {
  background-color: var(--white-color);
  color: var(--font-color-main);
  border-radius: 100px;
  padding: 8px 15px;
}
h3 {
  color: var(--font-color-main);
  text-align: center;
  margin: 30px 0;
}
.search {
  width: 340px;
  height: 50px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 1px 2px 2px var(--font-color-main);
  background-color: var(--white-color);
}
.search-icon {
  width: 18px;
  height: 50px;
  display: flex;
  border-radius: 20px;
  justify-content: center;
  align-items: center;
}
.search-icon i {
  font-size: 18px;
  color: var(--font-color-main);
}
.search input {
  width: 85%;
  padding: 10px;
  font-size: 15px;
  color: var(--font-color-main);
  border: none;
  outline: none;
}
.search input::placeholder {
  color: var(--font-color-main);
}
/*  */
.error-message {
  display: none;
}
.error-message p {
  width: 100%;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--font-color-main);
  text-align: center;
  padding: 40px;
}
/*  */
.message {
  display: block;
}
.message p {
  width: 100%;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--font-color-main);
  text-align: center;
  padding: 50px;
}
/*  */
.return {
  display: none;
}
.box {
  max-width: 400px;
  height: auto;
  padding: 0 40px;
  margin-left: auto;
  margin-right: auto;
  border:1px solid black;
  margin-top: 40px;
}
.weather-box {
  height: 200px;
  max-width: 320px;
  border-radius: 40px;
  margin-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--font-color-main);
}
.name {
  padding-left: 40px;
  width: 220px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  color: var(--white-color);
  height: auto;
}
.city-name {
  font-size: 20px;
}
.weather-temp {
  font-size: 60px;
}
.weather-icon {
  padding: 0 20px;
  width: 220px;
  height: 170px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.weather-icon img {
  width: 100%;
}
/*  */
.weather-desc {
  display: flex;
  justify-content: center;
  column-gap: 10px;
}
.desc-box {
  width: 100px;
  display: grid;
  padding: 15px;
  gap: 5px;
  height: 100px;
  margin-top: 10px;
  border-radius: 20px;
  place-content: center;
  color: var(--white-color);
  background-color: var(--font-color-main);
}

@media (max-width: 400px) {
  .pc {
    border: none;
    border-radius: none;
    width: auto;
    height: auto;
  }
}
