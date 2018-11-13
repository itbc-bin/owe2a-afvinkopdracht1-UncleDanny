# Naam: Tymon Simonides
# Datum: 6 oktober 2018
# Versie: 1.3
class ExtensionError(Exception):
    pass


def main():
    file = "/home/tymon/Documents/Bio-Informatics/Periode 2/Weektaak 1/Afvinkopdracht/alpaca.fas"
    try:
        headers, seqs = read_contents(file)
    except TypeError:
        print("TypeError: The function returned the wrong type, or returned empty.")
    else:
        searchterm = input("Enter a search term: ")
        for i in range(len(headers)):
            if searchterm in headers[i]:
                print(headers[i])
                cutsInSequence(seqs[i])
           
def read_contents(file_name):
    try:
        if not file_name.endswith(".fa"):
            raise ExtensionError
        else:
            file = open(file_name)
    except ExtensionError:
        print("ExtensionError: File is not in fasta format.")
    except IOError:
        print("IOError: File can not be found")
    else:
        headers = []
        seqs = []
        sequenceLine = ""
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequenceLine != "":
                    seqs.append(sequenceLine)
                    sequenceLine = ""
                headers.append(line)
            else:
                sequenceLine += line
        seqs.append(sequenceLine)
        return headers, seqs

def is_dna(seq):
    totalDNA = sum(seq.count(ACGT) for ACGT in ("A", "C", "G", "T"))
    if len(seq) == totalDNA:
        return True
    else:
        return False    

def cutsInSequence(seq):
    restrictionEnzyms = []
    file = open ("enzymen.txt")

    for line in file:
        enzym, enzymSeq = line.split()
        enzymSeq = enzymSeq.replace("^","")
        enzymen = [[enzym, enzymSeq]]
        for i in enzymen:
            if i[1] in seq:
                restrictionEnzyms.append(i[0])
    print(", ".join(restrictionEnzyms), "cut in the given sequence\n")
                
main()

