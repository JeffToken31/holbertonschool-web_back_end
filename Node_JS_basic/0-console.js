function displayMessage(message) {
    if (typeof message !== "string") {
        throw new Error('Must be a string');
    }
    process.stdout.write(message + '\n');
}

module.exports = displayMessage;