def solution(text, ending):
    #reverse both text and ending
    reversed_text = text[::-1]
    reversed_ending = ending[::-1]
    print("reversed text:", reversed_text)
    print("reversed ending:", reversed_ending)
    #compare length
    length_text = len(text)
    length_ending = len(ending)
    print("length of text: ", length_text)
    print("length of ending: ", length_ending)
    #slice into same lenght
    reversed_sliced_text = reversed_text[0:length_ending]
    print("reversed_sliced_text:", reversed_sliced_text)
    #compare
    if reversed_sliced_text == reversed_ending:
        print("True")
        return True
    else :
        print("False")
        return False
            
solution("samurai", "ai")