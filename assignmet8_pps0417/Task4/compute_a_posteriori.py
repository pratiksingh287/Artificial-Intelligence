import sys

h_prior_probability = [0.1, 0.2, 0.4, 0.2, 0.1]
ch_probability = [1, 0.75, 0.5, 0.25, 0]
lh_probability = [0, 0.25, 0.5, 0.75, 1]
try:
    result_file = open("result.txt", 'w')
except:
    print ('Unable to create output file!')


def nxt_obs_prob(observed_prob, h_prob):
    result = 0
    for index in range(5):
        result += (observed_prob[index] * h_prob[index])
    return result


def nxt_h_prob(obs_prob, h_prob, last_obs_prob):
    result = [0, 0, 0, 0, 0]
    for index in range(5):
        result[index] = ((obs_prob[index] * h_prob[index]) / last_obs_prob)
    return result


def check_obs_sequence(obs_sequence, h_prob, l_prior_prob, c_prior_prob):
    for val in range(len(obs_sequence)):
        if obs_sequence[val] == 'C':
            if (val + 1) == 1:
                h_prob = [0.1, 0.2, 0.4, 0.2, 0.1]

            h_prob = nxt_h_prob(ch_probability, h_prob, c_prior_prob)
            c_prior_prob = nxt_obs_prob(ch_probability, h_prob)
            l_prior_prob = 1 - c_prior_prob

            result_file.write('After Observation %d = %s\r\n' % (val, obs_sequence[:val + 1]))

            index = 0
            while index < 5:
                result_file.write('P(h%d | %s) = %8.5f\r\n' % (index + 1, obs_sequence[val], h_prob[index]))
                index += 1

            result_file.write('Probability that the next candy we pick will be C, given %s: %8.5f\r\n' % (obs_sequence[val], c_prior_prob))
            result_file.write('Probability that the next candy we pick will be L, given %s: %8.5f\r\n' % (obs_sequence[val], l_prior_prob))

        else:
            if (val + 1) == 1:
                h_prob = [0.1, 0.2, 0.4, 0.2, 0.1]
            h_prob = nxt_h_prob(lh_probability, h_prob, l_prior_prob)
            l_prior_prob = nxt_obs_prob(lh_probability, h_prob)
            c_prior_prob = 1 - l_prior_prob

            result_file.write('After Observation %d = %s\r\n' % (val, obs_sequence[:val + 1]))

            index = 0
            while index < 5:
                result_file.write('P(h%d | %s) = %8.5f\r\n' % (index + 1, obs_sequence[val], h_prob[index]))
                index += 1

            result_file.write('Probability that the next candy we pick will be C, given %s: %8.5f\r\n' % (obs_sequence[val], c_prior_prob))
            result_file.write('Probability that the next candy we pick will be L, given %s: %8.5f\r\n' % (obs_sequence[val], l_prior_prob))


def write_to_file(argv):

    if (len(argv) > 1):
        obs_sequence = argv[1]
        c_prior_prob = nxt_obs_prob(ch_probability, h_prior_probability)
        l_prior_prob = 1 - c_prior_prob
        h_prob = [0, 0, 0, 0, 0]

        result_file.write('Observation sequence : %s\r\n' % (obs_sequence))
        result_file.write('Length of sequence: %s\r\n' % str(len(obs_sequence)))
        check_obs_sequence(obs_sequence, h_prob, l_prior_prob, c_prior_prob)

    else:
        result_file.write('No observation sequence : \r\n')

        c_prior_prob = nxt_obs_prob(ch_probability, h_prior_probability)
        l_prior_prob = 1 - c_prior_prob

        result_file.write(
            'Probability that the next candy we pick will be C, given there is no observation: %8.5f\r\n' % (c_prior_prob))
        result_file.write(
            'Probability that the next candy we pick will be L, given there is no observation: %8.5f\r\n' % (l_prior_prob))

    result_file.close()
    print ('Check result.txt file for output!')


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) > 2:
        print 'Two command-line arguments are needed:'
        print('Usage: %s [observation-sequence]' % argv[0])
        print('or: %s' % argv[0])
        sys.exit(0)
    write_to_file(argv)


if __name__ == '__main__':
    main(sys.argv)
