/ Base-Ä encoder-decoder library
\d .baseA

a: ("Atomic";"Ballistic";"Big";"Boxer";"Bracer";"Brawler";"Breaker";"Challenger";"Champion";"Cherno";"Chrome";"Cobra";"Contender";"Coyote";"Crimson";"Decider";"Diablo";"Dingo";"Disrupter";"Echo";"Eden";"Falcon";"Fearless";"Galaxy";"Gallant";"Gipsy";"Golden";"Grand";"Grizzly";"Guardian";"Horizon";"Hydra";"Intrepid";"Keeper";"Legend";"Mammoth";"Matador";"Mighty";"Mountain";"Neon";"Nova";"Phantom";"Protector";"Puma";"Righteous";"Romeo";"Shaolin";"Shining";"Solar";"Spartan";"Steady";"Striker";"Tacit";"Tesla";"Tiger";"Titan";"Valiant";"Viper";"Vulcan";"Warden";"Warrior";"Wildcat";"Yankee";"Zenith")
b: ("Absolute";"Ajax";"Alpha";"Apostle";"Ares";"Artemis";"Assassin";"Athena";"Avenger";"Banzai";"Blue";"Brave";"Bravo";"Brutus";"Cerberus";"Colossus";"Corinthian";"Courage";"Cruiser";"Danger";"Dawn";"Dazzle";"Delta";"Dreadnought";"Eureka";"Finisher";"Fist";"Fortress";"Fury";"Gauntlet";"Gladius";"Hyperion";"Infinite";"Intercept";"Judas";"Kilo";"Lightning";"Mega";"November";"Omega";"Paladin";"Phoenix";"Prophet";"Real";"Redeemer";"Resolve";"Rogue";"Romeo";"Ronin";"Saber";"Sentinel";"Sierra";"Specter";"Tango";"Thunder";"Turbo";"Typhoon";"Venus";"Victory";"Vigor";"Yukon";"Zero";"Zeus";"Zulu")

m:      -1+*/(#a;#b)                          / maximum encoding
i:      !1+m                                  / indices
n:      {x," ",y}.'+(a;b)@'64 64\:(1+m)!123*i / names
o2s:    i!n                                   / ordinal -> string
s2o:    (_n)!i                                / string -> ordinal

valid:  ~^s2o@_:
encode: o2s
decode: s2o@_:
