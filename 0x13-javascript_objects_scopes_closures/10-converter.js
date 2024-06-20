#!/usr/bin/node
exports.converter = function (base) {
  function convertNum (x) {
    return n.toString(base);
  }
  return convertNum;
};
