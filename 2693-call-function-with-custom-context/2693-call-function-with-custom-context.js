/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
Function.prototype.callPolyfill = function(context, ...args) {
 const temp = Symbol();
    context[temp] = this;
    const ans = context[temp](...args);
    delete context[temp];
    return ans;
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */