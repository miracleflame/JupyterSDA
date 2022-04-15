const person = {
    firstName: "Tomas",
    lastName: "Fuchs",
    getName() {
        return `${this.firstName} ${this.lastName}`;
    },
};


const name = person.getName();
console.log(name);
