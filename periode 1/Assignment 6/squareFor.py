getal = int(input("Voer een getal in: \n"))         # (1, S.getal) -> (PC + 1, S[getal-> int(input(S.getal + (5)))])
for a in range(getal):                              # (2,S) ->fVRB(firstLine(B, S) when S[a] == range(getal) | (PC,S) ->fVRB(skipAfter(B, S) when S[a] != range getal)
    output = ""                                     # (3, S.output) -> (PC + 1, S[output-> S.output + ()])
    for i in range(getal):                          # (4,S) ->fVRB(firstLine(B, S) when S[a] == range(getal) | (PC,S) ->fVRB(skipAfter(B, S) when S[a] != range getal)
        output = output + "*"                       # (5, S.output) -> (PC + 1, S[output-> S.output + S.output + (*)])
    print(output)                                   # (6, S.output) -> (PC + 1, S[output-> print(S.output)])
