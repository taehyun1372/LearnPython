import copy


def sum_of_intervals(intervals):
    final_intervals = []
    for original_set in intervals:
        if final_intervals == []:
            final_intervals.append(original_set)
        else:
            for final_set in final_intervals:
                if original_set[0] > final_set[0] and original_set[1] < final_set[1]:
                    pass
                elif original_set[0] < final_set[0] and original_set[1] > final_set[1]:
                    final_intervals.remove(final_set)
                    final_intervals.append(original_set)
                elif original_set[0] <= final_set[1]:
                    final_intervals.remove(final_set)
                    final_intervals.append((final_set[0], original_set[1]))
                elif original_set[1] >= final_set[0]:
                    final_intervals.remove(final_set)
                    final_intervals.append((original_set[0], final_set[1]))
                else:
                    final_intervals.append(original_set)
    return final_intervals

def sum_of_intervals2(intervals):
    final = []
    for set in intervals:
        final += [i for i in range(set[0], set[1])]
        final = list(set(final))
    return final

if __name__ == "__main__":
    print(sum_of_intervals2( [(1, 5)] ))
    print(sum_of_intervals2( [(1, 5), (6, 10)] ))
    print(sum_of_intervals2( [(1, 5), (1, 5)] ))
    print(sum_of_intervals2( [(1, 4), (7, 10), (3, 5)] ))

