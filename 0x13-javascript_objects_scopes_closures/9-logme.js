#!/usr/bin/node
let counter = 0;
exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter = counter + 1;
};
