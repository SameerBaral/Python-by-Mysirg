# File Handling:-

# file me oprration karne ke liye kuch common steps follow karna hoga
# 1) Open the File
# 2) Do operation Like: read,write,append etc.
# 3) Close the File 



# Writing in file, w mode=> file not exist then create and write the contents


def writing(filename,text):
    f = open(filename,"w")
    f.write(text)
    f.close()


# -----------------------------------------
# append mode jo file ani hai uske content ke age aur dalege last me content


def append(filename,text):
    f = open(filename,"a")
    f.write(text)
    f.close()

append("file1.txt","append content")


# ------------------------------------------

# reading mode

def reading(filename):
    try:
        f = open(filename,"r")
        text = f.read()
        print(text)
        f.close()
    except FileNotFoundError as e:
        print("File Not Found Error")

reading("file1.txt")


# ------------------------------------------

# Search a word in a file

def search(filename,word):
    try:
        f = open(filename,"r")
        line_count = 0 
        for line in f.readlines():
            line_count+=1
            strlist = line.split(' ')
            word_count = 0
            for w in strlist:
                word_count+=1
                if word==w:
                    return(line_count,word_count)
        else:
            return None
        f.close()
    except FileNotFoundError:
        print("File Not Found Error")

s = "MySirG Education Services Private Limited\n"
s+="Saurabh Shukla Classes"
s+="Premimum website of MySirG"
# append("file1.txt",s)

t = search("file1.txt","website")
print(t)

