import matplotlib.pylab as plt

#these are the letters we are interested in when dealing with frequency analysis
letters = " abcdefghijklmnopqrstuvwxyz"

#The method to do frequency analysis: we just count the occurences of the given characters
def frequency_analysis(cipher_text):
    
    #The text we analyise
    cipher_text = cipher_text.lower()

    #we use a dictionary to store the letter frequency pair
    letter_frequency = {}
    
    #initialize the dictionary (of course with 0 frequencies)
    for letter in letters:
        letter_frequency[letter] = 0

    #let's consider the text we want to analyise
    for letter in cipher_text:
        #we keep increamenting the occurence of the given letter
        if letter in letters:
            letter_frequency[letter] += 1

    return letter_frequency

#plot the histogram of the letter_frequency pairs
def plot_distribution(letter_frequency):
    centers = range(len(letters))
    plt.bar(centers,letter_frequency.values(),align = 'center',tick_label = letter_frequency.keys())
    plt.xlim([0,len(letters)-1]) 
    plt.show()

def ceasar_crack(cipher_text):

    letter_frequency = frequency_analysis(cipher_text)
    print(letter_frequency)
    plot_distribution(letter_frequency)

if __name__== "__main__":
     
     cipher_text = "fpzyn sifqfrf enof enqtbf uf 25 Ijhjrgjw Ptrf ufrfkzsnpf pzyn frkzrz fefujwjpj xnlnsjsyhmf dfpfqj nof dfsdtbfsndn xfdnqtqfsxt Rfz f hmnsxnsxn fxnymfsxt Ufst fpzyn rzpflbnwnyxj syhmnyt enptrt Uf spmfsn ensf fpzyn fsfgf rfyfgbf fof sin gfrgt fpj f rfqnpt" 
     ceasar_crack(cipher_text)