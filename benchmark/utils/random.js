export function getRandomInt(min, max) {
    return min + Math.floor(Math.random() * max);
}

export function getRandomFromArray(arr) {
    return arr[getRandomInt(0, arr.length)];
}

export function getRandomElementsFromArray(arr, count) {
    let samples = [];
    for (let i = 0; i < count; i++) {
        samples.push(getRandomFromArray(arr));
    }
    return samples;
}