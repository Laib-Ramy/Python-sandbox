def is_apocaliptic(n):
    return '666' in str(2**n)


bad_numbers={384, 390, 394, 278, 411, 285, 157, 287, 286, 434, 312, 443, 192, 
             218, 220, 222, 478, 224, 226, 355, 361, 366, 497, 243, 499, 245, 
             247, 251, 382}

def test_apocaliptic():
    maybe_bad={n for n in range(500) if is_apocaliptic(n)}
    if maybe_bad==bad_numbers:
        print("Test passed")
    else:
        print("Failed to detect the following apocaliptic numbers:")
        print(bad_numbers-maybe_bad)
        print("The following numbers were falsely detected as apocaliptic:")
        print(maybe_bad-bad_numbers)

test_apocaliptic()