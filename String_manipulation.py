Input_text = ''' AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTAÑACORP
HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE
WITH THE OBJECTIVES FOR THE YEAR. THE MAIN DRIVER OF THE SALES HAS
BEEN
THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING
DEPARTMENT.
OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH
THE BOARD
CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS
SATISFACTORY
AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD
EXPECTS
AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS. '''
words = Input_text.split()
redacted = [''.join('x' if w.isdigit() else w for w in word) for word in words]
ascii_text = [word.encode('ascii',
                          errors='replace').decode('ascii')
              for word in redacted]
newlines = [word + '\n' if word.endswith('.') else word for word in
            ascii_text]
LINE_SIZE = 80
lines = []
line = ''
for word in newlines:
    if line.endswith('\n') or len(line) + len(word) + 1 > LINE_SIZE:
        lines.append(line)
        line = ''
    line = line + ' ' + word
lines = [line.title() for line in lines]
result = '\n'.join(lines)
print(result)