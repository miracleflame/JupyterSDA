const form = document.querySelector("form");
const firstNameElement = document.querySelector("#first-name");
const lastNameElement = document.querySelector("#last-name");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const firstName = firstNameElement.value;
    const lastName = lastNameElement.value;
    console.log(firstName, lastName);
});
