export default function cleanSet(set, startString) {
    if (!startString || typeof startString !== 'string') {
        return '';
    }
    let array = [];
    set.forEach(element => {
        if (element.slice(0, startString.length) === startString) {
            array.push(element.slice(startString.length));
       }
    });
    return array.join('-');
}