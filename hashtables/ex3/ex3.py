def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for a in arrays[0]: 
        for b in arrays[1]: 
            for c in arrays[2]: 
                if a == b:
                    result.append(a)
                if b == c: 
                    result.append(b)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
