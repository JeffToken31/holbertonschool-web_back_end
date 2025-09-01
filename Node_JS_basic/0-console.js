function displayMessage(message) {
    if (typeof message !== "string") {
        throw new Error('Must be a string');
    }
    console.log(message);
}

module.exports = displayMessage;