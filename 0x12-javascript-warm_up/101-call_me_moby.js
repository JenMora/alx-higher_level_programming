#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;
