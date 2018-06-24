//usr/bin/cc $0 -Wall -Wextra -Wpedantic -o baseatest && ./baseatest; rm baseatest; exit;
// Unit Tests for the C Base-Ä implementation

#include <stdio.h>
#include <assert.h>
#include "basea.h"

int main() {
	char temp[BASE_A_LENGTH];
	int r = -1;

	// every combination must round-trip successfully
	for (int x = 0; x <= BASE_A_MAX; x++) {
		base_a_encode(x, temp);
		base_a_decode(temp, &r);
		assert(r == x);
	}

	// invalid encodes
	assert(base_a_encode(-1,   temp));
	assert(base_a_encode(8514, temp));

	// invalid decodes
	assert(base_a_decode(NULL,    &r));
	assert(base_a_decode("",      &r));
	assert(base_a_decode("Gipsy", &r));
	assert(base_a_decode("1 2",   &r));

	// validity checks
	assert(1 == base_a_valid("Gipsy Danger"));
	assert(0 == base_a_valid("Gipsy Doofus"));
	assert(0 == base_a_valid("Goatse Danger"));

	printf("all tests successful.\n");

	// sample a few names for visual inspection
	for (int x = 0; x < 15; x++) {
		base_a_encode(x, temp);
		printf("%s\n", temp);
	}
}
