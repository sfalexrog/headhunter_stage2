from random import randint
import task2

MAXNUM = 9999999

s = ''.join([str(i) for i in range(1, MAXNUM)])

def get_random_substring(length):
    start = randint(0, MAXNUM - length)
    substr = s[start:start + length + 1]
    firstpos = s.find(substr)
    if (start != firstpos):
        #print('First occurence does not match the random start: {} (expected {})'.format(firstpos, start))
        pass
    return (firstpos + 1, substr)

def check_position(number):
    calc_position = task2.get_number_position(number) - 1
    nrepr = str(number)
    num_at_pos = s[calc_position:calc_position + len(nrepr)]
    print('Expected number: {}, found number: {}'.format(nrepr, num_at_pos))
    return nrepr == num_at_pos

if __name__ == '__main__':
    print('Running tests for task2...')
    print('Testing if position calculations are correct')
    for i in range(10):
        n = randint(1, MAXNUM)
        if (not check_position(n)):
            print('Warning! Position calculation failed for {}'.format(n))
    print('Running tests for edge cases')
    for i in range(99):
        for j in range(1, 5):
            seq = str(i) * j
            real_ans = s.find(seq) + 1
            if real_ans < 0:
                continue
            ans = task2.get_sequence_pos(seq)
            if ans != real_ans:
                print('Failing sequence: {}, expected {}, got {}'.format(seq, real_ans, ans))
    fail_count = 0
    pass_count = 0
    TEST_NR = 9999999
    FAIL_THRESHOLD = 1
    failed_tests = []
    print('Testing if substring analysis is correct')
    for i in range(TEST_NR):
        rss = get_random_substring(randint(1, 20))
        ans = task2.get_sequence_pos(rss[1])
        # print('Expecting to find {} at {}...'.format(rss[1], rss[0]))
        if (ans != rss[0]):
            print('Test failed! Expected answer: {}, actual: {} (substring {})'.format(rss[0], ans, rss[1]))
            failed_tests.append((rss[1], rss[0], ans)) # Substring, expected answer, actual answer
            fail_count += 1
            if fail_count >= FAIL_THRESHOLD:
                print('Failure limit hit; stopping...')
                break
        else:
            pass_count += 1
        if (i % 100 == 0):
            print('Tests finished: {} out of {}'.format(i, TEST_NR))
    print('Testing finished; {} tests passed, {} failed'.format(pass_count, fail_count))
    for test in failed_tests:
        print('Failed test case: substring {}, expected answer: {}, got answer: {}'.format(test[0], test[1], test[2]))
