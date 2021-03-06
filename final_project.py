def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    no_punct_file_contents = ""
    for char in file_contents:
       if char not in punctuations:
           no_punct_file_contents = no_punct_file_contents + char
    arr_file_contents = no_punct_file_contents.split(' ')
    good_file_contents = []
    for word in arr_file_contents:
        if word.lower() not in uninteresting_words and word.isalpha():
            good_file_contents.append(word.lower())
    frequencies = {}
    for word in good_file_contents:
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
# display the unpunctuated string
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()
 
# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
