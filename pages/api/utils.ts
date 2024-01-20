var map = {}
const tone = ["C", "D", "E", "F", "G", "A", "B"]

for (let i = 0; i < 20;  i++){
    var character = String.fromCharCode(i+65);
    map[character] = tone[(i+70) % 7] + (i+21)//7 
}

/* map["A"] = "C4";
map["B"] = "D4";
map["C"] = "E4";
map["D"] = "F4";
map["E"] = "G4";
;ap["F"] = "A5";
map["G"] = "B5";
map["H"] = "C5";
map["I"] = "D5";
map */

