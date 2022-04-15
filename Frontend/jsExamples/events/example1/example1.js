const input = document.querySelector("input")
const h1 = document.querySelector("h1");

input.addEventListener("keyup", (e) => {
    const { value } = e.target;

    h1.innerHTML = value;
});
