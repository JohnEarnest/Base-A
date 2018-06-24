// Base-Ä encoder-decoder library
if (typeof(BaseÄ) == 'undefined') {
	BaseÄ = (_ => {
		const a = [
			'Atomic', 'Ballistic', 'Big', 'Boxer', 'Bracer', 'Brawler', 'Breaker', 'Challenger',
			'Champion', 'Cherno', 'Chrome', 'Cobra', 'Contender', 'Coyote', 'Crimson', 'Decider',
			'Diablo', 'Dingo', 'Disrupter', 'Echo', 'Eden', 'Falcon', 'Fearless', 'Galaxy',
			'Gallant', 'Gipsy', 'Golden', 'Grand', 'Grizzly', 'Guardian', 'Horizon', 'Hydra',
			'Intrepid', 'Keeper', 'Legend', 'Mammoth', 'Matador', 'Mighty', 'Mountain', 'Neon',
			'Nova', 'Phantom', 'Protector', 'Puma', 'Righteous', 'Romeo', 'Shaolin', 'Shining',
			'Solar', 'Spartan', 'Steady', 'Striker', 'Tacit', 'Tesla', 'Tiger', 'Titan', 'Valiant',
			'Viper', 'Vulcan', 'Warden', 'Warrior', 'Wildcat', 'Yankee', 'Zenith',
		]
		const b = [
			'Absolute', 'Ajax', 'Alpha', 'Apostle', 'Ares', 'Artemis', 'Assassin', 'Athena',
			'Avenger', 'Banzai', 'Blue', 'Brave', 'Bravo', 'Brutus', 'Cerberus', 'Colossus',
			'Corinthian', 'Courage', 'Cruiser', 'Danger', 'Dawn', 'Dazzle', 'Delta', 'Dreadnought',
			'Eureka', 'Finisher', 'Fist', 'Fortress', 'Fury', 'Gauntlet', 'Gladius', 'Hyperion',
			'Infinite', 'Intercept', 'Judas', 'Kilo', 'Lightning', 'Mega', 'November', 'Omega',
			'Paladin', 'Phoenix', 'Prophet', 'Real', 'Redeemer', 'Resolve', 'Rogue', 'Romeo',
			'Ronin', 'Saber', 'Sentinel', 'Sierra', 'Specter', 'Tango', 'Thunder', 'Turbo',
			'Typhoon', 'Venus', 'Victory', 'Vigor', 'Yukon', 'Zero', 'Zeus', 'Zulu',
		]
		const max   =       a.length * b.length - 1
		const err   = (x,y) => { if (!x) throw new Error(y) }
		const norm  = x     => (x || '').toLowerCase()
		const range = x     => err(x >= 0 && x <= max, `'${x}' cannot be encoded in Base-Ä.`)
		const valid = x     => err(norm(x) in s2o,     `'${x}' is not a valid Base-Ä identifier.`)
		const h     = Array.from(Array(1+max)).map((_, i) => i * 123 % (1+max))
		const n     = h.map(x => a[x >> 6] + ' ' + b[x % b.length])
		const o2s   = n.reduce((d,n,i) => (d[i]      =n, d), {})
		const s2o   = n.reduce((d,n,i) => (d[norm(n)]=i, d), {})

		return {
			max:    max,                          // maximum encodable ordinal
			valid:  x => norm(x) in s2o,          // is a string a valid encoding?
			encode: x => o2s[range(x),x],         // convert ordinal to printable string
			decode: x => s2o[norm((valid(x),x))], // convert printable string to ordinal
		}
	})()
}
