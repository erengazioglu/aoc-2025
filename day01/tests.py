from .solution import count_clicks

def test_count_clicks(dial, turns):
    print(f"{dial}\tturns {turns}\t-> finishes at {(dial + turns) % 100}, clicks {count_clicks(dial, turns)} times")

def suite():
    test_count_clicks(0, 1)
    test_count_clicks(0, -1)
    test_count_clicks(10, -30)
    test_count_clicks(30, -10)
    test_count_clicks(0, -20)
    test_count_clicks(0, 20)
    test_count_clicks(0, 120)


if __name__ == "__main__":
    suite()