def my_mod(dividend, divisor):
    mod = dividend%divisor
    if mod < 0:
        return mod + divisor
    else:
        return mod

# txt is the text representing our genome
# pats is a list of the patterns to look for
def HFGS_Test(txt):
    pats = ["GCA", "GCC", "GCG", "GCT"]
    results = None 
    print("Testing for HFGS...", end = "")
    
    for pat in pats:
        assert(len(pat) <= len(txt))
    
    second_length = ""
    third_length = ""
    pattern_length = len(pats[0])
    text_length = len(txt)
    prime = 2971215073
    
    current_txt_hash = 0

    best_length = 0
    current_best_location = None
    second_location = None
    third_location = None
    
    current_length = 0
    current_location = None
    
    exponent = 1
    base = 256
    i = 0
    
    if pattern_length > text_length:
        return None
    
    #calculate exponent
    for i in range(pattern_length - 1):
        exponent = (base**(pattern_length-1))%prime
    
    # Create a dictionary of patterns mapped to their hashes
    pats_dictionary = {}
    for pat in pats:
        pattern_hash = 0
        for i in range(pattern_length):
            pattern_hash = (base*pattern_hash + ord(pat[i]))%prime
        pats_dictionary[pat] = pattern_hash
        
    #calculate first hash and pattern hash    
    for i in range(pattern_length):
        current_txt_hash = my_mod((base*current_txt_hash + ord(txt[i])),prime)

    i = 0
    #rolling hash
    while i < (len(txt)):
        number_of_letters_rolling_over = 0 
        current_chunk = txt[i:i+pattern_length]
        for pat in pats:
            pattern_hash = pats_dictionary[pat]
            if current_txt_hash == pattern_hash and current_chunk == pat:
                current_length += 1  
                current_location = i 

                number_of_letters_rolling_over = pattern_length
                break
        
        #record best lengths
        else:
            if current_length > best_length:
                third_length = second_length
                third_location = second_location
                second_length = best_length
                second_location = current_best_location
                best_length = current_length
                current_best_location = current_location - (pattern_length)*((current_length)-1)

            current_length = 0
            number_of_letters_rolling_over = 1 
        
        #re-hash
        if i + number_of_letters_rolling_over <= text_length - pattern_length:
            for j in range(number_of_letters_rolling_over):
                current_txt_hash = my_mod((base*(current_txt_hash-ord(txt[i])*exponent) + ord(txt[i+pattern_length])),prime)
                i += 1
            
            #in case of negative hash value
            if current_txt_hash < 0:
                current_txt_hash = current_txt_hash + prime
        else:
            i += number_of_letters_rolling_over

    #record best lengths last time
    if current_length > best_length:
        third_length = second_length
        third_location = second_location
        second_length = best_length
        second_location = current_best_location
        best_length = current_length
        current_best_location = current_location - (len(pat))*((current_length)-1)
        
    #determine diseaase positive/negative    
    if best_length < 1:
        return None
    elif best_length == 18 and second_length == 14 and third_length = 12:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", third_length, "Location 3: Index", third_location, "Negative Result: Normal Allele"
        
    elif best_length == 14 and second_length == 12 and third_length = 12:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", third_length, "Location 3: Index", third_location, "Negative Result: Normal Allele"
        
    elif best_length == 14 and second_length == 12 and third_length = 8:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", third_length, "Location 3: Index", third_location, "Negative Result: Normal Allele"
        
    elif best_length == 22:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", third_length, "Location 3: Index", third_location, "Positive Result: Pathogenic Allele"
        
    elif best_length >= 18 and second_length >= 18:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", third_length, "Location 3: Index", third_location, "Positive Result: Pathogenic Allele"
        
    elif best_length > 19:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", third_length, "Location 3: Index", third_location, "Positive Result: Pathogenic Allele"
        
    else:
        return "GCN Repeat Length 1:", best_length, "Location 1: Index", current_best_location, "GCN Repeat Length 2:", second_length, "Location 2: Index", second_location, "GCN Repeat Length 3:", t'hird_length, "Location 3: Index", third_location, "Undetermined Result"








    



