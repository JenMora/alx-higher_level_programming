#!/usr/bin/node
exports.converter = function (base) {
  return function (integer) {
    return integer.toString(base);
  };
};
