def myPrint(*args):
    if True:
        print(*args)
        
def my_mod(dividend, divisor):
    mod = dividend%divisor
    if mod < 0:
        return mod + divisor
    else:
        return mod
    
def find_best_pattern(txt, pat):
    assert(len(pat) <= len(txt))
    
    pattern_length = len(pat)
    text_length = len(txt)
    prime = 2971215073
    
    pattern_hash = 0
    current_txt_hash = 0

    best_length = 0
    current_best_location = None
    
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
        
        
    #calculate first hash and pattern hash    
    for i in range(pattern_length):
        pattern_hash = (base*pattern_hash + ord(pat[i]))%prime
        current_txt_hash = my_mod((base*current_txt_hash + ord(txt[i])),prime)
        myPrint("first_hash=", current_txt_hash)
        myPrint("PATTERNHASH=", pattern_hash)

    i = 0
    #rolling hash
    while i < (len(txt) - len(pat) + 1):
        number_of_letters_rolling_over = 0 
        current_chunk = txt[i:i+pattern_length] 
        myPrint("i=", i)      
        myPrint("current_chunk=", current_chunk)
        myPrint("current_txt_hash=", current_txt_hash)
        myPrint("pattern_hash=", pattern_hash)
        if current_txt_hash == pattern_hash and current_chunk == pat:
                current_length += 1  
                myPrint("current_length=", current_length)
                current_location = i 

                number_of_letters_rolling_over = len(pat)
        
        #record best lengths
        else:
            myPrint("here1")
            if current_length > best_length:
                best_length = current_length
                current_best_location = current_location - (len(pat))*((current_length)-1)

            current_length = 0
            number_of_letters_rolling_over = 1 
        
        #re-hash
        if i + number_of_letters_rolling_over <= text_length - pattern_length:
            myPrint("here2")
            myPrint("current_txt_hash=", current_txt_hash)
            myPrint("ordvalue1=", ord(txt[i]))
            myPrint("exponent=", exponent)
            myPrint("ordvalue2=", ord(txt[i+pattern_length]))
            for j in range(number_of_letters_rolling_over):
                current_txt_hash = my_mod((base*(current_txt_hash-ord(txt[i])*exponent) + ord(txt[i+pattern_length])),prime)
                i += 1
                
            myPrint("newhash=", current_txt_hash)
            
            #in case of negative hash value
            if current_txt_hash < 0:
                current_txt_hash = current_txt_hash + prime
        else:
            i += number_of_letters_rolling_over

    #record best lengths last time
    if current_length > best_length:
        best_length = current_length
        current_best_location = current_location - (len(pat))*((current_length)-1)

    
    return (best_length, current_best_location)


