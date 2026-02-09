def ips_between(start, end):
    ip1 = [int(i) for i in start.split(".")]
    ip1.reverse()
    ip2 = [int(i) for i in end.split(".")]
    ip2.reverse()
    result = 0
    for i in range(len(ip1)):
        result += (ip2[i] - ip1[i]) * (256 ** i)

    print(result)

    return result

if __name__ == "__main__":
    print("Starting the test..")

    assert(ips_between("150.0.0.0", "150.0.0.1") == 1)
    assert(ips_between("10.0.0.0", "10.0.0.50") == 50)
    assert(ips_between("20.0.0.10", "20.0.1.0") == 246)
    assert(ips_between("10.11.12.13", "10.11.13.0") == 243)
    assert(ips_between("160.0.0.0", "160.0.1.0") == 256)

    print("Test finished..")