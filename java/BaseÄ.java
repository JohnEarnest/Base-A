// Base-Ä encoder-decoder library
import java.util.*;

public class BaseÄ {
	private static final String[] a = {
		"Atomic", "Ballistic", "Big", "Boxer", "Bracer", "Brawler", "Breaker", "Challenger",
		"Champion", "Cherno", "Chrome", "Cobra", "Contender", "Coyote", "Crimson", "Decider",
		"Diablo", "Dingo", "Disrupter", "Echo", "Eden", "Falcon", "Fearless", "Galaxy",
		"Gallant", "Gipsy", "Golden", "Grand", "Grizzly", "Guardian", "Horizon", "Hydra",
		"Intrepid", "Keeper", "Legend", "Mammoth", "Matador", "Mighty", "Mountain", "Neon",
		"Nova", "Phantom", "Protector", "Puma", "Righteous", "Romeo", "Shaolin", "Shining",
		"Solar", "Spartan", "Steady", "Striker", "Tacit", "Tesla", "Tiger", "Titan", "Valiant",
		"Viper", "Vulcan", "Warden", "Warrior", "Wildcat", "Yankee", "Zenith"
	};
	private static final String[] b = {
		"Absolute", "Ajax", "Alpha", "Apostle", "Ares", "Artemis", "Assassin", "Athena",
		"Avenger", "Banzai", "Blue", "Brave", "Bravo", "Brutus", "Cerberus", "Colossus",
		"Corinthian", "Courage", "Cruiser", "Danger", "Dawn", "Dazzle", "Delta", "Dreadnought",
		"Eureka", "Finisher", "Fist", "Fortress", "Fury", "Gauntlet", "Gladius", "Hyperion",
		"Infinite", "Intercept", "Judas", "Kilo", "Lightning", "Mega", "November", "Omega",
		"Paladin", "Phoenix", "Prophet", "Real", "Redeemer", "Resolve", "Rogue", "Romeo",
		"Ronin", "Saber", "Sentinel", "Sierra", "Specter", "Tango", "Thunder", "Turbo",
		"Typhoon", "Venus", "Victory", "Vigor", "Yukon", "Zero", "Zeus", "Zulu"
	};
	public static final int MAX = a.length * b.length - 1;
	private static final Map<Integer, String> o2s = new HashMap<>();
	private static final Map<String, Integer> s2o = new HashMap<>();
	static {
		for (int x = 0; x <= MAX; x++) {
			int h = (x * 123) & MAX;
			String s = a[(h >> 6) % a.length] + ' ' + b[h % b.length];
			o2s.put(x, s); s2o.put(s.toLowerCase(), x);
		}
	}
	public static boolean valid(String x) { return x != null && s2o.containsKey(x.toLowerCase()); }
	public static String encode(int x) {
		if (x >= 0 && x <= MAX) return o2s.get(x);
		throw new IllegalArgumentException("'" + x + "' cannot be encoded in Base-Ä.");
	}
	public static int decode(String x) {
		if (valid(x)) return s2o.get(x.toLowerCase());
		throw new IllegalArgumentException("'" + x + "' is not a valid Base-Ä identifier.");
	}
}