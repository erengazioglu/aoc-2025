from .part2 import check_substr

def test_check_substr(id, id_len, sub_len, verbose=False):
    print(f"check {id}({sub_len}) -> {check_substr(id, id_len, sub_len, verbose)}")

def suite(verbose=False):
    test_check_substr("123212321232", 12, 3, verbose)
    test_check_substr("123212321232", 12, 4, verbose)
    test_check_substr("3939393039", 10, 4, verbose)


if __name__ == "__main__":
    suite()