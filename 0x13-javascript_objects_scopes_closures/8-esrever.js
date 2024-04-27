#!/usr/bin/node
exports.esrever = function (list) {
  const out = [];
  for (let i = list.length - 1; i >= 0; i--) {
    out.push(list[i]);
  }
  return out;
};
