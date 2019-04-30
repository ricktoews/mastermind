'use strict';

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

function buildDigits(count) {
    var list = '';
    for (var i = 0; i < count; i++) {
        list += letters.charAt(i);
	}
    return list
}


function product() {
  var args = Array.prototype.slice.call(arguments); // makes array from arguments
  return args.reduce(function tl (accumulator, value) {
    var tmp = [];
    accumulator.forEach(function (a0) {
      value.forEach(function (a1) {
        tmp.push(a0.concat(a1));
      });
    });
    return tmp;
  }, [[]]);
}

function build(symbols, places) {
    var perms = [];
    var digits = buildDigits(symbols);
    for (var num in product(digits, repeat=places) {
        let perm = ''.join(num);
        perms.push(perm);
    }

    return perms
}
