// Base-Ä encoder-decoder library
#ifndef BASE_A_MAX
#define BASE_A_MAX 4095
#define BASE_A_LENGTH 64

#include <ctype.h> // tolower()
static const char* base_a_a[] = {
	"Atomic", "Ballistic", "Big", "Boxer", "Bracer", "Brawler", "Breaker", "Challenger",
	"Champion", "Cherno", "Chrome", "Cobra", "Contender", "Coyote", "Crimson", "Decider",
	"Diablo", "Dingo", "Disrupter", "Echo", "Eden", "Falcon", "Fearless", "Galaxy",
	"Gallant", "Gipsy", "Golden", "Grand", "Grizzly", "Guardian", "Horizon", "Hydra",
	"Intrepid", "Keeper", "Legend", "Mammoth", "Matador", "Mighty", "Mountain", "Neon",
	"Nova", "Phantom", "Protector", "Puma", "Righteous", "Romeo", "Shaolin", "Shining",
	"Solar", "Spartan", "Steady", "Striker", "Tacit", "Tesla", "Tiger", "Titan", "Valiant",
	"Viper", "Vulcan", "Warden", "Warrior", "Wildcat", "Yankee", "Zenith"
};
static const char* base_a_b[] = {
	"Absolute", "Ajax", "Alpha", "Apostle", "Ares", "Artemis", "Assassin", "Athena",
	"Avenger", "Banzai", "Blue", "Brave", "Bravo", "Brutus", "Cerberus", "Colossus",
	"Corinthian", "Courage", "Cruiser", "Danger", "Dawn", "Dazzle", "Delta", "Dreadnought",
	"Eureka", "Finisher", "Fist", "Fortress", "Fury", "Gauntlet", "Gladius", "Hyperion",
	"Infinite", "Intercept", "Judas", "Kilo", "Lightning", "Mega", "November", "Omega",
	"Paladin", "Phoenix", "Prophet", "Real", "Redeemer", "Resolve", "Rogue", "Romeo",
	"Ronin", "Saber", "Sentinel", "Sierra", "Specter", "Tango", "Thunder", "Turbo",
	"Typhoon", "Venus", "Victory", "Vigor", "Yukon", "Zero", "Zeus", "Zulu"
};

static const char* base_a_f(const char** source, const char* x, int* result) {
	for (int z = 0; x && z < 64; z++) {
		const char *a = x, *b = source[z];
		while (*a && *b && tolower(*a) == tolower(*b)) a++, b++;
		if ((*a == '\0' || *a == ' ') && *b == '\0') return *result = z, a;
	}
	return NULL;
}
int base_a_decode(const char* x, int* result) {
	int a, b;
	return (!(x = base_a_f(base_a_a, x, &a)) || *x != ' ' || !base_a_f(base_a_b, x+1, &b)) ? 1 :
	       (*result = (a << 6 | b) * 7859 % (BASE_A_MAX + 1), 0);
}
int base_a_encode(int x, char* result) {
	int h = (x * 123) % (BASE_A_MAX + 1);
	return (x < 0 || x > BASE_A_MAX) ? 1 :
	       (sprintf(result, "%s %s", base_a_a[h >> 6], base_a_b[h % 64]), 0);
}
int base_a_valid(const char* x) {
	int r;
	return !base_a_decode(x, &r);
}
#endif
