#!/usr/bin/node
module.export = class square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
