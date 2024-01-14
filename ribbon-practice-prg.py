''' ribbon program : Practice program'''
import math

def solution(a, k):
    ''' logic '''
    min_length_ribbon_in_arry = min(a)
    current_length = min_length_ribbon_in_arry
    while True:
        ribbon_count = 0
        for item in a:
            ribbon_count += math.floor(item / current_length)
        if ribbon_count < k:
            if current_length -1 >= min_length_ribbon_in_arry:
                return current_length -1
            else:
                current_length = min_length_ribbon_in_arry-1
                while True:
                    ribbon_count = 0
                    for item in a:
                        ribbon_count += math.floor(item / current_length)
                    if ribbon_count >= k:
                        break
                    current_length -= 1
                return current_length
        current_length += 1

def solution2(a, k):
    ''' try2 '''
    sum_of_all_ribbon_sizes = sum(a)
    max_piece_size_possible = math.floor(sum_of_all_ribbon_sizes / k)
    max_ribbon_size = max(a)
    if max_piece_size_possible > max_ribbon_size:
        max_piece_size_possible = max_ribbon_size
    current_length = max_piece_size_possible
    while current_length > 1:
        ribbon_count = 0
        for item in a:
            print("item:", item)
            ribbon_count += math.floor(item / current_length)
            print("ribbon_count:", ribbon_count)
        if ribbon_count >= k:
            return current_length
        current_length -= 1
    return 1
