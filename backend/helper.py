import re

# used for calling youtube video play
def extract_yt_term(query):
    pattern = r'play\s+(.*?)\s+on\s+YouTube'
    match = re.search(pattern, query,re.IGNORECASE)
    return match.group(1) if match else query


# used to remove unwanted words in the spoken string
def remove_words(input_string, words_to_remove): 
    words = input_string.split()
 
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
 
    result_string = ' '.join(filtered_words)

    return result_string