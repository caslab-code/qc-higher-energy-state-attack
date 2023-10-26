def get_closest_multiple_of(num, base_number):
    """Compute the nearest multiple of base_number. Needed because pulse enabled devices require 
    durations which are multiples of base_number samples.
    """
    return int(num + base_number/2) - (int(num + base_number/2) % base_number)

def get_closest_multiple_of_16(num):
    """Compute the nearest multiple of 16. Needed because pulse enabled devices require 
    durations which are multiples of 16 samples.
    """
    return get_closest_multiple_of(num, 16)
