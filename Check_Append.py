
def check(set_of_values, what_are_you_looking_for):
    result = []
    split_result = []
    for value in set_of_values:
        if what_are_you_looking_for not in value:
            result.append(value)
        elif what_are_you_looking_for in value:
            splitted_value = value.split(',')
            split_result.append(splitted_value)
            for sp_value in split_result:
                joined_value =''.join(sp_value[0:])
            result.append(joined_value)
    return result
