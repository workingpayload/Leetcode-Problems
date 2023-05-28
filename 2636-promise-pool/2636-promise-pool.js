var promisePool = async function(functions, n) {
    let index = 0;

    async function callNext() {
        const curFunction = functions[index];
        if (curFunction) {
            index++;
            await curFunction();
            return callNext();
        }
    }

    return Promise.all(new Array(n).fill().map(callNext));
};