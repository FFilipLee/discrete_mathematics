def nim_sum(heaps):
    from functools import reduce
    from operator import xor
    return reduce(xor, heaps)

def ai_move(heaps):
    current_nim_sum = nim_sum(heaps)
    if current_nim_sum == 0:
        for i, heap in enumerate(heaps):
            if heap > 0:
                return i, 1
    else:
        for i, heap in enumerate(heaps):
            target_heap = heap ^ current_nim_sum
            if target_heap < heap:
                return i, heap - target_heap
    return None, None

def user_move(heaps):
    while True:
        try:
            print(f"Current heaps: {heaps}")
            pile = int(input("Choose a heap index (0-based): "))
            if pile < 0 or pile >= len(heaps) or heaps[pile] == 0:
                print("Invalid heap. Try again.")
                continue
            count = int(input(f"How many to remove from heap {pile}? "))
            if count < 1 or count > heaps[pile]:
                print("Invalid number of objects. Try again.")
                continue
            return pile, count
        except ValueError:
            print("Please enter valid integers.")

def play_nim_game(starting_player="user", initial_heaps=[3, 4, 5]):
    heaps = initial_heaps[:]
    current_player = starting_player

    while any(heap > 0 for heap in heaps):
        print("\n--- New Turn ---")
        if current_player == "user":
            print("Your move:")
            pile, count = user_move(heaps)
        else:
            print("AI's move:")
            pile, count = ai_move(heaps)
            print(f"AI removes {count} from heap {pile}")

        heaps[pile] -= count

        if all(heap == 0 for heap in heaps):
            print(f"\nAll heaps are empty. {current_player.upper()} wins!")
            break

        current_player = "ai" if current_player == "user" else "user"

if __name__ == "__main__":
    print("Welcome to Nim!")
    starter = input("Who should start? (user/ai): ").strip().lower()
    if starter not in ("user", "ai"):
        print("Invalid choice, defaulting to user.")
        starter = "user"
    play_nim_game(starting_player=starter)
