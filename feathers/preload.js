window.eval = global.eval = function() {
    throw new this.Error('unsecure window.eval() is not supported.');
};