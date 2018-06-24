/**
* Unit Tests for the Java Base-Ä implementation
**/

import java.util.stream.*;

public class Test {
	static boolean thrown(Runnable test, String message) {
		try { test.run(); return false; }
		catch (Exception e) { return e.getMessage().equals(message); }
	}

	public static void main(String[] args) {

		// every combination must be distinct
		assert IntStream.rangeClosed(0, BaseÄ.MAX)
		                .mapToObj(BaseÄ::encode)
		                .collect(Collectors.toSet())
		                .size() == BaseÄ.MAX + 1 : "encoding must be injective.";

		// every combination must round-trip successfully
		IntStream.rangeClosed(0, BaseÄ.MAX).forEach(x -> {
			assert BaseÄ.decode(BaseÄ.encode(x)) == x : "encoding must be bijective.";
		});

		// invalid encodes
		assert thrown(() -> BaseÄ.encode(  -1), "'-1' cannot be encoded in Base-Ä.");
		assert thrown(() -> BaseÄ.encode(8514), "'8514' cannot be encoded in Base-Ä.");

		// invalid decodes
		assert thrown(() -> BaseÄ.decode(null),    "'null' is not a valid Base-Ä identifier.");
		assert thrown(() -> BaseÄ.decode("Gipsy"), "'Gipsy' is not a valid Base-Ä identifier.");
		assert thrown(() -> BaseÄ.decode("1 2"),   "'1 2' is not a valid Base-Ä identifier.");

		// validity checks
		assert BaseÄ.valid("Gipsy Danger" ) == true;
		assert BaseÄ.valid("Gipsy Doofus" ) == false;
		assert BaseÄ.valid("Goatse Danger") == false;

		System.out.println("all tests successful.");

		// sample a few names for visual inspection
		System.out.println(
			IntStream.rangeClosed(0, 15).mapToObj(BaseÄ::encode).collect(Collectors.toList())
		);
	}
}
