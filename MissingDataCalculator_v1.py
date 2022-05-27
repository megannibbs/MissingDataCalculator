#PART I: PROMPT USER TO INPUT MATRIX

#create dictionary (= matrix) and taxon counter
matrix = {}
tax1 = []
comp_list = []
#comp_list_sep = []

#populate dictionary with matrix
while True:
    taxon = input("Enter the taxon name. When you are finished, hit enter: ")
#loop breaks when no taxon name is input
    if len(taxon) == 0:
        break
    if tax1.count(taxon) >= 1:
        print('You have already input this taxon.')
        continue
    else:
#match each taxon with characters from NEXUS file
        characters = input("Enter your character string as state numbers, starting at 0: ")
        matrix[taxon] = characters
        comp_list.extend(list(characters))
        tax1.append(taxon)
for key,val in matrix.items():
    print('>' + key + '    ' + val )

#===============================================

#PART II: SELECT INCLUDED TAXA

#prompt user for taxa you are looking to calculate missing and/or inapplicable 
taxa = []
selec_tax = []

while True:
    selection = input("Which taxa would you like to calculate missing data for (input one at a time)? When you are finished, press enter. ")
#ends loop when user is done inputting taxa
    if len(selection) == 0:
        break
#assures input taxa are keys in matirx and will have associated values
    if not selection in matrix:
        print('Not a taxon in matrix. Double check for spaces and typos.')
        continue
    if taxa.count(selection) >= 1:
        print('You have already included this taxon.')
        continue
#add values for taxon key to list for math; add taxa to list to check for duplicates
    else:
        selec_tax.extend(matrix.get(selection))
        taxa.append(selection)
        continue

#================================================

#PART III: PERFORM CALCULATIONS DETERMINED BY USER

#functions for missing characters by taxon defined by user       

def missing():
#count occurrences of '?' in values for taxon
    missing_count = (selec_tax.count('?'))
#perform operation for % unknown character states in matrix
    math_missing = (missing_count / len(selec_tax))
    return(math_missing)

#function for inapplicable characters by taxon defined by user       
def inapp():
#count occurences of '-' in taxon list
    inapp_count = selec_tax.count('-')
#perform operations for inapplicable character states in matrix
    math_inapp = (inapp_count / len(selec_tax))
    return(math_inapp)

#function for missing and inapplicable characters by taxon defined by user - combine values above
def inapp_missing():
    inapp_missing_count = selec_tax.count('?') + selec_tax.count('-')
    math_both = (inapp_missing_count / len(selec_tax))
    return(math_both)

#prompt user for function to call for missing and/or inapplicable character states; print selection
while True:
    call = input("What calculation would you like to perform? Type 'missing' for unknown scorings, 'inapp' for inapplicable scorings, or 'both' for both (Press enter when done): ")
    if call == 'missing':
        print_missing = missing()
        print(print_missing)
        continue
    if call == 'inapp':
        print_inapp = inapp()
        print(print_inapp)
        continue
    if call == 'both':
        print_both = inapp_missing()
        print(print_both)
        continue
    if len(call) == 0:
        break
    else:
        #assure input is valid
        print('Invalid calculation option.')
        continue
