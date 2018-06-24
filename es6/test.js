#!/usr/local/bin/node

/**
* Unit Tests for the JS Base-Ä implementation
**/

require('./base-ä.js')
const assert = require('assert')
const range = x => Array.from(Array(x)).map((_, i) => i)

// every combination must be distinct
const e = range(BaseÄ.max + 1).map(BaseÄ.encode)
const u = Object.keys(e.reduce((a, k) => { a[k]=1; return a }, {}))
assert(u.length == BaseÄ.max + 1, 'encoding must be injective.')

// every combination must round-trip successfully
range(BaseÄ.max + 1).map(x => {
	assert(BaseÄ.decode(BaseÄ.encode(x)) == x, 'encoding must be bijective.')
})

// invalid encodes
assert.throws(_ => BaseÄ.encode(-1),   { message: '\'-1\' cannot be encoded in Base-Ä.' })
assert.throws(_ => BaseÄ.encode(8514), { message: '\'8514\' cannot be encoded in Base-Ä.' })

// invalid decodes
assert.throws(_ => BaseÄ.decode(null),    { message: '\'null\' is not a valid Base-Ä identifier.' })
assert.throws(_ => BaseÄ.decode('Gipsy'), { message: '\'Gipsy\' is not a valid Base-Ä identifier.' })
assert.throws(_ => BaseÄ.decode('1 2'),   { message: '\'1 2\' is not a valid Base-Ä identifier.' })

// validity checks
assert(BaseÄ.valid('Gipsy Danger' ) === true)
assert(BaseÄ.valid('Gipsy Doofus' ) === false)
assert(BaseÄ.valid('Goatse Danger') === false)

console.log('all tests successful.')

// sample a few names for visual inspection
console.log(range(15).map(BaseÄ.encode))
