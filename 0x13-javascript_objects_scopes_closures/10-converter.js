#!/usr/bin/node
exports.converter = function (base) {
  function myConverter(x) {
    return n.toString(base);
  }
  return myConverter;
};
