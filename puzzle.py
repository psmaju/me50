from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
)
knowledge0.add(
    Or(AKnight,AKnave)
    )

knowledge0.add(
    Or(Not(AKnight),And(AKnight,AKnave))
    )
    

knowledge0.add(
    Or(Not(AKnave),Not(And(AKnight,AKnave)))
    )

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
)

knowledge1.add(
    And(Or(AKnight,AKnave),Or(BKnight,BKnave))
    )

knowledge1.add(
    Or(Not(AKnight),And(AKnave,BKnave))
    )

knowledge1.add(
    Or(Not(AKnave),Not(And(AKnave,BKnave)))
    )

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
)


knowledge2.add(
    And(Or(AKnight,AKnave),Or(BKnight,BKnave))
    )

knowledge2.add(
    Or(Not(AKnight),Or(And(AKnave,BKnave),And(AKnight,BKnight)))
    )

knowledge2.add(
    Or(Not(AKnave),Not(Or(And(AKnave,BKnave),And(AKnight,BKnight))))
    )

knowledge2.add(
    Or(Not(BKnight),Or(And(AKnave,BKnight),And(AKnight,BKnave)))
    )

knowledge2.add(
    Or(Not(BKnave),Not(Or(And(AKnave,BKnight),And(AKnight,BKnave))))
    )


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)

knowledge3.add(
    And(Or(AKnight,AKnave),Or(BKnight,BKnave),Or(CKnight,CKnave))
    )

knowledge3.add(
    Or(Not(AKnight),Or(AKnave,AKnight))
    )

knowledge3.add(
    Or(Not(AKnave),Or(AKnave,AKnight))
    )

knowledge3.add(
    Or(Not(BKnight),Or(Or(Not(AKnight),AKnave),Or(Not(AKnave),AKnave)))
    )

knowledge3.add(
    Or(Not(BKnave),Not(Or(Or(Not(AKnight),AKnave),Or(Not(AKnave),AKnave))))
    )

knowledge3.add(
    Or(Not(BKnight),CKnave)
    )

knowledge3.add(
    Or(Not(BKnave),Not(CKnave))
    )

knowledge3.add(
    Or(Not(CKnight),AKnight)
    )

knowledge3.add(
    Or(Not(CKnave),Not(AKnight))
    )


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
