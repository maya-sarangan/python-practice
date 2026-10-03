"""Quest 59 -- Caesar Cipher Encoder   [World 7: The Loop Lair]

Julius Caesar really used this code to send orders to his generals. Now
you can send secret messages too.

YOUR MISSION
    Shift every letter of a whole message. Leave spaces and punctuation
    alone.

EXAMPLES
    caesar_encode('attack at dawn', 3)  ->  'dwwdfn dw gdzq'
    caesar_encode('zoo', 1)             ->  'app'
    caesar_encode('hello world', 13)    ->  'uryyb jbeyq'
    caesar_encode('dragons!', 1)        ->  'esbhpot!'
    caesar_encode('abc', 0)             ->  'abc'

WHEN YOU ARE READY
    python3 practice.py 59            grade it
    python3 practice.py 59 --hint     ask for a nudge
    python3 practice.py 59 --play     play with it once it works 🎮
"""


def caesar_encode(message, shift):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    message = input("Message to encode: ")
    shift = int(input("Shift by how much? "))
    print("Secret message:", caesar_encode(message, shift))
